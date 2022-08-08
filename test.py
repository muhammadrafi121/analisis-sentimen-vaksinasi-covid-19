# -*- coding: utf-8 -*-
"""
Created on Tue Jun 28 17:23:16 2022

@author: Acer
"""

from PyQt5 import QtCore, QtGui, QtWidgets 
from PyQt5.QtCore import Qt
import sys
import pandas as pd 
import numpy as np
#Class Ui_Setting merupakan kelas parent dimana iya membuat objek dari semua tampilan interface
class Ui_Setting(object):
    #method yang mengatur dan membuat objek pada interface 
    def setting_ui(self, MainWindow):
        MainWindow.setObjectName("MainWindow") 
        MainWindow.resize(982, 707)
        
        self.centralwidget = QtWidgets.QWidget(MainWindow) 
        self.centralwidget.setObjectName("centralwidget") 
        
        
        self.tampil_hasil_preproses = QtWidgets.QTableView(self.centralwidget) 
        self.tampil_hasil_preproses.setGeometry(QtCore.QRect(10, 120, 301, 461))
        self.tampil_hasil_preproses.setObjectName("tampil_hasil_preproses")
        self.tampil_hasil_preproses.horizontalHeader().setSectionResizeMode(QtWidgets.QHeaderView.Stretch)
        self.tampil_hasil_preproses.horizontalHeader().setVisible(False) 
        
        
        r"""
        self.tampil_hasil_train = QtWidgets.QTableView(self.centralwidget) 
        self.tampil_hasil_train.setGeometry(QtCore.QRect(330, 240, 631, 311))
        self.tampil_hasil_train.setObjectName("tampil_hasil_train") 
        self.tampil_hasil_train.verticalHeader().setVisible(False) 
        self.tampil_hasil_train.horizontalHeader().setVisible(False) 
        """
        
        
        self.actionbutton_prapengolahan = QtWidgets.QPushButton(self.centralwidget) 
        self.actionbutton_prapengolahan.setGeometry(QtCore.QRect(70, 60, 151, 23))
        self.actionbutton_prapengolahan.setObjectName("actionbutton_prapengolahan")
        
        self.Label_HasilPrapengolahan = QtWidgets.QLabel(self.centralwidget)
        self.Label_HasilPrapengolahan.setGeometry(QtCore.QRect(50, 100, 191, 16))
        font = QtGui.QFont() 
        font.setFamily("Times New Roman") 
        font.setPointSize(11) 
        font.setBold(True) 
        font.setWeight(75)
        self.Label_HasilPrapengolahan.setFont(font)
        self.Label_HasilPrapengolahan.setObjectName("Label_HasilPrapengolahan")
        
        
        self.Label_PilihMetode = QtWidgets.QLabel(self.centralwidget) 
        self.Label_PilihMetode.setGeometry(QtCore.QRect(590, 50, 191, 16)) 
        font = QtGui.QFont()
        font.setFamily("Times New Roman") 
        font.setPointSize(11) 
        font.setBold(True) 
        font.setWeight(75) 
        self.Label_PilihMetode.setFont(font)
        self.Label_PilihMetode.setObjectName("Label_PilihMetode")
        
        self.Label_Metode = QtWidgets.QLabel(self.centralwidget) 
        self.Label_Metode.setGeometry(QtCore.QRect(400, 80, 191, 16)) 
        font = QtGui.QFont()
        font.setFamily("Times New Roman") 
        font.setPointSize(11) 
        font.setBold(True) 
        font.setWeight(75)
        self.Label_Metode.setFont(font) 
        self.Label_Metode.setObjectName("Label_Metode") 
        
        self.Label_Kernel = QtWidgets.QLabel(self.centralwidget) 
        self.Label_Kernel.setGeometry(QtCore.QRect(400, 110, 191, 16)) 
        font = QtGui.QFont()
        font.setFamily("Times New Roman") 
        font.setPointSize(11) 
        font.setBold(True) 
        font.setWeight(75) 
        self.Label_Kernel.setFont(font)
        self.Label_Kernel.setObjectName("Label_Kernel") 
        
        self.Label_NilaiC = QtWidgets.QLabel(self.centralwidget) 
        self.Label_NilaiC.setGeometry(QtCore.QRect(400, 140, 191, 16)) 
        font = QtGui.QFont()
        font.setFamily("Times New Roman") 
        font.setPointSize(11) 
        font.setBold(True) 
        font.setWeight(75)
        self.Label_NilaiC.setFont(font) 
        self.Label_NilaiC.setObjectName("Label_NilaiC") 
        
        self.Label_NilaiK = QtWidgets.QLabel(self.centralwidget) 
        self.Label_NilaiK.setGeometry(QtCore.QRect(400, 170, 191, 16)) 
        font = QtGui.QFont()
        font.setFamily("Times New Roman") 
        font.setPointSize(11) 
        font.setBold(True) 
        font.setWeight(75) 
        self.Label_NilaiK.setFont(font)
        self.Label_NilaiK.setObjectName("Label_NilaiK") 
        
        self.Label_JumlahFitur = QtWidgets.QLabel(self.centralwidget) 
        self.Label_JumlahFitur.setGeometry(QtCore.QRect(370, 560, 101,
        16))
        font = QtGui.QFont() 
        font.setFamily("Times New Roman") 
        font.setPointSize(11) 
        font.setBold(True) 
        font.setWeight(75) 
        self.Label_JumlahFitur.setFont(font)
        self.Label_JumlahFitur.setObjectName("Label_JumlahFitur") 
        
        self.actionbutton_klasifikasi_train = QtWidgets.QPushButton(self.centralwidget) 
        self.actionbutton_klasifikasi_train.setGeometry(QtCore.QRect(550,
        210, 181, 23))
        self.actionbutton_klasifikasi_train.setObjectName("actionbutton_klasifikasi_train")
        
        self.groupbox_metode = QtWidgets.QGroupBox(self.centralwidget) 
        self.groupbox_metode.setGeometry(QtCore.QRect(470, 70, 381, 31)) 
        self.groupbox_metode.setTitle("") 
        self.groupbox_metode.setCheckable(False) 
        self.groupbox_metode.setObjectName("groupbox_metode") 
        
        self.tanpaseleksifitur = QtWidgets.QRadioButton(self.groupbox_metode) 
        self.tanpaseleksifitur.setGeometry(QtCore.QRect(10, 10, 161, 17)) 
        self.tanpaseleksifitur.setObjectName("tanpaseleksifitur") 
        
        self.seleksifitur = QtWidgets.QRadioButton(self.groupbox_metode) 
        self.seleksifitur.setGeometry(QtCore.QRect(220, 10, 151, 17)) 
        self.seleksifitur.setObjectName("seleksifitur")
        
        self.groupbox_kernel = QtWidgets.QGroupBox(self.centralwidget) 
        self.groupbox_kernel.setGeometry(QtCore.QRect(470, 100, 381, 31)) 
        self.groupbox_kernel.setTitle("") 
        self.groupbox_kernel.setObjectName("groupbox_kernel")
        
        self.linear = QtWidgets.QRadioButton(self.groupbox_kernel)
        self.linear.setGeometry(QtCore.QRect(10, 10, 82, 17)) 
        self.linear.setObjectName("linear")
        
        self.polynomial = QtWidgets.QRadioButton(self.groupbox_kernel) 
        self.polynomial.setGeometry(QtCore.QRect(120, 10, 82, 17)) 
        self.polynomial.setObjectName("polynomial")
        
        self.rbf = QtWidgets.QRadioButton(self.groupbox_kernel) 
        self.rbf.setGeometry(QtCore.QRect(220, 10, 82, 17)) 
        self.rbf.setObjectName("rbf")
        
        self.groupbox_nilaic = QtWidgets.QGroupBox(self.centralwidget) 
        self.groupbox_nilaic.setGeometry(QtCore.QRect(470, 140, 381, 21)) 
        self.groupbox_nilaic.setTitle("") 
        self.groupbox_nilaic.setObjectName("groupbox_nilaic") 
        
        self.radioButtonnilaic_1 = QtWidgets.QRadioButton(self.groupbox_nilaic) 
        self.radioButtonnilaic_1.setGeometry(QtCore.QRect(10, 0, 82, 17)) 
        self.radioButtonnilaic_1.setObjectName("radioButtonnilaic_1") 
        
        self.radioButtonnilaic_2 = QtWidgets.QRadioButton(self.groupbox_nilaic) 
        self.radioButtonnilaic_2.setGeometry(QtCore.QRect(120, 0, 82, 17)) 
        self.radioButtonnilaic_2.setObjectName("radioButton_2") 
        
        self.tampil_hasil_jumlah_fitur = QtWidgets.QLineEdit(self.centralwidget) 
        self.tampil_hasil_jumlah_fitur.setGeometry(QtCore.QRect(480, 560, 113, 20))
        self.tampil_hasil_jumlah_fitur.setObjectName("tampil_hasil_jumlah_fitur") 
        
        self.horizontalScrollBar = QtWidgets.QScrollBar(self.centralwidget) 
        self.horizontalScrollBar.setGeometry(QtCore.QRect(110, 730, 211, 20))
        self.horizontalScrollBar.setOrientation(QtCore.Qt.Horizontal) 
        self.horizontalScrollBar.setObjectName("horizontalScrollBar") 
        
        self.masukan_nilaik = QtWidgets.QLineEdit(self.centralwidget) 
        self.masukan_nilaik.setGeometry(QtCore.QRect(480, 170, 113, 20)) 
        self.masukan_nilaik.setObjectName("masukan_nilaik") 
        
        self.masukan_komentar = QtWidgets.QLineEdit(self.centralwidget) 
        self.masukan_komentar.setGeometry(QtCore.QRect(190, 620, 611, 31))
        self.masukan_komentar.setObjectName("masukan_komentar") 
        
        self.Label_JumlahFitur_2 = QtWidgets.QLabel(self.centralwidget) 
        self.Label_JumlahFitur_2.setGeometry(QtCore.QRect(420, 590, 181, 31))
        font = QtGui.QFont() 
        font.setFamily("Times New Roman") 
        font.setPointSize(14) 
        font.setBold(True) 
        font.setWeight(75)
        self.Label_JumlahFitur_2.setFont(font) 
        self.Label_JumlahFitur_2.setObjectName("Label_JumlahFitur_2") 
        
        self.Label_JumlahFitur_3 = QtWidgets.QLabel(self.centralwidget) 
        self.Label_JumlahFitur_3.setGeometry(QtCore.QRect(20, 620, 151, 20))
        font = QtGui.QFont() 
        font.setFamily("Times New Roman") 
        font.setPointSize(11) 
        font.setBold(True) 
        font.setWeight(75)
        self.Label_JumlahFitur_3.setFont(font) 
        self.Label_JumlahFitur_3.setObjectName("Label_JumlahFitur_3") 
        
        self.actionbutton_klasifikasi_test = QtWidgets.QPushButton(self.centralwidget) 
        self.actionbutton_klasifikasi_test.setGeometry(QtCore.QRect(830, 620, 131, 31))
        self.actionbutton_klasifikasi_test.setObjectName("actionbutton_klasifikasi_test")
        
        self.line = QtWidgets.QFrame(self.centralwidget) 
        self.line.setGeometry(QtCore.QRect(0, 580, 971, 20)) 
        self.line.setFrameShape(QtWidgets.QFrame.HLine) 
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken) 
        self.line.setObjectName("line")
        
        self.Label_JumlahFitur_4 = QtWidgets.QLabel(self.centralwidget) 
        self.Label_JumlahFitur_4.setGeometry(QtCore.QRect(20, 660, 171, 20))
        font = QtGui.QFont() 
        font.setFamily("Times New Roman") 
        font.setPointSize(11) 
        font.setBold(True) 
        font.setWeight(75)
        self.Label_JumlahFitur_4.setFont(font) 
        self.Label_JumlahFitur_4.setObjectName("Label_JumlahFitur_4") 
        
        self.tampil_hasil_komentar = QtWidgets.QLineEdit(self.centralwidget) 
        self.tampil_hasil_komentar.setGeometry(QtCore.QRect(190, 660, 141, 20))
        self.tampil_hasil_komentar.setObjectName("tampil_hasil_komentar") 
        
        self.line_2 = QtWidgets.QFrame(self.centralwidget) 
        self.line_2.setGeometry(QtCore.QRect(10, 50, 20, 541)) 
        self.line_2.setFrameShape(QtWidgets.QFrame.VLine) 
        self.line_2.setFrameShadow(QtWidgets.QFrame.Sunken) 
        self.line_2.setObjectName("line_2")
        
        self.line_3 = QtWidgets.QFrame(self.centralwidget)
        self.line_3.setGeometry(QtCore.QRect(320, 40, 651, 20)) 
        self.line_3.setFrameShape(QtWidgets.QFrame.HLine) 
        self.line_3.setFrameShadow(QtWidgets.QFrame.Sunken) 
        self.line_3.setObjectName("line_3")
        
        self.line_4 = QtWidgets.QFrame(self.centralwidget) 
        self.line_4.setGeometry(QtCore.QRect(960, 50, 20, 541)) 
        self.line_4.setFrameShape(QtWidgets.QFrame.VLine) 
        self.line_4.setFrameShadow(QtWidgets.QFrame.Sunken) 
        self.line_4.setObjectName("line_4")
        
        self.background = QtWidgets.QLabel(self.centralwidget) 
        self.background.setGeometry(QtCore.QRect(280, 20, 47, 13)) 
        self.background.setText("") 
        self.background.setObjectName("background") 
        
        self.Label_Perangkatlunak = QtWidgets.QLabel(self.centralwidget) 
        self.Label_Perangkatlunak.setGeometry(QtCore.QRect(30, 10, 941, 21))
        font = QtGui.QFont() 
        font.setFamily("Times New Roman") 
        font.setPointSize(12) 
        font.setBold(True) 
        font.setItalic(False) 
        font.setUnderline(False) 
        font.setWeight(75) 
        font.setStrikeOut(False)
        self.Label_Perangkatlunak.setFont(font) 
        self.Label_Perangkatlunak.setMouseTracking(False) 
        self.Label_Perangkatlunak.setText("") 
        self.Label_Perangkatlunak.setPixmap(QtGui.QPixmap("assets/Habis gelap terbitlah.png")) 
        self.Label_Perangkatlunak.setObjectName("Label_Perangkatlunak") 
        
        self.label = QtWidgets.QLabel(self.centralwidget) 
        self.label.setGeometry(QtCore.QRect(610, 170, 261, 20))
        font = QtGui.QFont() 
        font.setFamily("Times New Roman") 
        font.setPointSize(9) 
        font.setItalic(True) 
        self.label.setFont(font)
        self.label.setAutoFillBackground(False) 
        self.label.setObjectName("label")
        
        self.label_2 = QtWidgets.QLabel(self.centralwidget) 
        self.label_2.setGeometry(QtCore.QRect(0, 0, 1001, 731)) 
        self.label_2.setText("") 
        self.label_2.setPixmap(QtGui.QPixmap("assets/Hotel (2).png")) 
        self.label_2.setObjectName("label_2")
        self.label_2.raise_()
        
        self.tampil_hasil_preproses.raise_() 
        self.actionbutton_prapengolahan.raise_() 
        self.Label_HasilPrapengolahan.raise_() 
        
        # self.tampil_hasil_train.raise_() 
        self.Label_PilihMetode.raise_() 
        self.Label_Metode.raise_() 
        self.Label_Kernel.raise_() 
        self.Label_NilaiC.raise_() 
        self.Label_NilaiK.raise_() 
        self.Label_JumlahFitur.raise_() 
        self.actionbutton_klasifikasi_train.raise_() 
        self.groupbox_metode.raise_() 
        self.groupbox_kernel.raise_() 
        self.groupbox_nilaic.raise_() 
        self.tampil_hasil_jumlah_fitur.raise_() 
        self.horizontalScrollBar.raise_() 
        self.masukan_nilaik.raise_() 
        self.masukan_komentar.raise_() 
        self.Label_JumlahFitur_2.raise_() 
        self.Label_JumlahFitur_3.raise_() 
        self.actionbutton_klasifikasi_test.raise_() 
        self.line.raise_() 
        self.Label_JumlahFitur_4.raise_() 
        self.tampil_hasil_komentar.raise_() 
        self.line_2.raise_()
        self.line_3.raise_() 
        self.line_4.raise_() 
        self.background.raise_() 
        self.label.raise_() 
        self.Label_Perangkatlunak.raise_()
        MainWindow.setCentralWidget(self.centralwidget) 
        self.statusbar = QtWidgets.QStatusBar(MainWindow) 
        self.statusbar.setObjectName("statusbar") 
        MainWindow.setStatusBar(self.statusbar)
        self.retranslateUi(MainWindow) 
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        
        #Method yang mengatur penamaan objek pada interface 
    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate 
        MainWindow.setWindowTitle(_translate("MainWindow",
        "MainWindow")) 
        self.actionbutton_prapengolahan.setText(_translate("MainWindow", "Proses Data"))
        self.Label_HasilPrapengolahan.setText(_translate("MainWindow", "Hasil Pra-pengolahan Data"))
        self.Label_PilihMetode.setText(_translate("MainWindow", "Pilih Metode"))
        self.Label_Metode.setText(_translate("MainWindow", "Metode :")) 
        self.Label_Kernel.setText(_translate("MainWindow", "Kernel :")) 
        self.Label_NilaiC.setText(_translate("MainWindow", "Nilai C :")) 
        self.Label_NilaiK.setText(_translate("MainWindow", "Nilai K :")) 
        self.Label_JumlahFitur.setText(_translate("MainWindow", "Jumlah Fitur :"))
        self.actionbutton_klasifikasi_train.setText(_translate("MainWindow", "Model Klasifikasi (Train and Test)"))
        self.tanpaseleksifitur.setText(_translate("MainWindow", "Tanpa Seleksi Fitur "))
        self.seleksifitur.setText(_translate("MainWindow", "Seleksi Fitur ")) 
        self.linear.setText(_translate("MainWindow", "linear")) 
        self.polynomial.setText(_translate("MainWindow", "polynomial")) 
        self.rbf.setText(_translate("MainWindow", "rbf")) 
        self.radioButtonnilaic_1.setText(_translate("MainWindow", "0.1"))
        self.radioButtonnilaic_2.setText(_translate("MainWindow", "1")) 
        self.Label_JumlahFitur_2.setText(_translate("MainWindow", "Pengujian Komentar")) 
        self.Label_JumlahFitur_3.setText(_translate("MainWindow", "Masukkan Komentar :")) 
        self.actionbutton_klasifikasi_test.setText(_translate("MainWindow", "Klasifikasi Komentar")) 
        self.Label_JumlahFitur_4.setText(_translate("MainWindow", "Hasil Komentar :"))
        self.label.setText(_translate("MainWindow", "*Range nilai 0-1 (Contoh masukan : 0.2)"))
        
class AktivitasPengguna(QtWidgets.QMainWindow): 
#method Connect signal objek di initialisasi
    def __init__(self): 
        QtWidgets.QMainWindow.__init__(self)
        self.ui = Ui_Setting() 
        self.ui.setting_ui(self)

#main Program
if __name__ =="__main__": 
    app=QtWidgets.QApplication(sys.argv) 
    w=AktivitasPengguna()
    w.show() 
    sys.exit(app.exec_())