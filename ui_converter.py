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
from PySide6.QtWidgets import (QApplication, QComboBox, QHBoxLayout, QLabel,
    QLayout, QLineEdit, QMainWindow, QMenuBar,
    QPushButton, QSizePolicy, QSplitter, QStatusBar,
    QVBoxLayout, QWidget)

class Ui_Converter(object):
    def setupUi(self, Converter):
        if not Converter.objectName():
            Converter.setObjectName(u"Converter")
        Converter.resize(642, 209)
        font = QFont()
        font.setPointSize(10)
        Converter.setFont(font)
        self.centralwidget = QWidget(Converter)
        self.centralwidget.setObjectName(u"centralwidget")
        self.widget = QWidget(self.centralwidget)
        self.widget.setObjectName(u"widget")
        self.widget.setGeometry(QRect(21, 12, 565, 128))
        self.verticalLayout_3 = QVBoxLayout(self.widget)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.label = QLabel(self.widget)
        self.label.setObjectName(u"label")
        font1 = QFont()
        font1.setPointSize(15)
        self.label.setFont(font1)

        self.verticalLayout.addWidget(self.label)

        self.Measurments = QComboBox(self.widget)
        self.Measurments.addItem("")
        self.Measurments.addItem("")
        self.Measurments.addItem("")
        self.Measurments.addItem("")
        self.Measurments.addItem("")
        self.Measurments.addItem("")
        self.Measurments.addItem("")
        self.Measurments.addItem("")
        self.Measurments.setObjectName(u"Measurments")
        self.Measurments.setFont(font1)

        self.verticalLayout.addWidget(self.Measurments)


        self.horizontalLayout_3.addLayout(self.verticalLayout)

        self.splitter = QSplitter(self.widget)
        self.splitter.setObjectName(u"splitter")
        self.splitter.setOrientation(Qt.Vertical)
        self.layoutWidget = QWidget(self.splitter)
        self.layoutWidget.setObjectName(u"layoutWidget")
        self.verticalLayout_2 = QVBoxLayout(self.layoutWidget)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.clearleft = QPushButton(self.layoutWidget)
        self.clearleft.setObjectName(u"clearleft")

        self.horizontalLayout_2.addWidget(self.clearleft)

        self.clearright = QPushButton(self.layoutWidget)
        self.clearright.setObjectName(u"clearright")

        self.horizontalLayout_2.addWidget(self.clearright)


        self.verticalLayout_2.addLayout(self.horizontalLayout_2)

        self.clearall = QPushButton(self.layoutWidget)
        self.clearall.setObjectName(u"clearall")

        self.verticalLayout_2.addWidget(self.clearall)

        self.splitter.addWidget(self.layoutWidget)

        self.horizontalLayout_3.addWidget(self.splitter)


        self.verticalLayout_3.addLayout(self.horizontalLayout_3)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setSpacing(5)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setSizeConstraint(QLayout.SetMaximumSize)
        self.horizontalLayout.setContentsMargins(2, -1, -1, -1)
        self.Number1 = QLineEdit(self.widget)
        self.Number1.setObjectName(u"Number1")
        self.Number1.setFont(font)
        self.Number1.setAutoFillBackground(False)

        self.horizontalLayout.addWidget(self.Number1)

        self.Select1 = QComboBox(self.widget)
        self.Select1.setObjectName(u"Select1")

        self.horizontalLayout.addWidget(self.Select1)

        self.label_2 = QLabel(self.widget)
        self.label_2.setObjectName(u"label_2")
        font2 = QFont()
        font2.setPointSize(20)
        self.label_2.setFont(font2)

        self.horizontalLayout.addWidget(self.label_2)

        self.Number2 = QLineEdit(self.widget)
        self.Number2.setObjectName(u"Number2")
        self.Number2.setFont(font)

        self.horizontalLayout.addWidget(self.Number2)

        self.Select2 = QComboBox(self.widget)
        self.Select2.setObjectName(u"Select2")

        self.horizontalLayout.addWidget(self.Select2)


        self.verticalLayout_3.addLayout(self.horizontalLayout)

        Converter.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(Converter)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 642, 26))
        Converter.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(Converter)
        self.statusbar.setObjectName(u"statusbar")
        Converter.setStatusBar(self.statusbar)

        self.retranslateUi(Converter)

        QMetaObject.connectSlotsByName(Converter)
    # setupUi

    def retranslateUi(self, Converter):
        Converter.setWindowTitle(QCoreApplication.translate("Converter", u"Converter", None))
        self.label.setText(QCoreApplication.translate("Converter", u"\u0415\u0434\u0438\u043d\u0438\u0446\u044b \u0438\u0437\u043c\u0435\u0440\u0435\u043d\u0438\u044f", None))
        self.Measurments.setItemText(0, QCoreApplication.translate("Converter", u"\u0414\u043b\u0438\u043d\u0430", None))
        self.Measurments.setItemText(1, QCoreApplication.translate("Converter", u"\u0412\u0430\u043b\u044e\u0442\u0430", None))
        self.Measurments.setItemText(2, QCoreApplication.translate("Converter", u"\u041f\u043b\u043e\u0449\u0430\u0434\u044c", None))
        self.Measurments.setItemText(3, QCoreApplication.translate("Converter", u"\u041e\u0431\u044a\u0435\u043c", None))
        self.Measurments.setItemText(4, QCoreApplication.translate("Converter", u"\u041c\u0430\u0441\u0441\u0430", None))
        self.Measurments.setItemText(5, QCoreApplication.translate("Converter", u"\u0422\u0435\u043c\u043f\u0435\u0440\u0430\u0442\u0443\u0440\u0430", None))
        self.Measurments.setItemText(6, QCoreApplication.translate("Converter", u"\u0421\u043a\u043e\u0440\u043e\u0441\u0442\u044c", None))
        self.Measurments.setItemText(7, QCoreApplication.translate("Converter", u"\u0412\u0440\u0435\u043c\u044f", None))

        self.clearleft.setText(QCoreApplication.translate("Converter", u"\u041e\u0447\u0438\u0441\u0442\u0438\u0442\u044c \u043b\u0435\u0432\u043e", None))
        self.clearright.setText(QCoreApplication.translate("Converter", u"\u041e\u0447\u0438\u0442\u0441\u0442\u0438\u0442\u044c \u043f\u0440\u0430\u0432\u043e", None))
        self.clearall.setText(QCoreApplication.translate("Converter", u"\u041e\u0447\u0438\u0442\u0441\u0442\u0438\u0442\u044c \u0432\u0441\u0435", None))
#if QT_CONFIG(whatsthis)
        self.Number1.setWhatsThis("")
#endif // QT_CONFIG(whatsthis)
        self.Number1.setPlaceholderText(QCoreApplication.translate("Converter", u"\u0412\u0432\u0435\u0434\u0438\u0442\u0435 \u0447\u0438\u0441\u043b\u043e", None))
        self.label_2.setText(QCoreApplication.translate("Converter", u"=", None))
        self.Number2.setPlaceholderText(QCoreApplication.translate("Converter", u"\u0412\u0432\u0435\u0434\u0438\u0442\u0435 \u0447\u0438\u0441\u043b\u043e ", None))
    # retranslateUi

