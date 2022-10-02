# -*- coding: utf-8 -*-
"""
Created on Tue Jun 28 05:18:35 2022

@author: Acer
"""
import webbrowser, sys

from PyQt5 import QtGui

from PyQt5.QtCore import (
    Qt, 
    QRect, 
    QCoreApplication, 
    QAbstractTableModel, 
    )
from PyQt5.QtWidgets import (
    QFrame, 
    QLabel, 
    QWidget, 
    QComboBox, 
    QLineEdit,  
    QTableView, 
    QMessageBox, 
    QFileDialog, 
    QMainWindow, 
    QPushButton,
    QHeaderView, 
    QApplication, 
    )

class TableModel(QAbstractTableModel):
    def __init__(self, data, headerlabels):
        super(TableModel, self).__init__()
        
        self.horizontalHeaders = [''] * len(headerlabels)
        
        for i in range(len(headerlabels)):
            self.setHeaderData(i, Qt.Horizontal, headerlabels[i])
            
        self._data = data
        
    def setHeaderData(self, section, orientation, data, role=Qt.EditRole):
        if orientation == Qt.Horizontal and role in (Qt.DisplayRole, Qt.EditRole):
            try:
                self.horizontalHeaders[section] = data
                return True
            except:
                return False
        return super().setHeaderData(section, orientation, data, role)

    def headerData(self, section, orientation, role=Qt.DisplayRole):
        if orientation == Qt.Horizontal and role == Qt.DisplayRole:
            try:
                return self.horizontalHeaders[section]
            except:
                pass
        return super().headerData(section, orientation, role)

    def data(self, index, role):
        if role == Qt.DisplayRole:
            # See below for the nested-list data structure.
            # .row() indexes into the outer list,
            # .column() indexes into the sub-list
            return self._data[index.row()][index.column()]

    def rowCount(self, index):
        # The length of the outer list.
        return len(self._data)

    def columnCount(self, index):
        # The following takes the first sub-list, and returns
        # the length (only works if all rows are an equal length)
        return len(self._data[0])

