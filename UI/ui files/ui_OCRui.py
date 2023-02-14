# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'OCRui.ui'
##
## Created by: Qt User Interface Compiler version 6.4.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QCheckBox, QComboBox, QFrame,
    QGridLayout, QLabel, QMainWindow, QPlainTextEdit,
    QPushButton, QScrollBar, QSizePolicy, QSpacerItem,
    QSplitter, QStatusBar, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1138, 627)
        MainWindow.setStyleSheet(u"background:rgb(10, 15, 32)")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.gridLayout_4 = QGridLayout(self.centralwidget)
        self.gridLayout_4.setObjectName(u"gridLayout_4")
        self.settingsframe = QFrame(self.centralwidget)
        self.settingsframe.setObjectName(u"settingsframe")
        self.settingsframe.setStyleSheet(u"background-color:rgb(57, 50, 62);\n"
"border-radius:5px;\n"
"border-style:solid;\n"
"border-width:1px;\n"
"border-color:none")
        self.settingsframe.setFrameShape(QFrame.StyledPanel)
        self.settingsframe.setFrameShadow(QFrame.Raised)
        self.gridLayout_3 = QGridLayout(self.settingsframe)
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.pushButton_3 = QPushButton(self.settingsframe)
        self.pushButton_3.setObjectName(u"pushButton_3")
        self.pushButton_3.setStyleSheet(u"color: rgb(255, 255, 255);\n"
"font: 500 9pt \"Overpass\";\n"
"")

        self.gridLayout_3.addWidget(self.pushButton_3, 0, 0, 1, 1)

        self.label = QLabel(self.settingsframe)
        self.label.setObjectName(u"label")
        self.label.setStyleSheet(u"color: rgb(255, 255, 255);\n"
"font: 500 9pt \"Overpass\";\n"
"border-style:none;")

        self.gridLayout_3.addWidget(self.label, 1, 0, 1, 1)

        self.comboBox = QComboBox(self.settingsframe)
        self.comboBox.setObjectName(u"comboBox")
        self.comboBox.setStyleSheet(u"background-color: rgb(255, 255, 255);")

        self.gridLayout_3.addWidget(self.comboBox, 2, 0, 1, 1)

        self.checkBox_3 = QCheckBox(self.settingsframe)
        self.checkBox_3.setObjectName(u"checkBox_3")
        self.checkBox_3.setStyleSheet(u"color: rgb(255, 255, 255);\n"
"font: 500 9pt \"Overpass\";\n"
"border-style:none;")

        self.gridLayout_3.addWidget(self.checkBox_3, 3, 0, 1, 1)

        self.verticalSpacer_2 = QSpacerItem(20, 405, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.gridLayout_3.addItem(self.verticalSpacer_2, 4, 0, 1, 1)

        self.label_3 = QLabel(self.settingsframe)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setStyleSheet(u"color: rgb(255, 255, 255);\n"
"font: 500 9pt \"Overpass\";\n"
"border-style:none;")

        self.gridLayout_3.addWidget(self.label_3, 5, 0, 1, 1)

        self.checkBox_2 = QCheckBox(self.settingsframe)
        self.checkBox_2.setObjectName(u"checkBox_2")
        self.checkBox_2.setStyleSheet(u"color: rgb(255, 255, 255);\n"
"font: 500 9pt \"Overpass\";\n"
"border-style:none;")

        self.gridLayout_3.addWidget(self.checkBox_2, 6, 0, 1, 1)

        self.checkBox = QCheckBox(self.settingsframe)
        self.checkBox.setObjectName(u"checkBox")
        self.checkBox.setStyleSheet(u"color: rgb(255, 255, 255);\n"
"font: 500 9pt \"Overpass\";\n"
"border-style:none;")

        self.gridLayout_3.addWidget(self.checkBox, 7, 0, 1, 1)


        self.gridLayout_4.addWidget(self.settingsframe, 0, 0, 2, 1)

        self.splitter_3 = QSplitter(self.centralwidget)
        self.splitter_3.setObjectName(u"splitter_3")
        self.splitter_3.setOrientation(Qt.Horizontal)
        self.imageframe = QFrame(self.splitter_3)
        self.imageframe.setObjectName(u"imageframe")
        self.imageframe.setStyleSheet(u"background-color:rgb(57, 50, 62);\n"
"border-radius:5px;\n"
"border-style:solid;\n"
"border-width:1px;\n"
"border-color:none;\n"
"")
        self.imageframe.setFrameShape(QFrame.StyledPanel)
        self.imageframe.setFrameShadow(QFrame.Raised)
        self.gridLayout = QGridLayout(self.imageframe)
        self.gridLayout.setObjectName(u"gridLayout")
        self.label_2 = QLabel(self.imageframe)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setStyleSheet(u"font: 500 9pt \"Overpass\";\n"
"color: rgb(255, 255, 255);")
        self.label_2.setPixmap(QPixmap(u"../test case.jpg"))

        self.gridLayout.addWidget(self.label_2, 0, 0, 1, 1)

        self.splitter_3.addWidget(self.imageframe)
        self.resultTextframe = QFrame(self.splitter_3)
        self.resultTextframe.setObjectName(u"resultTextframe")
        self.resultTextframe.setStyleSheet(u"background-color:rgb(57, 50, 62);\n"
"border-radius:5px;\n"
"border-style:solid;\n"
"border-width:1px;\n"
"border-color:none;\n"
"")
        self.resultTextframe.setFrameShape(QFrame.StyledPanel)
        self.resultTextframe.setFrameShadow(QFrame.Raised)
        self.gridLayout_2 = QGridLayout(self.resultTextframe)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.plainTextEdit = QPlainTextEdit(self.resultTextframe)
        self.plainTextEdit.setObjectName(u"plainTextEdit")
        self.plainTextEdit.setStyleSheet(u"font: 500 9pt \"Overpass\";\n"
"color: rgb(255, 255, 255);\n"
"border-style:none;")

        self.gridLayout_2.addWidget(self.plainTextEdit, 0, 0, 1, 1)

        self.splitter_2 = QSplitter(self.resultTextframe)
        self.splitter_2.setObjectName(u"splitter_2")
        self.splitter_2.setOrientation(Qt.Vertical)
        self.verticalScrollBar = QScrollBar(self.splitter_2)
        self.verticalScrollBar.setObjectName(u"verticalScrollBar")
        self.verticalScrollBar.setOrientation(Qt.Vertical)
        self.splitter_2.addWidget(self.verticalScrollBar)

        self.gridLayout_2.addWidget(self.splitter_2, 0, 1, 1, 1)

        self.splitter = QSplitter(self.resultTextframe)
        self.splitter.setObjectName(u"splitter")
        self.splitter.setOrientation(Qt.Horizontal)
        self.horizontalScrollBar = QScrollBar(self.splitter)
        self.horizontalScrollBar.setObjectName(u"horizontalScrollBar")
        self.horizontalScrollBar.setOrientation(Qt.Horizontal)
        self.splitter.addWidget(self.horizontalScrollBar)

        self.gridLayout_2.addWidget(self.splitter, 1, 0, 1, 2)

        self.splitter_3.addWidget(self.resultTextframe)

        self.gridLayout_4.addWidget(self.splitter_3, 0, 1, 1, 3)

        self.horizontalSpacer_3 = QSpacerItem(838, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout_4.addItem(self.horizontalSpacer_3, 1, 2, 1, 1)

        self.pushButton_2 = QPushButton(self.centralwidget)
        self.pushButton_2.setObjectName(u"pushButton_2")
        self.pushButton_2.setStyleSheet(u"font: 500 9pt \"Overpass\";\n"
"color: rgb(255, 255, 255);\n"
"background:rgb(140, 141, 208);\n"
"\n"
"")

        self.gridLayout_4.addWidget(self.pushButton_2, 1, 3, 1, 1)

        self.pushButton = QPushButton(self.centralwidget)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setStyleSheet(u"font: 500 9pt \"Overpass\";\n"
"color: rgb(255, 255, 255);\n"
"background:rgb(140, 141, 208);\n"
"\n"
"")

        self.gridLayout_4.addWidget(self.pushButton, 1, 1, 1, 1)

        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.pushButton_3.setText(QCoreApplication.translate("MainWindow", u"Open Image", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"Model", None))
        self.checkBox_3.setText(QCoreApplication.translate("MainWindow", u"Details", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"Pre-Processing", None))
        self.checkBox_2.setText(QCoreApplication.translate("MainWindow", u"Thresholding", None))
        self.checkBox.setText(QCoreApplication.translate("MainWindow", u"Skewness", None))
        self.label_2.setText("")
        self.plainTextEdit.setPlainText(QCoreApplication.translate("MainWindow", u"Result_,_Text_,_", None))
        self.pushButton_2.setText(QCoreApplication.translate("MainWindow", u"Export", None))
        self.pushButton.setText(QCoreApplication.translate("MainWindow", u"OCR", None))
    # retranslateUi

