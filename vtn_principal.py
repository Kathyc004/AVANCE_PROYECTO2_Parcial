# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'vtn_principal.ui'
##
## Created by: Qt User Interface Compiler version 6.5.1
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
from PySide6.QtWidgets import (QApplication, QLabel, QMainWindow, QMenuBar,
    QPushButton, QSizePolicy, QStatusBar, QTextEdit,
    QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(800, 294)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.txt_nombre = QTextEdit(self.centralwidget)
        self.txt_nombre.setObjectName(u"txt_nombre")
        self.txt_nombre.setGeometry(QRect(320, 40, 161, 31))
        self.txt_Apellido = QTextEdit(self.centralwidget)
        self.txt_Apellido.setObjectName(u"txt_Apellido")
        self.txt_Apellido.setGeometry(QRect(320, 90, 161, 31))
        self.lbl_Nombre = QLabel(self.centralwidget)
        self.lbl_Nombre.setObjectName(u"lbl_Nombre")
        self.lbl_Nombre.setGeometry(QRect(210, 50, 47, 13))
        self.lbl_Apellido = QLabel(self.centralwidget)
        self.lbl_Apellido.setObjectName(u"lbl_Apellido")
        self.lbl_Apellido.setGeometry(QRect(210, 100, 47, 13))
        self.btn_grabar = QPushButton(self.centralwidget)
        self.btn_grabar.setObjectName(u"btn_grabar")
        self.btn_grabar.setGeometry(QRect(370, 150, 75, 23))
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 800, 21))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.lbl_Nombre.setText(QCoreApplication.translate("MainWindow", u"Nombre:", None))
        self.lbl_Apellido.setText(QCoreApplication.translate("MainWindow", u"Apellido", None))
        self.btn_grabar.setText(QCoreApplication.translate("MainWindow", u"GRABAR", None))
    # retranslateUi
