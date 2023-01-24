from ui_simple import *
from PySide6.QtWidgets import QFileDialog, QGraphicsScene
from PySide6.QtCore import QRectF
from OCR_class import *


class ui_bindings(Ui_MainWindow):
    def __init__(self, window):
        # super.__init__()
        self.setupUi(window)
        window.setWindowTitle('Techgium')
        self.modelList(0)
        self.comboBox.activated.connect(self.modelList)
        self.DetailscheckBox.stateChanged.connect(self.details)
        self.OpenImageBtn.clicked.connect(self.openImgBtn)
        self.ImageLabel.wheelEvent = self.zoom
        self.ExportBtn.clicked.connect(self.export)
        self.OCRBtn.clicked.connect(self.resultText)

        # self.ImageLabel.resizeEvent = self.doSomething

    def openImgBtn(self):
        self.fileName = QFileDialog.getOpenFileName(
            None, '', "", "Images (*.png *.xpm *.jpg)")
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
            print(event.angleDelta())
            self.ImageLabel.scale(2, 2)

        if event.angleDelta() == QPoint(0, -120):
            print(event.angleDelta())
            self.ImageLabel.scale(0.5, 0.5)

    def resultText(self):
        self.ResultText.setPlainText('Hello world')

    def export(self):
        print(self.ResultText.toPlainText())
        self.saveFileLocation = QFileDialog.getSaveFileName(
            None, '', '', '*.docx')
        print(self.saveFileLocation[0])

    def modelList(self, count):
        # C:/Users/UserName/.EasyOCR/model
        if count == 0:
            modelList = os.listdir('C:/Users/ANKIT/.EasyOCR/model')
            self.comboBox.addItems(modelList)
            count = 1
        modelSelected = self.comboBox.currentText()
        print(modelSelected)

    def details(self):
        print(self.DetailscheckBox.checkState())

    def update(self):
        # mdownload new model to the directory and update modelList(0)
        pass


if __name__ == "__main__":
    import sys

    app = QApplication(sys.argv)
    MainWindow = QMainWindow()
    ui = ui_bindings(MainWindow)
    # ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec())
