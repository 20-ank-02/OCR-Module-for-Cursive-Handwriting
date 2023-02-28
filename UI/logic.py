from ui_simple import *
from PySide6.QtWidgets import QFileDialog, QGraphicsScene, QLineEdit, QCompleter
from PySide6.QtGui import QIntValidator
from PySide6.QtCore import QRectF, QEvent
from OCR_class import *
import qdarktheme
from spellchecker import SpellChecker


class UI_Bindings(Ui_MainWindow, OCR):
    newUserName = 'called'

    def __init__(self, window):
        # super.__init__()
        self.setupUi(window)
        window.setWindowTitle('R.A.M.P')
        self.userList(0, 0)
        self.modelList(0)
        self.theme(0)
        self.userComboBox.activated.connect(
            lambda selected=0, count=1: self.userList(selected, count))
        self.comboBox.activated.connect(self.modelList)

        self.OpenImageBtn.clicked.connect(self.openImgBtn)
        self.ImageLabel.wheelEvent = self.zoom
        self.ExportBtn.clicked.connect(self.export)
        self.OCRBtn.clicked.connect(self.imgText)
        self.lineEditList = []

        # ---------------------

        # self.ImageLabel.resizeEvent = self.doSomething

    def theme(self, count):
        if count == 0:
            self.themeBox.addItems(qdarktheme.get_themes())

        self.themeBox.currentTextChanged.connect(qdarktheme.setup_theme)

    def openImgBtn(self):
        # self.statusLabel.setText('not started')
        self.fileName = QFileDialog.getOpenFileName(
            None, '', "", "Images (*.png *.xpm *.jpg)")

        if self.fileName == ('', ''):
            pass
        else:
            self.clearLineEdits()
            self.showImg(self.fileName[0])

    def showImg(self, imgpath):
        # self.imageViewer(imgpath)
        self.scene = QGraphicsScene()
        self.pixmap = QPixmap(imgpath)
        self.scene.addPixmap(self.pixmap)
        self.ImageLabel.setScene(self.scene)
        self.ImageLabel.fitInView(
            QRectF(self.pixmap.rect()), Qt.KeepAspectRatio)

        # -------Qlabel image show------
        # self.ImageLabel.show()
        # self.verticalLayout.addWidget(self.ImageLabel)
        # self.ImageLabel.setPixmap(self.pixmap.scaled(
        #     (self.ImageLabel.width()-10), (self.ImageLabel.height()-10), aspectMode=Qt.KeepAspectRatio, mode=Qt.SmoothTransformation))
        # self.splitter.splitterMoved.connect(self.splitterResize)

    # def splitterResize(self, pos):
        #     # print(pos)
        #     self.ImageLabel.setScaledContents(True)

        # self.ImageLabel.setPixmap(self.pixmap.scaled(
        #     (self.ImageLabel.width()-10), (self.ImageLabel.height()-10), aspectMode=Qt.KeepAspectRatio, mode=Qt.SmoothTransformation))

    def zoom(self, event):

        if event.angleDelta() == QPoint(0, 120):
            # print(event.angleDelta())
            self.ImageLabel.scale(2, 2)

        if event.angleDelta() == QPoint(0, -120):
            # print(event.angleDelta())
            self.ImageLabel.scale(0.5, 0.5)

    def rngSel(self):
        # if self.lineEditList:
        #     for i in range(len(self.lineEditList)):
        #         self.tempResult[i][2] = self.lineEditList[i][0].text()

        self.clearLineEdits()
        if self.rangeLow.text() == '' or self.rangeHigh.text() == '':
            self.createLineEdits(0, 0)
        else:
            print(int(self.rangeLow.text()),
                  int(self.rangeHigh.text()))
            self.createLineEdits(int(self.rangeLow.text()),
                                 int(self.rangeHigh.text()))

    def imgText(self):

        self.DetailscheckBox.stateChanged.connect(self.details)
        self.imgRead(
            self.fileName[0], self.modelSelected)
        self.rangeLow.setText('0')
        self.rangeHigh.setText('100')
        validator = QIntValidator(0, 100, self.rangeLow)
        self.rangeLow.setValidator(validator)
        self.rangeHigh.setValidator(validator)
        self.rangeLow.returnPressed.connect(self.rngSel)
        self.rangeHigh.returnPressed.connect(self.rngSel)

        self.clearLineEdits()
        self.createLineEdits(0, 100)

        # self.ResultText.clear()
        # self.ResultText.appendPlainText(self.tempResult)
        # self.statusLabel.setText('done')
        # for i in range(len(text)): for list of strings
        #     self.ResultText.appendPlainText(text[i])

    def clearLineEdits(self):
        if self.lineEditList:
            for i in range(len(self.lineEditList)):
                self.lineEditList[i][0].deleteLater()

            self.lineEditList.clear()

    def createLineEdits(self, low, high):
        strList = ['most', 'language', 'extension', 'is']
        self.lineEditList = []
        print(self.lineEditList)
        for i in range(len(self.tempResult)):
            if self.tempResult[i][3]*100 >= low and self.tempResult[i][3]*100 <= high:

                resultLineEdit = QLineEdit(
                    self.centralwidget)  # --------
                # self.resultLineEdit.setFocusPolicy(Qt.ClickFocus)
                resultLineEdit.setObjectName(f"resultLineEdit{i}")
                resultLineEdit.setText(self.tempResult[i][2])
                self.verticalLayout_4.addWidget(resultLineEdit)

                self.scrollArea.setWidget(
                    self.scrollAreaWidgetContents)  # --------

                self.completer = QCompleter(strList)
                self.completer.setCaseSensitivity(Qt.CaseInsensitive)
                resultLineEdit.setCompleter(self.completer)
                resultLineEdit.textChanged.connect(
                    lambda text, index=i: self.capture(text, index))
                resultLineEdit.focusInEvent = lambda event, index=i: self.on_focus_in(
                    event, index)
            # redefining of focusInEvent of qlineedit, basically copying/replacing of method
            # method- on_focus_in in my class- UI_Bindings is getting copied to method- focusInEvent of qlineedit
            # just like in zoom method in my class with wheelEvent
                print(i)
                self.lineEditList.append((resultLineEdit, i))

    def capture(self, text, i):
        print(text, i)
        self.tempResult[i][2] = text  # self.lineEditList[i][0].text()

    def on_focus_in(self, event, index):
        # print(self.lineEditList[index].text())

        self.details(str(self.DetailscheckBox.checkState())
                     == 'CheckState.Checked', index)

    def userList(self, selected, count):

        print('called', count)
        if count == 0:
            userList = os.listdir(f'{os.getcwd()}/Dataset/')
            userList.append('create user')
            # print(userList)
            self.userComboBox.addItems(userList)
            count = 1
        self.userSelected = self.userComboBox.currentText()
        if self.userSelected == 'create user':
            self.newUser = CreateUser()
            self.newUser.show()
            # self.userComboBox.setCurrentText()

    def export(self):
        # for i in range(len(self.lineEditList)):
        #     self.tempResult[self.lineEditList[i][1]
        #                     ][2] = self.lineEditList[i][0].text()

        self.saveFileLocation = QFileDialog.getSaveFileName(
            None, '', '', '*.docx')
        print(self.saveFileLocation[0])
        self.docx(self.saveFileLocation[0])
        self.crop_label(self.userSelected)

    def modelList(self, count):
        # C:/Users/UserName/.EasyOCR/model
        if count == 0:
            modelList = os.listdir('C:/Users/ANKIT/.EasyOCR/model')
            modelList.append('standard')

            self.comboBox.addItems(modelList)
            self.comboBox.setCurrentText('standard')
            count = 1
        self.modelSelected = (self.comboBox.currentText().split(sep='.'))[0]

    def newUserDS(self, userName):
        print('cled newUserDs')
        os.mkdir(f'{os.getcwd()}/Dataset/{userName}')
        self.userList(0, 0)

    def details(self, state, i=-1):

        # if str(self.DetailscheckBox.checkState()) == 'CheckState.Checked':
        if state:

            self.detailedImg(i, self.fileName[0])
            self.showImg(
                f'{os.getcwd()}/temp/bound.jpg')
        else:
            self.showImg(self.fileName[0])

    def update(self):
        # mdownload new model to the directory and update modelList(0)
        pass

    def rangeSelect():
        pass


class CreateUser(QWidget, UI_Bindings):
    def __init__(self):
        super().__init__()

        self.layout = QHBoxLayout()
        self.nameInput = QLineEdit()
        self.addBtn = QPushButton()
        self.nameInput.setPlaceholderText('Name')
        self.addBtn.setText('Add')
        self.layout.addWidget(self.nameInput)
        self.layout.addWidget(self.addBtn)
        self.setLayout(self.layout)
        self.addBtn.clicked.connect(self.returnName)

    def returnName(self):
        print(self.nameInput.text())
        self.newUserDS(self.nameInput.text())
        print('cl')
        self.close()


if __name__ == "__main__":
    import sys

    app = QApplication(sys.argv)
    MainWindow = QMainWindow()
    ui = UI_Bindings(MainWindow)
    qdarktheme.setup_theme("auto")

    MainWindow.show()
    sys.exit(app.exec())
