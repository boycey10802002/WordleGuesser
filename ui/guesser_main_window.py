# Form implementation generated from reading ui file 'D:\PythonGamePrototypes\WordleGuesser\ui\guesser_main_window.ui'
#
# Created by: PyQt6 UI code generator 6.4.2
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(466, 600)
        self.centralwidget = QtWidgets.QWidget(parent=MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.cbx_letter_01 = QtWidgets.QComboBox(parent=self.centralwidget)
        self.cbx_letter_01.setObjectName("cbx_letter_01")
        self.verticalLayout.addWidget(self.cbx_letter_01)
        self.btn_letter_01 = QtWidgets.QCheckBox(parent=self.centralwidget)
        self.btn_letter_01.setTristate(True)
        self.btn_letter_01.setObjectName("btn_letter_01")
        self.verticalLayout.addWidget(self.btn_letter_01)
        self.horizontalLayout_2.addLayout(self.verticalLayout)
        self.verticalLayout_3 = QtWidgets.QVBoxLayout()
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.cbx_letter_02 = QtWidgets.QComboBox(parent=self.centralwidget)
        self.cbx_letter_02.setObjectName("cbx_letter_02")
        self.verticalLayout_3.addWidget(self.cbx_letter_02)
        self.btn_letter_02 = QtWidgets.QCheckBox(parent=self.centralwidget)
        self.btn_letter_02.setStyleSheet("")
        self.btn_letter_02.setTristate(True)
        self.btn_letter_02.setObjectName("btn_letter_02")
        self.verticalLayout_3.addWidget(self.btn_letter_02)
        self.horizontalLayout_2.addLayout(self.verticalLayout_3)
        self.verticalLayout_4 = QtWidgets.QVBoxLayout()
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.cbx_letter_03 = QtWidgets.QComboBox(parent=self.centralwidget)
        self.cbx_letter_03.setObjectName("cbx_letter_03")
        self.verticalLayout_4.addWidget(self.cbx_letter_03)
        self.btn_letter_03 = QtWidgets.QCheckBox(parent=self.centralwidget)
        self.btn_letter_03.setTristate(True)
        self.btn_letter_03.setObjectName("btn_letter_03")
        self.verticalLayout_4.addWidget(self.btn_letter_03)
        self.horizontalLayout_2.addLayout(self.verticalLayout_4)
        self.verticalLayout_5 = QtWidgets.QVBoxLayout()
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.cbx_letter_04 = QtWidgets.QComboBox(parent=self.centralwidget)
        self.cbx_letter_04.setObjectName("cbx_letter_04")
        self.verticalLayout_5.addWidget(self.cbx_letter_04)
        self.btn_letter_04 = QtWidgets.QCheckBox(parent=self.centralwidget)
        self.btn_letter_04.setTristate(True)
        self.btn_letter_04.setObjectName("btn_letter_04")
        self.verticalLayout_5.addWidget(self.btn_letter_04)
        self.horizontalLayout_2.addLayout(self.verticalLayout_5)
        self.verticalLayout_6 = QtWidgets.QVBoxLayout()
        self.verticalLayout_6.setObjectName("verticalLayout_6")
        self.cbx_letter_05 = QtWidgets.QComboBox(parent=self.centralwidget)
        self.cbx_letter_05.setObjectName("cbx_letter_05")
        self.verticalLayout_6.addWidget(self.cbx_letter_05)
        self.btn_letter_05 = QtWidgets.QCheckBox(parent=self.centralwidget)
        self.btn_letter_05.setTristate(True)
        self.btn_letter_05.setObjectName("btn_letter_05")
        self.verticalLayout_6.addWidget(self.btn_letter_05)
        self.horizontalLayout_2.addLayout(self.verticalLayout_6)
        self.verticalLayout_2.addLayout(self.horizontalLayout_2)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.txt_Suggestions = QtWidgets.QTextEdit(parent=self.centralwidget)
        self.txt_Suggestions.setObjectName("txt_Suggestions")
        self.horizontalLayout.addWidget(self.txt_Suggestions)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        self.verticalLayout_2.addLayout(self.horizontalLayout)
        spacerItem1 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Policy.Minimum, QtWidgets.QSizePolicy.Policy.Expanding)
        self.verticalLayout_2.addItem(spacerItem1)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(parent=MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 466, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(parent=MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.btn_letter_01.setText(_translate("MainWindow", "_"))
        self.btn_letter_02.setText(_translate("MainWindow", "_"))
        self.btn_letter_03.setText(_translate("MainWindow", "_"))
        self.btn_letter_04.setText(_translate("MainWindow", "_"))
        self.btn_letter_05.setText(_translate("MainWindow", "_"))
