# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'ImageEncrypter.ui'
##
## Created by: Qt User Interface Compiler version 6.6.2
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
from PySide6.QtWidgets import (QApplication, QFrame, QGridLayout, QGroupBox,
    QHBoxLayout, QLabel, QLineEdit, QMainWindow,
    QPushButton, QSizePolicy, QStatusBar, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(628, 512)
        MainWindow.setStyleSheet(u"")
        MainWindow.setUnifiedTitleAndToolBarOnMac(False)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.frame = QFrame(self.centralwidget)
        self.frame.setObjectName(u"frame")
        self.frame.setGeometry(QRect(-1, -1, 631, 511))
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.groupBox = QGroupBox(self.frame)
        self.groupBox.setObjectName(u"groupBox")
        self.groupBox.setGeometry(QRect(10, 100, 300, 300))
        self.gridLayout = QGridLayout(self.groupBox)
        self.gridLayout.setObjectName(u"gridLayout")
        self.loadImageLabel = QLabel(self.groupBox)
        self.loadImageLabel.setObjectName(u"loadImageLabel")

        self.gridLayout.addWidget(self.loadImageLabel, 0, 0, 1, 1)

        self.groupBox_2 = QGroupBox(self.frame)
        self.groupBox_2.setObjectName(u"groupBox_2")
        self.groupBox_2.setGeometry(QRect(320, 100, 300, 300))
        self.gridLayout_2 = QGridLayout(self.groupBox_2)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.outputImageLabel = QLabel(self.groupBox_2)
        self.outputImageLabel.setObjectName(u"outputImageLabel")

        self.gridLayout_2.addWidget(self.outputImageLabel, 0, 0, 1, 1)

        self.layoutWidget = QWidget(self.frame)
        self.layoutWidget.setObjectName(u"layoutWidget")
        self.layoutWidget.setGeometry(QRect(10, 70, 301, 27))
        self.horizontalLayout = QHBoxLayout(self.layoutWidget)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.loadedImageNameLabel = QLabel(self.layoutWidget)
        self.loadedImageNameLabel.setObjectName(u"loadedImageNameLabel")
        self.loadedImageNameLabel.setStyleSheet(u"")

        self.horizontalLayout.addWidget(self.loadedImageNameLabel)

        self.loadImageButton = QPushButton(self.layoutWidget)
        self.loadImageButton.setObjectName(u"loadImageButton")
        self.loadImageButton.setStyleSheet(u"")

        self.horizontalLayout.addWidget(self.loadImageButton)

        self.layoutWidget1 = QWidget(self.frame)
        self.layoutWidget1.setObjectName(u"layoutWidget1")
        self.layoutWidget1.setGeometry(QRect(320, 70, 301, 27))
        self.horizontalLayout_2 = QHBoxLayout(self.layoutWidget1)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.outputImageNameLabel = QLabel(self.layoutWidget1)
        self.outputImageNameLabel.setObjectName(u"outputImageNameLabel")
        self.outputImageNameLabel.setStyleSheet(u"")

        self.horizontalLayout_2.addWidget(self.outputImageNameLabel)

        self.saveImageButton = QPushButton(self.layoutWidget1)
        self.saveImageButton.setObjectName(u"saveImageButton")
        self.saveImageButton.setStyleSheet(u"")

        self.horizontalLayout_2.addWidget(self.saveImageButton)

        self.layoutWidget2 = QWidget(self.frame)
        self.layoutWidget2.setObjectName(u"layoutWidget2")
        self.layoutWidget2.setGeometry(QRect(10, 430, 601, 27))
        self.horizontalLayout_3 = QHBoxLayout(self.layoutWidget2)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.keyLineEdit = QLineEdit(self.layoutWidget2)
        self.keyLineEdit.setObjectName(u"keyLineEdit")

        self.horizontalLayout_3.addWidget(self.keyLineEdit)

        self.encryptButton = QPushButton(self.layoutWidget2)
        self.encryptButton.setObjectName(u"encryptButton")
        self.encryptButton.setStyleSheet(u"")

        self.horizontalLayout_3.addWidget(self.encryptButton)

        self.decryptButton = QPushButton(self.layoutWidget2)
        self.decryptButton.setObjectName(u"decryptButton")
        self.decryptButton.setStyleSheet(u"")

        self.horizontalLayout_3.addWidget(self.decryptButton)

        self.label = QLabel(self.frame)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(160, 10, 311, 51))
        font = QFont()
        font.setPointSize(28)
        font.setBold(True)
        self.label.setFont(font)
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"Image Encrypter", None))
        self.frame.setStyleSheet("")
        self.groupBox.setTitle(QCoreApplication.translate("MainWindow", u"Image", None))
        self.loadImageLabel.setText("")
        self.groupBox_2.setTitle(QCoreApplication.translate("MainWindow", u"Output", None))
        self.outputImageLabel.setText("")
        self.loadedImageNameLabel.setText("")
        self.loadImageButton.setText(QCoreApplication.translate("MainWindow", u"Load Image", None))
        self.outputImageNameLabel.setText("")
        self.saveImageButton.setText(QCoreApplication.translate("MainWindow", u"Save Image", None))
        self.keyLineEdit.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Enter Encryption Key", None))
        self.encryptButton.setText(QCoreApplication.translate("MainWindow", u"Encrypt", None))
        self.decryptButton.setText(QCoreApplication.translate("MainWindow", u"Decrypt", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"Content Security", None))
    # retranslateUi

