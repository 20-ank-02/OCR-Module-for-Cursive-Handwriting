# -*- coding: utf-8 -*-

################################################################################
# Form generated from reading UI file 'simple.ui'
##
# Created by: Qt User Interface Compiler version 6.4.2
##
# WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
                            QMetaObject, QObject, QPoint, QRect,
                            QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
                           QFont, QFontDatabase, QGradient, QIcon,
                           QImage, QKeySequence, QLinearGradient, QPainter,
                           QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QCheckBox, QComboBox, QGraphicsView,
                               QGridLayout, QHBoxLayout, QLabel, QMainWindow,
                               QMenuBar, QPlainTextEdit, QPushButton, QSizePolicy,
                               QSpacerItem, QSplitter, QStatusBar, QVBoxLayout,
                               QWidget, QGraphicsScene)


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(859, 489)
        MainWindow.setStyleSheet(u"background-color: rgb(10, 15, 32);")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.gridLayout = QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName(u"gridLayout")
        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.verticalLayout_3 = QVBoxLayout()
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.OpenImageBtn = QPushButton(self.centralwidget)
        self.OpenImageBtn.setObjectName(u"OpenImageBtn")
        self.OpenImageBtn.setStyleSheet(u"color:rgb(255, 255, 255);\n"
                                        "background-color: rgb(140, 141, 208);\n"
                                        "font: 700 9pt \"Overpass\";")

        self.verticalLayout_3.addWidget(self.OpenImageBtn)

        self.verticalSpacer_2 = QSpacerItem(
            20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_3.addItem(self.verticalSpacer_2)

        self.label = QLabel(self.centralwidget)
        self.label.setObjectName(u"label")
        self.label.setStyleSheet(u"color: rgb(255, 255, 255);\n"
                                 "font: 700 9pt \"Overpass\";")

        self.verticalLayout_3.addWidget(self.label)

        self.comboBox = QComboBox(self.centralwidget)
        self.comboBox.setObjectName(u"comboBox")
        self.comboBox.setStyleSheet(u"background-color: rgb(255, 255, 255);")

        self.verticalLayout_3.addWidget(self.comboBox)

        self.DetailscheckBox = QCheckBox(self.centralwidget)
        self.DetailscheckBox.setObjectName(u"DetailscheckBox")
        self.DetailscheckBox.setStyleSheet(u"color: rgb(255, 255, 255);\n"
                                           "font: 700 9pt \"Overpass\";")

        self.verticalLayout_3.addWidget(self.DetailscheckBox)

        self.verticalSpacer = QSpacerItem(
            20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_3.addItem(self.verticalSpacer)

        self.horizontalLayout_3.addLayout(self.verticalLayout_3)

        self.splitter = QSplitter(self.centralwidget)
        self.splitter.setObjectName(u"splitter")
        self.splitter.setOrientation(Qt.Horizontal)
        self.verticalLayoutWidget = QWidget(self.splitter)
        self.verticalLayoutWidget.setObjectName(u"verticalLayoutWidget")
        self.verticalLayout = QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)

        self.ImageLabel = QGraphicsView(self.verticalLayoutWidget)

        self.ImageLabel.setObjectName(u"ImageLabel")
        self.ImageLabel.setStyleSheet(u"background-color:rgb(57, 50, 62);\n"
                                      "border-radius:5px;\n"
                                      "border-style:solid;\n"
                                      "border-width:1px;\n"
                                      "border-color:white;")

        self.verticalLayout.addWidget(self.ImageLabel)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalSpacer_2 = QSpacerItem(
            40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer_2)

        self.OCRBtn = QPushButton(self.verticalLayoutWidget)
        self.OCRBtn.setObjectName(u"OCRBtn")
        self.OCRBtn.setStyleSheet(u"color:rgb(255, 255, 255);\n"
                                  "background-color: rgb(140, 141, 208);\n"
                                  "font: 700 9pt \"Overpass\";")

        self.horizontalLayout_2.addWidget(self.OCRBtn)

        self.verticalLayout.addLayout(self.horizontalLayout_2)

        self.splitter.addWidget(self.verticalLayoutWidget)
        self.verticalLayoutWidget_2 = QWidget(self.splitter)
        self.verticalLayoutWidget_2.setObjectName(u"verticalLayoutWidget_2")
        self.verticalLayout_2 = QVBoxLayout(self.verticalLayoutWidget_2)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.ResultText = QPlainTextEdit(self.verticalLayoutWidget_2)
        self.ResultText.setObjectName(u"ResultText")
        self.ResultText.setStyleSheet(u"background-color:rgb(57, 50, 62);\n"
                                      "border-radius:5px;\n"
                                      "border-style:solid;\n"
                                      "border-width:1px;\n"
                                      "border-color:none;\n"
                                      "color:rgb(255, 255, 255);\n"
                                      "font: 500 9pt \"Overpass\";")

        self.verticalLayout_2.addWidget(self.ResultText)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalSpacer = QSpacerItem(
            40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer)

        self.ExportBtn = QPushButton(self.verticalLayoutWidget_2)
        self.ExportBtn.setObjectName(u"ExportBtn")
        self.ExportBtn.setStyleSheet(u"color:rgb(255, 255, 255);\n"
                                     "background-color: rgb(140, 141, 208);\n"
                                     "font: 700 9pt \"Overpass\";")

        self.horizontalLayout.addWidget(self.ExportBtn)

        self.verticalLayout_2.addLayout(self.horizontalLayout)

        self.splitter.addWidget(self.verticalLayoutWidget_2)

        self.horizontalLayout_3.addWidget(self.splitter)

        self.gridLayout.addLayout(self.horizontalLayout_3, 0, 0, 1, 1)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 859, 25))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate(
            "MainWindow", u"MainWindow", None))
        self.OpenImageBtn.setText(QCoreApplication.translate(
            "MainWindow", u"Open Image", None))
        self.label.setText(QCoreApplication.translate(
            "MainWindow", u"Model", None))
        self.DetailscheckBox.setText(
            QCoreApplication.translate("MainWindow", u"Details", None))
        self.OCRBtn.setText(QCoreApplication.translate(
            "MainWindow", u"OCR", None))
        self.ExportBtn.setText(QCoreApplication.translate(
            "MainWindow", u"Export", None))
    # retranslateUi
