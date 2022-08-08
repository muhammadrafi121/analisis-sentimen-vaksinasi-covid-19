# -*- coding: utf-8 -*-
"""
Created on Tue Jun 28 05:18:35 2022

@author: Acer
"""

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
    def __init__(self, controller):
        super().__init__()
        
        self.controller = controller        
        self._setUI()
        
    def _setUI(self):
        self.setObjectName("MainWindow")
        self.resize(900, 800)
        
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
        self.datasetpath.setGeometry(QRect(10, 40, 770, 30))
        self.datasetpath.setObjectName("datasetpath")
        
        self.loaddataset_btn = QPushButton(container) 
        self.loaddataset_btn.setGeometry(QRect(790, 40, 100, 30))
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
            "Epochs 3 & Batch Size 32",
            "Epochs 4 & Batch Size 32",
            "Epochs 3 & Batch Size 50",
            "Epochs 4 & Batch Size 50",
            ]
        self.model_config = QComboBox(container) 
        self.model_config.setGeometry(QRect(10, 100, 770, 30)) 
        # self.model_config.lineEdit().setAlignment(Qt.AlignCenter)
        self.model_config.addItems(model_opt)
        
        self.runtest_btn = QPushButton(container) 
        self.runtest_btn.setGeometry(QRect(790, 100, 100, 30))
        self.runtest_btn.setObjectName("runtest_btn")
        self.runtest_btn.clicked.connect(
            lambda: self.controller.run_test(
                self.model_config.currentText(), 
                self.datasetpath.text()
                )
            )
        
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
        header.setHorizontalHeaderLabels(['Comments', 'Expected Label', 'Detected Label'])
        header.setHeaderData(0, Qt.Horizontal, Qt.AlignCenter, Qt.TextAlignmentRole)
        self.result_table = QTableView(container) 
        self.result_table.setGeometry(QRect(10, 180, 880, 250))
        self.result_table.setObjectName("result_table") 
        self.result_table.setModel(header)
        self.result_table.horizontalHeader().setSectionResizeMode(0, QHeaderView.Stretch)
        self.result_table.horizontalHeader().setSectionResizeMode(1, QHeaderView.ResizeToContents)
        self.result_table.horizontalHeader().setSectionResizeMode(2, QHeaderView.ResizeToContents)
        
        self.label_history = QLabel(container) 
        self.label_history.setGeometry(QRect(10, 460, 100, 16)) 
        font = QtGui.QFont()
        font.setFamily("Times New Roman")  
        self.label_history.setFont(font)
        self.label_history.setObjectName("history")
        
        header2 = QtGui.QStandardItemModel()
        header2.setHorizontalHeaderLabels([
            'Configuration', 
            'TP', 
            'FP', 
            'TN', 
            'FN',
            'Accuracy',
            'Precision',
            'Recall',
            'F-Measure',
            'Execution Time'
            ])
        header2.setHeaderData(0, Qt.Horizontal, Qt.AlignCenter, Qt.TextAlignmentRole)
        self.history_table = QTableView(container) 
        self.history_table.setGeometry(QRect(90, 460, 800, 300))
        self.history_table.setObjectName("history_table") 
        self.history_table.setModel(header2)
        self.history_table.horizontalHeader().setSectionResizeMode(0, QHeaderView.Stretch)
        self.history_table.horizontalHeader().setSectionResizeMode(1, QHeaderView.ResizeToContents)
        self.history_table.horizontalHeader().setSectionResizeMode(2, QHeaderView.ResizeToContents)
        self.history_table.horizontalHeader().setSectionResizeMode(3, QHeaderView.ResizeToContents)
        self.history_table.horizontalHeader().setSectionResizeMode(4, QHeaderView.ResizeToContents)
        self.history_table.horizontalHeader().setSectionResizeMode(5, QHeaderView.ResizeToContents)
        self.history_table.horizontalHeader().setSectionResizeMode(6, QHeaderView.ResizeToContents)
        self.history_table.horizontalHeader().setSectionResizeMode(7, QHeaderView.ResizeToContents)
        self.history_table.horizontalHeader().setSectionResizeMode(8, QHeaderView.ResizeToContents)

        self.label_dataset.raise_()
        self.datasetpath.raise_()
        self.loaddataset_btn.raise_()
        self.runtest_btn.raise_()
        self.line.raise_()
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
                "Analisis Sentimen Komentar Vaksinasi Covid-19 di Instagram Menggunakan Deep Learning XLNet"
                )
            ) 
        
        self.label_dataset.setText(_translate("MainWindow", "Dataset File Path"))
        self.loaddataset_btn.setText(_translate("MainWindow", "Load File .csv"))
        self.label_model.setText(_translate("MainWindow", "Model Configuration"))
        self.runtest_btn.setText(_translate("MainWindow", "Run the Test"))
        self.label_result.setText(_translate("MainWindow", "Results"))
        self.label_history.setText(_translate("MainWindow", "Test History"))
        
    def getdataset(self):
        path = QFileDialog.getOpenFileName(self, 'Open a file', '',
                                         'csv (*.csv)')
        if path != ('', ''):
            self.datasetpath.setText(path[0])
            
            self.controller.getdataset(self.datasetpath.text())
    
    def showresult(self, data):
        headerlabels = ['Comments', 'Expected Label', 'Detected Label']
        data_model = TableModel(data, headerlabels)
        self.result_table.setModel(data_model)
        self.result_table.setWordWrap(False)
        
    def showhistory(self, history):
        headerlabels = [
            'Configuration', 
            'TP', 
            'FP', 
            'TN', 
            'FN',
            'Accuracy',
            'Precision',
            'Recall',
            'F-Measure',
            'Execution Time'
            ]
        data_model = TableModel(history, headerlabels)
        self.history_table.setModel(data_model)
        self.history_table.verticalHeader().hide()
        self.history_table.setWordWrap(False)
        
    def showerror(self):
        self.msg = QMessageBox(
            QMessageBox.Warning,
            "Warning", 
            "Invalid file path! Needs to be a .csv file"
            )
    
    def main(self):
        app = QApplication([])
        self.show()
        
        app.exec()