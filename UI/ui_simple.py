# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'simpleCPCUGG.ui'
##
## Created by: Qt User Interface Compiler version 6.3.1
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
from PySide6.QtWidgets import (QApplication, QCheckBox, QComboBox, QFormLayout,
    QGraphicsView, QHBoxLayout, QLabel, QLineEdit,
    QMainWindow, QPushButton, QScrollArea, QSizePolicy,
    QSpacerItem, QSplitter, QStatusBar, QVBoxLayout,
    QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(859, 489)
        MainWindow.setStyleSheet(u"")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.formLayout = QFormLayout(self.centralwidget)
        self.formLayout.setObjectName(u"formLayout")
        self.verticalLayout_3 = QVBoxLayout()
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.OpenImageBtn = QPushButton(self.centralwidget)
        self.OpenImageBtn.setObjectName(u"OpenImageBtn")
        self.OpenImageBtn.setStyleSheet(u"")

        self.verticalLayout_3.addWidget(self.OpenImageBtn)

        self.verticalSpacer_4 = QSpacerItem(20, 13, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_3.addItem(self.verticalSpacer_4)

        self.label_3 = QLabel(self.centralwidget)
        self.label_3.setObjectName(u"label_3")

        self.verticalLayout_3.addWidget(self.label_3)

        self.userComboBox = QComboBox(self.centralwidget)
        self.userComboBox.setObjectName(u"userComboBox")

        self.verticalLayout_3.addWidget(self.userComboBox)

        self.verticalSpacer_2 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_3.addItem(self.verticalSpacer_2)

        self.label = QLabel(self.centralwidget)
        self.label.setObjectName(u"label")
        self.label.setStyleSheet(u"")

        self.verticalLayout_3.addWidget(self.label)

        self.comboBox = QComboBox(self.centralwidget)
        self.comboBox.setObjectName(u"comboBox")
        self.comboBox.setStyleSheet(u"")

        self.verticalLayout_3.addWidget(self.comboBox)

        self.DetailscheckBox = QCheckBox(self.centralwidget)
        self.DetailscheckBox.setObjectName(u"DetailscheckBox")
        self.DetailscheckBox.setStyleSheet(u"")

        self.verticalLayout_3.addWidget(self.DetailscheckBox)

        self.verticalSpacer = QSpacerItem(20, 13, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_3.addItem(self.verticalSpacer)

        self.rangeLow = QLineEdit(self.centralwidget)
        self.rangeLow.setObjectName(u"rangeLow")
        self.rangeLow.setFocusPolicy(Qt.ClickFocus)

        self.verticalLayout_3.addWidget(self.rangeLow)

        self.rangeHigh = QLineEdit(self.centralwidget)
        self.rangeHigh.setObjectName(u"rangeHigh")
        self.rangeHigh.setFocusPolicy(Qt.ClickFocus)

        self.verticalLayout_3.addWidget(self.rangeHigh)

        self.verticalSpacer_3 = QSpacerItem(20, 18, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_3.addItem(self.verticalSpacer_3)

        self.label_2 = QLabel(self.centralwidget)
        self.label_2.setObjectName(u"label_2")

        self.verticalLayout_3.addWidget(self.label_2)

        self.themeBox = QComboBox(self.centralwidget)
        self.themeBox.setObjectName(u"themeBox")

        self.verticalLayout_3.addWidget(self.themeBox)


        self.formLayout.setLayout(0, QFormLayout.LabelRole, self.verticalLayout_3)

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
        self.ImageLabel.setStyleSheet(u"")

        self.verticalLayout.addWidget(self.ImageLabel)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer_2)

        self.OCRBtn = QPushButton(self.verticalLayoutWidget)
        self.OCRBtn.setObjectName(u"OCRBtn")
        self.OCRBtn.setStyleSheet(u"")

        self.horizontalLayout_2.addWidget(self.OCRBtn)


        self.verticalLayout.addLayout(self.horizontalLayout_2)

        self.splitter.addWidget(self.verticalLayoutWidget)
        self.verticalLayoutWidget_2 = QWidget(self.splitter)
        self.verticalLayoutWidget_2.setObjectName(u"verticalLayoutWidget_2")
        self.verticalLayout_2 = QVBoxLayout(self.verticalLayoutWidget_2)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.scrollArea = QScrollArea(self.verticalLayoutWidget_2)
        self.scrollArea.setObjectName(u"scrollArea")
        self.scrollArea.setWidgetResizable(True)
        self.scrollAreaWidgetContents = QWidget()
        self.scrollAreaWidgetContents.setObjectName(u"scrollAreaWidgetContents")
        self.scrollAreaWidgetContents.setGeometry(QRect(0, 0, 223, 414))
        self.verticalLayout_4 = QVBoxLayout(self.scrollAreaWidgetContents)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.scrollArea.setWidget(self.scrollAreaWidgetContents)

        self.verticalLayout_2.addWidget(self.scrollArea)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer)

        self.ExportBtn = QPushButton(self.verticalLayoutWidget_2)
        self.ExportBtn.setObjectName(u"ExportBtn")
        self.ExportBtn.setStyleSheet(u"")

        self.horizontalLayout.addWidget(self.ExportBtn)


        self.verticalLayout_2.addLayout(self.horizontalLayout)

        self.splitter.addWidget(self.verticalLayoutWidget_2)

        self.formLayout.setWidget(0, QFormLayout.FieldRole, self.splitter)

        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.OpenImageBtn.setText(QCoreApplication.translate("MainWindow", u"Open Image", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"User", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"Model", None))
        self.DetailscheckBox.setText(QCoreApplication.translate("MainWindow", u"Bound Box", None))
        self.rangeLow.setPlaceholderText(QCoreApplication.translate("MainWindow", u"rangeLow", None))
        self.rangeHigh.setPlaceholderText(QCoreApplication.translate("MainWindow", u"rangeHigh", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"Theme", None))
        self.splitter.setStyleSheet("")
        self.verticalLayoutWidget.setStyleSheet("")
        self.OCRBtn.setText(QCoreApplication.translate("MainWindow", u"OCR", None))
        self.verticalLayoutWidget_2.setStyleSheet("")
        self.ExportBtn.setText(QCoreApplication.translate("MainWindow", u"Export", None))
    # retranslateUi

