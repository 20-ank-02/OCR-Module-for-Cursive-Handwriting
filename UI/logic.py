from ui_simpleWhite import *
from PySide6.QtWidgets import QFileDialog, QGraphicsScene, QLineEdit
from PySide6.QtCore import QRectF
from OCR_class import *
import qdarktheme
from PySide6.QtCore import QEvent


class UI_Bindings(Ui_MainWindow, OCR):
    newUserName = 'called'

    def __init__(self, window):
        # super.__init__()
        self.setupUi(window)
        window.setWindowTitle('R.A.M.P')
        self.userList(0)
        self.modelList(0)
        self.theme(0)
        self.userComboBox.activated.connect(self.userList)
        self.comboBox.activated.connect(self.modelList)
        self.DetailscheckBox.stateChanged.connect(self.details)
        self.OpenImageBtn.clicked.connect(self.openImgBtn)
        self.ImageLabel.wheelEvent = self.zoom
        self.ExportBtn.clicked.connect(self.export)
        self.OCRBtn.clicked.connect(self.imgText)

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

    def imgText(self):
        # self.statusLabel.setText('model error')

        self.imgRead(
            self.fileName[0], self.modelSelected)
        self.ResultText.clear()
        self.ResultText.appendPlainText(self.tempResult)
        # self.statusLabel.setText('done')
        # for i in range(len(text)): for list of strings
        #     self.ResultText.appendPlainText(text[i])

    def userList(self, count):
        if count == 0:
            userList = os.listdir(f'{os.getcwd()}/Dataset/')
            userList.append('create user')
            print(userList)
            self.userComboBox.addItems(userList)
            count = 1
        self.userSelected = self.userComboBox.currentText()
        if self.userSelected == 'create user':
            self.newUser = CreateUser()
            self.newUser.show()
            # self.userComboBox.setCurrentText()

    def export(self):
        self.tempResult = self.ResultText.toPlainText()
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

        os.mkdir(f'{os.getcwd()}/Dataset/{userName}')
        self.userList(0)

    def details(self):
        if str(self.DetailscheckBox.checkState()) == 'CheckState.Checked':
            self.detailedImg()
            self.showImg(
                f'{os.getcwd()}/temp/bound.jpg')
        else:
            self.showImg(self.fileName[0])

    def update(self):
        # mdownload new model to the directory and update modelList(0)
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
        self.newUserDS(self.nameInput.text())
        self.close()


if __name__ == "__main__":
    import sys

    app = QApplication(sys.argv)
    MainWindow = QMainWindow()
    ui = UI_Bindings(MainWindow)
    qdarktheme.setup_theme("auto")
    # ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec())
