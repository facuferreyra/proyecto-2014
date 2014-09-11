#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys
import datetime
import dateutil
from PyQt4 import QtCore, QtGui, Qt
from PyQt4.uic import *
from qrcode import *
from datetime import *
from dateutil.relativedelta import *

class asd(QtGui.QMainWindow):
    def __init__(self, parent=None):
        locale=unicode(QtCore.QLocale.system().name())
        QtGui.QWidget.__init__(self, parent)
        self.ui=loadUi("ingreso.ui",self)

    def ing(self):
        usuario=self.ui.lineEdit.text()
        contrasena=self.ui.lineEdit_2.text()
        if (usuario=="facu") and (contrasena=="asd"):
            QtGui.QMessageBox.information(self,"Mensaje de sistema","sesion iniciada")
            cam3=ingreso().show()
            self.close()
            self.logeo=1
        else:
            QtGui.QMessageBox.critical(self,"Mensaje de sistema","error de logeo")
            self.logeo=0
            
               
class ingreso(QtGui.QMainWindow):
    def __init__(self, parent=None):
        locale=unicode(QtCore.QLocale.system().name())
        QtGui.QWidget.__init__(self, parent)
        self.ui=loadUi("entra.ui",self)
    
    def keyPressEvent(self, qKeyEvent):
        if (qKeyEvent.key() == QtCore.Qt.Key_Return):
            self.entrar()
            
    def entrar(self):
        cambio=Myform().show()
        cambio=self.close()

class Myform(QtGui.QMainWindow):
    def __init__(self, parent=None):
        locale=unicode(QtCore.QLocale.system().name())
        QtGui.QWidget.__init__(self, parent)
        self.ui=loadUi("proyec.ui",self)

    def keyPressEvent(self, qKeyEvent):
        if (qKeyEvent.key() == QtCore.Qt.Key_Return):
            self.ok()

    def ok(self):
        nombre=self.ui.lineEdit1.text()
        apellido=a=self.ui.lineEdit2.text()
        sexo=self.ui.comboBox.currentText()
        self.dni=d=self.ui.lineEdit5.text()
        fecha=f=str(self.ui.dateEdit1.text())
        fechaNac=datetime.strptime(fecha,"%x").date()
        dHoy = datetime.now().date()
        if fechaNac.year > dHoy.year:
                fechaNac = datetime(fechaNac.year - 100, fechaNac.month, fechaNac.day) 
        edad = dateutil.relativedelta.relativedelta(dHoy, fechaNac).years
        print edad
        if edad>=16:
            eda="ES MAYOR DE EDAD"
        else:
            eda="ES MENOR DE EDAD"
            
        self.variable=("nombre= "+nombre+"\n"+"apellido= "+a+"\n" +"sexo= "+sexo+"\n"+"dni= "+self.dni+"\n"+"fecha= "+f+"\n\n"+eda)
            
        if self.lineEdit5.text():
            try:
                bar=int(self.lineEdit5.text())
                self.dNi=2
                print self.dNi   
            except :  
                QtGui.QMessageBox.critical(self,"Mensaje de sistema","complete con numeros !!!")       
                self.dNi=0
                print self.dNi   
        if apellido=="" or nombre=="" or sexo=="" or self.dni =="":
            QtGui.QMessageBox.critical(self,"Mensaje de sistema","faltan campos por completar !!!")
            self.dNi=1
        if self.dNi==2:
            QtGui.QMessageBox.information(self,"Mensaje de sistema","Registrado !!!")
            
            with open("archivo.ini","a+r") as z:
                z.write("nombre="+self.ui.lineEdit1.text()+"\n")
                z.write("apellido="+self.ui.lineEdit2.text()+"\n")
                z.write("sexo="+self.ui.comboBox.currentText()+" \n")
                z.write("DNI= "+self.ui.lineEdit5.text()+"\n")
                z.write("fecha-de-nacimiento="+self.ui.dateEdit1.text()+"\n\n\n")
        if self.dNi==2:
            
            camb=codi(self.dni,self.variable).show()
            camb=self.close()
                       
    def nuevo(self):
        self.ui.label_5.clear()

            
class codi(QtGui.QMainWindow):
    def __init__(self, dn,var,parent=None):
        locale=unicode(QtCore.QLocale.system().name())
        QtGui.QWidget.__init__(self, parent)    
        self.ui=loadUi("codigo.ui",self)
        self.dni=dn
        self.variable=var
    def keyPressEvent(self, qKeyEvent):
        if (qKeyEvent.key() == QtCore.Qt.Key_Return):
            self.codigos()
        
    def codigos(self):
        self.dni="registrados/"+str(self.dni)+'.png'
        print self.dni
        qr = QRCode(version=1, box_size=5 ,error_correction=ERROR_CORRECT_L)
        qr.add_data(self.variable)
        qr.make()
        im=qr.make_image()
        im.save(self.dni)

        pixmap=QtGui.QPixmap(self.dni)
        self.qrcode_2.setPixmap(pixmap)
        self.qrcode_2.setGeometry(210,30,291,291)

    def registro(self):
        cam=Myform().show()
        cam=self.close()

    def volver(self):
        cam2=asd().show()
        cam2=self.close()

if __name__=="__main__":
    app=QtGui.QApplication(sys.argv)
    myapp =asd()
    myapp.show()
    sys.exit(app.exec_())
