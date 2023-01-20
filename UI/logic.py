from ui_simple import *


class ui_bindings(Ui_MainWindow):
    def __init__(self, window):
        # super.__init__()
        self.setupUi(window)
        self.OpenImageBtn.clicked.connect(self.openImgBtn)

    def openImgBtn(self):
        self.fileName = QFileDialog.getOpenFileName(
            None, '', "", "Images (*.png *.xpm *.jpg)")
        print(self.fileName[0])

    def showImg():
        pass


if __name__ == "__main__":
    import sys

    app = QApplication(sys.argv)
    MainWindow = QMainWindow()
    ui = ui_bindings(MainWindow)
    # ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec())