class View(QMainWindow):
    def __init__(self):
        pass

    def main(self, controller):
        app = QApplication([])

        super().__init__()  
        
        self.controller = controller
        self._setUI()
        self.show()
        
        app.exec()
        
    def _setUI(self):
        self.setObjectName("MainWindow")
        self.resize(900, 850)
        
        container = QWidget()
        container.setObjectName("Container")
        self.setCentralWidget(container)
        
        self.label_dataset = QLabel(container) 
        self.label_dataset.setGeometry(QRect(10, 20, 200, 16)) 
        font = QtGui.QFont()
        font.setFamily("Times New Roman")  
        self.label_dataset.setFont(font)
        self.label_dataset.setObjectName("dataset")
        
        self.datasetpath = QLineEdit(container) 
        self.datasetpath.setGeometry(QRect(10, 40, 730, 30))
        self.datasetpath.setObjectName("datasetpath")
        
        self.loaddataset_btn = QPushButton(container) 
        self.loaddataset_btn.setGeometry(QRect(750, 40, 140, 30))
        self.loaddataset_btn.setObjectName("loaddataset_btn")
        self.loaddataset_btn.clicked.connect(self.getdataset)
        
        self.label_model = QLabel(container) 
        self.label_model.setGeometry(QRect(10, 80, 200, 16)) 
        font = QtGui.QFont()
        font.setFamily("Times New Roman")  
        self.label_model.setFont(font)
        self.label_model.setObjectName("model")
        
        model_opt = [
            "Epochs 3 & Batch Size 16",
            "Epochs 4 & Batch Size 16",
            "Epochs 5 & Batch Size 16",
            "Epochs 6 & Batch Size 16",
            "Epochs 7 & Batch Size 16",
            "Epochs 8 & Batch Size 16",
            "Epochs 3 & Batch Size 32",
            "Epochs 4 & Batch Size 32",
            "Epochs 5 & Batch Size 32",
            "Epochs 6 & Batch Size 32",
            "Epochs 7 & Batch Size 32",
            "Epochs 8 & Batch Size 32",
            "Epochs 3 & Batch Size 50",
            "Epochs 4 & Batch Size 50",
            "Epochs 5 & Batch Size 50",
            "Epochs 6 & Batch Size 50",
            "Epochs 7 & Batch Size 50",
            "Epochs 8 & Batch Size 50",
            ]
        self.model_config = QComboBox(container) 
        self.model_config.setGeometry(QRect(10, 100, 880, 30)) 
        self.model_config.addItems(model_opt)
        
        self.line = QFrame(container) 
        self.line.setGeometry(QRect(10, 130, 880, 20)) 
        self.line.setFrameShape(QFrame.HLine) 
        self.line.setFrameShadow(QFrame.Sunken) 
        self.line.setObjectName("line")
        
        self.label_result = QLabel(container) 
        self.label_result.setGeometry(QRect(10, 160, 200, 16)) 
        font = QtGui.QFont()
        font.setFamily("Times New Roman")  
        self.label_result.setFont(font)
        self.label_result.setObjectName("result")
        
        header = QtGui.QStandardItemModel()
        header.setHorizontalHeaderLabels(['Komentar', 'Label Harapan', 'Label Deteksi'])
        header.setHeaderData(0, Qt.Horizontal, Qt.AlignCenter, Qt.TextAlignmentRole)
        self.result_table = QTableView(container) 
        self.result_table.setGeometry(QRect(10, 180, 880, 250))
        self.result_table.setObjectName("result_table") 
        self.result_table.setModel(header)
        self.result_table.horizontalHeader().setSectionResizeMode(0, QHeaderView.Stretch)
        self.result_table.horizontalHeader().setSectionResizeMode(1, QHeaderView.ResizeToContents)
        self.result_table.horizontalHeader().setSectionResizeMode(2, QHeaderView.ResizeToContents)
        
        self.label_history = QLabel(container) 
        self.label_history.setGeometry(QRect(10, 460, 120, 16)) 
        font = QtGui.QFont()
        font.setFamily("Times New Roman")  
        self.label_history.setFont(font)
        self.label_history.setObjectName("history")
        
        header2 = QtGui.QStandardItemModel()
        header2.setHorizontalHeaderLabels([
            'Konfigurasi', 
            'TP', 
            'FP', 
            'TN', 
            'FN',
            'Akurasi',
            'Presisi',
            'Recall',
            'F-Measure',
            'Waktu Eksekusi' 
            ])
        header2.setHeaderData(0, Qt.Horizontal, Qt.AlignCenter, Qt.TextAlignmentRole)
        self.history_table = QTableView(container) 
        self.history_table.setGeometry(QRect(140, 460, 750, 300))
        self.history_table.setObjectName("history_table") 
        self.history_table.setModel(header2)
        self.history_table.horizontalHeader().setResizeContentsPrecision(-1)
        self.history_table.horizontalHeader().setSectionResizeMode(0, QHeaderView.Stretch)
        self.history_table.horizontalHeader().setSectionResizeMode(1, QHeaderView.ResizeToContents)
        self.history_table.horizontalHeader().setSectionResizeMode(2, QHeaderView.ResizeToContents)
        self.history_table.horizontalHeader().setSectionResizeMode(3, QHeaderView.ResizeToContents)
        self.history_table.horizontalHeader().setSectionResizeMode(4, QHeaderView.ResizeToContents)
        self.history_table.horizontalHeader().setSectionResizeMode(5, QHeaderView.ResizeToContents)
        self.history_table.horizontalHeader().setSectionResizeMode(6, QHeaderView.ResizeToContents)
        self.history_table.horizontalHeader().setSectionResizeMode(7, QHeaderView.ResizeToContents)
        self.history_table.horizontalHeader().setSectionResizeMode(8, QHeaderView.ResizeToContents)
        self.history_table.horizontalHeader().setSectionResizeMode(9, QHeaderView.ResizeToContents)

        self.line2 = QFrame(container) 
        self.line2.setGeometry(QRect(10, 760, 880, 20)) 
        self.line2.setFrameShape(QFrame.HLine) 
        self.line2.setFrameShadow(QFrame.Sunken) 
        self.line2.setObjectName("line2")

        self.runtest_btn = QPushButton(container) 
        self.runtest_btn.setGeometry(QRect(10, 790, 140, 30))
        self.runtest_btn.setObjectName("runtest_btn")
        self.runtest_btn.clicked.connect(
            lambda: self.controller.run_test(
                self.model_config.currentText(), 
                self.datasetpath.text()
                )
            )

        self.reset_btn = QPushButton(container) 
        self.reset_btn.setGeometry(QRect(450, 790, 140, 30))
        self.reset_btn.setObjectName("reset_btn")
        self.reset_btn.clicked.connect(
            lambda: self._resetUI()
            )
        
        self.manual_btn = QPushButton(container) 
        self.manual_btn.setGeometry(QRect(600, 790, 140, 30))
        self.manual_btn.setObjectName("manual_btn")
        self.manual_btn.clicked.connect(
            lambda: self._loadManual()
            )

        self.exit_btn = QPushButton(container) 
        self.exit_btn.setGeometry(QRect(750, 790, 140, 30))
        self.exit_btn.setObjectName("exit_btn")
        self.exit_btn.clicked.connect(
            lambda: sys.exit()
            )

        self.label_dataset.raise_()
        self.datasetpath.raise_()
        self.loaddataset_btn.raise_()
        self.runtest_btn.raise_()
        self.reset_btn.raise_()
        self.line.raise_()
        self.line2.raise_()
        self.label_result.raise_()
        self.result_table.raise_()
        self.label_history.raise_()
        # self.history_table.raise_()
        
        self.retranslateUi()
        
    def retranslateUi(self):
        _translate = QCoreApplication.translate 
        self.setWindowTitle(
            _translate(
                "MainWindow", 
                "Aplikasi Analisis Sentimen Komentar Vaksinasi Covid-19 Menggunakan XLNet"
                )
            ) 
        
        self.label_dataset.setText(_translate("MainWindow", "Lokasi File Dataset"))
        self.loaddataset_btn.setText(_translate("MainWindow", "Buka"))
        self.label_model.setText(_translate("MainWindow", "Konfigurasi Model"))
        self.runtest_btn.setText(_translate("MainWindow", "Jalankan Pengujian"))
        self.reset_btn.setText(_translate("MainWindow", "Reset"))
        self.manual_btn.setText(_translate("MainWindow", "Manual"))
        self.exit_btn.setText(_translate("MainWindow", "Keluar"))
        self.label_result.setText(_translate("MainWindow", "Hasil"))
        self.label_history.setText(_translate("MainWindow", "Riwayat Pengujian"))
        
    def getdataset(self):
        path = QFileDialog.getOpenFileName(self, 'Pilih File', '',
                                         'csv (*.csv)')
        if path != ('', ''):
            self.datasetpath.setText(path[0])
            
            self.controller.getdataset(self.datasetpath.text())
    
    def showresult(self, data):
        headerlabels = ['Komentar', 'Label Harapan', 'Label Deteksi']
        data_model = TableModel(data, headerlabels)
        self.result_table.setModel(data_model)
        self.result_table.verticalHeader().hide()
        self.result_table.setWordWrap(False)
        
    def showhistory(self, history):
        headerlabels = [
            'Konfigurasi', 
            'TP', 
            'FP', 
            'TN', 
            'FN',
            'Akurasi',
            'Presisi',
            'Recall',
            'F-Measure',
            'Waktu Eksekusi'
            ]
        data_model = TableModel(history, headerlabels)
        self.history_table.setModel(data_model)
        self.history_table.verticalHeader().hide()
        self.history_table.setWordWrap(False)
        
    def showerror(self):
        self.msg = QMessageBox(
            QMessageBox.Warning,
            "Warning", 
            "Lokasi File Tidak Sesuai! Harus berupa file .csv "
            )

    def _resetUI(self):
        self.controller.history = []
        self._setUI()
    
    def _loadManual(self):
        webbrowser.open_new("Manual.pdf")
        pass