# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'converter.ui'
##
## Created by: Qt User Interface Compiler version 6.6.1
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
from PySide6.QtWidgets import (QApplication, QComboBox, QLabel, QLineEdit,
    QMainWindow, QMenuBar, QSizePolicy, QStatusBar,
    QWidget)

class Ui_Converter(object):
    def setupUi(self, Converter):
        if not Converter.objectName():
            Converter.setObjectName(u"Converter")
        Converter.resize(598, 237)
        self.centralwidget = QWidget(Converter)
        self.centralwidget.setObjectName(u"centralwidget")
        self.label = QLabel(self.centralwidget)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(20, 10, 311, 31))
        font = QFont()
        font.setPointSize(15)
        self.label.setFont(font)
        self.Measurments = QComboBox(self.centralwidget)
        self.Measurments.addItem("")
        self.Measurments.addItem("")
        self.Measurments.addItem("")
        self.Measurments.addItem("")
        self.Measurments.addItem("")
        self.Measurments.addItem("")
        self.Measurments.addItem("")
        self.Measurments.addItem("")
        self.Measurments.setObjectName(u"Measurments")
        self.Measurments.setGeometry(QRect(20, 50, 261, 41))
        self.Measurments.setFont(font)
        self.Select2 = QComboBox(self.centralwidget)
        self.Select2.setObjectName(u"Select2")
        self.Select2.setGeometry(QRect(440, 120, 121, 41))
        self.Select1 = QComboBox(self.centralwidget)
        self.Select1.setObjectName(u"Select1")
        self.Select1.setGeometry(QRect(140, 120, 121, 41))
        self.Number2 = QLineEdit(self.centralwidget)
        self.Number2.setObjectName(u"Number2")
        self.Number2.setGeometry(QRect(322, 121, 111, 31))
        self.Number1 = QLineEdit(self.centralwidget)
        self.Number1.setObjectName(u"Number1")
        self.Number1.setGeometry(QRect(20, 120, 111, 31))
        self.Number1.setAutoFillBackground(False)
        self.label_2 = QLabel(self.centralwidget)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(280, 120, 31, 21))
        font1 = QFont()
        font1.setPointSize(20)
        self.label_2.setFont(font1)
        Converter.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(Converter)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 598, 26))
        Converter.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(Converter)
        self.statusbar.setObjectName(u"statusbar")
        Converter.setStatusBar(self.statusbar)

        self.retranslateUi(Converter)

        QMetaObject.connectSlotsByName(Converter)
    # setupUi

    def retranslateUi(self, Converter):
        Converter.setWindowTitle(QCoreApplication.translate("Converter", u"MainWindow", None))
        self.label.setText(QCoreApplication.translate("Converter", u"\u0415\u0434\u0438\u043d\u0438\u0446\u044b \u0438\u0437\u043c\u0435\u0440\u0435\u043d\u0438\u044f", None))
        self.Measurments.setItemText(0, QCoreApplication.translate("Converter", u"\u0414\u043b\u0438\u043d\u0430", None))
        self.Measurments.setItemText(1, QCoreApplication.translate("Converter", u"\u041f\u043b\u043e\u0449\u0430\u0434\u044c", None))
        self.Measurments.setItemText(2, QCoreApplication.translate("Converter", u"\u041e\u0431\u044a\u0435\u043c", None))
        self.Measurments.setItemText(3, QCoreApplication.translate("Converter", u"\u041c\u0430\u0441\u0441\u0430", None))
        self.Measurments.setItemText(4, QCoreApplication.translate("Converter", u"\u0422\u0435\u043c\u043f\u0435\u0440\u0430\u0442\u0443\u0440\u0430", None))
        self.Measurments.setItemText(5, QCoreApplication.translate("Converter", u"\u0421\u043a\u043e\u0440\u043e\u0441\u0442\u044c", None))
        self.Measurments.setItemText(6, QCoreApplication.translate("Converter", u"\u0412\u0440\u0435\u043c\u044f", None))
        self.Measurments.setItemText(7, QCoreApplication.translate("Converter", u"\u0412\u0430\u043b\u044e\u0442\u0430", None))

        self.Number2.setPlaceholderText(QCoreApplication.translate("Converter", u"\u0412\u0432\u0435\u0434\u0438\u0442\u0435 \u0447\u0438\u0441\u043b\u043e ", None))
#if QT_CONFIG(whatsthis)
        self.Number1.setWhatsThis("")
#endif // QT_CONFIG(whatsthis)
        self.Number1.setPlaceholderText(QCoreApplication.translate("Converter", u"\u0412\u0432\u0435\u0434\u0438\u0442\u0435 \u0447\u0438\u0441\u043b\u043e", None))
        self.label_2.setText(QCoreApplication.translate("Converter", u"=", None))
    # retranslateUi

