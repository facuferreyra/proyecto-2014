# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'proyec.ui'
#
# Created: Wed Jul 30 21:59:52 2014
#      by: PyQt4 UI code generator 4.10.4
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName(_fromUtf8("Form"))
        Form.resize(662, 657)
        self.tabWidget = QtGui.QTabWidget(Form)
        self.tabWidget.setGeometry(QtCore.QRect(40, 70, 591, 471))
        self.tabWidget.setObjectName(_fromUtf8("tabWidget"))
        self.tab = QtGui.QWidget()
        self.tab.setObjectName(_fromUtf8("tab"))
        self.lineEdit1 = QtGui.QLineEdit(self.tab)
        self.lineEdit1.setGeometry(QtCore.QRect(160, 10, 231, 20))
        self.lineEdit1.setObjectName(_fromUtf8("lineEdit1"))
        self.line_3 = QtGui.QFrame(self.tab)
        self.line_3.setGeometry(QtCore.QRect(0, 130, 451, 20))
        self.line_3.setFrameShape(QtGui.QFrame.HLine)
        self.line_3.setFrameShadow(QtGui.QFrame.Sunken)
        self.line_3.setObjectName(_fromUtf8("line_3"))
        self.label_6 = QtGui.QLabel(self.tab)
        self.label_6.setGeometry(QtCore.QRect(10, 190, 66, 17))
        self.label_6.setObjectName(_fromUtf8("label_6"))
        self.label_2 = QtGui.QLabel(self.tab)
        self.label_2.setGeometry(QtCore.QRect(10, 70, 66, 17))
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.lineEdit3 = QtGui.QLineEdit(self.tab)
        self.lineEdit3.setGeometry(QtCore.QRect(160, 110, 231, 21))
        self.lineEdit3.setObjectName(_fromUtf8("lineEdit3"))
        self.lineEdit2 = QtGui.QLineEdit(self.tab)
        self.lineEdit2.setGeometry(QtCore.QRect(160, 60, 231, 21))
        self.lineEdit2.setObjectName(_fromUtf8("lineEdit2"))
        self.pushButton = QtGui.QPushButton(self.tab)
        self.pushButton.setGeometry(QtCore.QRect(310, 400, 98, 27))
        self.pushButton.setObjectName(_fromUtf8("pushButton"))
        self.line = QtGui.QFrame(self.tab)
        self.line.setGeometry(QtCore.QRect(0, 40, 451, 21))
        self.line.setFrameShape(QtGui.QFrame.HLine)
        self.line.setFrameShadow(QtGui.QFrame.Sunken)
        self.line.setObjectName(_fromUtf8("line"))
        self.label_5 = QtGui.QLabel(self.tab)
        self.label_5.setGeometry(QtCore.QRect(170, 390, 101, 17))
        self.label_5.setText(_fromUtf8(""))
        self.label_5.setObjectName(_fromUtf8("label_5"))
        self.lineEdit5 = QtGui.QLineEdit(self.tab)
        self.lineEdit5.setGeometry(QtCore.QRect(160, 190, 231, 21))
        self.lineEdit5.setObjectName(_fromUtf8("lineEdit5"))
        self.label_3 = QtGui.QLabel(self.tab)
        self.label_3.setGeometry(QtCore.QRect(10, 110, 66, 17))
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.line_2 = QtGui.QFrame(self.tab)
        self.line_2.setGeometry(QtCore.QRect(10, 80, 441, 20))
        self.line_2.setFrameShape(QtGui.QFrame.HLine)
        self.line_2.setFrameShadow(QtGui.QFrame.Sunken)
        self.line_2.setObjectName(_fromUtf8("line_2"))
        self.line_4 = QtGui.QFrame(self.tab)
        self.line_4.setGeometry(QtCore.QRect(10, 170, 451, 20))
        self.line_4.setFrameShape(QtGui.QFrame.HLine)
        self.line_4.setFrameShadow(QtGui.QFrame.Sunken)
        self.line_4.setObjectName(_fromUtf8("line_4"))
        self.lineEdit4 = QtGui.QLineEdit(self.tab)
        self.lineEdit4.setGeometry(QtCore.QRect(160, 147, 231, 20))
        self.lineEdit4.setObjectName(_fromUtf8("lineEdit4"))
        self.label = QtGui.QLabel(self.tab)
        self.label.setGeometry(QtCore.QRect(10, 10, 71, 20))
        self.label.setObjectName(_fromUtf8("label"))
        self.pushButton_2 = QtGui.QPushButton(self.tab)
        self.pushButton_2.setGeometry(QtCore.QRect(40, 390, 98, 27))
        self.pushButton_2.setObjectName(_fromUtf8("pushButton_2"))
        self.label_4 = QtGui.QLabel(self.tab)
        self.label_4.setGeometry(QtCore.QRect(10, 150, 66, 17))
        self.label_4.setObjectName(_fromUtf8("label_4"))
        self.line_5 = QtGui.QFrame(self.tab)
        self.line_5.setGeometry(QtCore.QRect(10, 210, 441, 21))
        self.line_5.setFrameShape(QtGui.QFrame.HLine)
        self.line_5.setFrameShadow(QtGui.QFrame.Sunken)
        self.line_5.setObjectName(_fromUtf8("line_5"))
        self.label_7 = QtGui.QLabel(self.tab)
        self.label_7.setGeometry(QtCore.QRect(10, 230, 141, 16))
        self.label_7.setObjectName(_fromUtf8("label_7"))
        self.lineEdit6 = QtGui.QLineEdit(self.tab)
        self.lineEdit6.setGeometry(QtCore.QRect(160, 230, 111, 21))
        self.lineEdit6.setObjectName(_fromUtf8("lineEdit6"))
        self.tabWidget.addTab(self.tab, _fromUtf8(""))
        self.tab_2 = QtGui.QWidget()
        self.tab_2.setObjectName(_fromUtf8("tab_2"))
        self.textBrowser = QtGui.QTextBrowser(self.tab_2)
        self.textBrowser.setGeometry(QtCore.QRect(0, 0, 521, 321))
        self.textBrowser.setObjectName(_fromUtf8("textBrowser"))
        self.tabWidget.addTab(self.tab_2, _fromUtf8(""))

        self.retranslateUi(Form)
        self.tabWidget.setCurrentIndex(1)
        QtCore.QObject.connect(self.pushButton, QtCore.SIGNAL(_fromUtf8("clicked()")), Form.ok)
        QtCore.QObject.connect(self.pushButton_2, QtCore.SIGNAL(_fromUtf8("clicked()")), self.lineEdit4.clear)
        QtCore.QObject.connect(self.pushButton_2, QtCore.SIGNAL(_fromUtf8("clicked()")), self.lineEdit3.clear)
        QtCore.QObject.connect(self.pushButton_2, QtCore.SIGNAL(_fromUtf8("clicked()")), self.lineEdit2.clear)
        QtCore.QObject.connect(self.pushButton_2, QtCore.SIGNAL(_fromUtf8("clicked()")), self.lineEdit1.clear)
        QtCore.QObject.connect(self.pushButton_2, QtCore.SIGNAL(_fromUtf8("clicked()")), self.lineEdit5.clear)
        QtCore.QObject.connect(self.pushButton_2, QtCore.SIGNAL(_fromUtf8("clicked()")), self.lineEdit6.clear)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        Form.setWindowTitle(_translate("Form", "Form", None))
        self.label_6.setText(_translate("Form", "DNI:", None))
        self.label_2.setText(_translate("Form", "apellido :", None))
        self.pushButton.setText(_translate("Form", "OK", None))
        self.label_3.setText(_translate("Form", "sexo:", None))
        self.label.setText(_translate("Form", "nombre:", None))
        self.pushButton_2.setText(_translate("Form", "nuevo ", None))
        self.label_4.setText(_translate("Form", "domicilio:", None))
        self.label_7.setText(_translate("Form", "fecha de nacimiento: ", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), _translate("Form", "registro", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), _translate("Form", "registrados en el lugar", None))

