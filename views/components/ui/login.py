# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'login.ui'
#
# Created by: PyQt5 UI code generator 5.15.6
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(720, 640)
        Form.setAutoFillBackground(False)
        Form.setStyleSheet("background-image: url(:/views/components/ui/image/login.png);")
        self.pushButton = QtWidgets.QPushButton(Form)
        self.pushButton.setEnabled(True)
        self.pushButton.setGeometry(QtCore.QRect(420, 370, 203, 35))
        self.pushButton.setStyleSheet("background-color: rgb(139, 255, 156);\n"
"font: 9pt \"宋体\";")
        self.pushButton.setObjectName("pushButton")
        self.lineEdit = QtWidgets.QLineEdit(Form)
        self.lineEdit.setGeometry(QtCore.QRect(420, 260, 200, 35))
        self.lineEdit.setStyleSheet("border-color: rgb(85, 255, 255);\n"
"background-color: rgb(85, 255, 255);")
        self.lineEdit.setInputMask("")
        self.lineEdit.setText("")
        self.lineEdit.setObjectName("lineEdit")
        self.lineEdit_2 = QtWidgets.QLineEdit(Form)
        self.lineEdit_2.setGeometry(QtCore.QRect(420, 320, 200, 35))
        self.lineEdit_2.setStyleSheet("background-color: rgb(85, 255, 255);\n"
"font: 9pt \"Aldhabi\";\n"
"border-color: rgb(85, 255, 255);")
        self.lineEdit_2.setInputMask("")
        self.lineEdit_2.setText("")
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.label = QtWidgets.QLabel(Form)
        self.label.setGeometry(QtCore.QRect(340, 260, 72, 35))
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(Form)
        self.label_2.setGeometry(QtCore.QRect(340, 320, 72, 35))
        self.label_2.setObjectName("label_2")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "登录"))
        self.pushButton.setText(_translate("Form", "登录"))
        self.label.setText(_translate("Form", "<html><head/><body><p align=\"right\"><span style=\" font-weight:600; color:#55ffff;\">用户名 ：</span></p></body></html>"))
        self.label_2.setText(_translate("Form", "<html><head/><body><p align=\"right\"><span style=\" font-weight:600; color:#55ffff;\">密码 ：</span></p></body></html>"))
import views.components.ui.login_rc

class LoginWidget(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()
        self.form=Ui_Form()
        self.form.setupUi(self)
        self.button=self.form.pushButton
        self.nameEdit=self.form.lineEdit
        self.passwdEdit=self.form.lineEdit_2