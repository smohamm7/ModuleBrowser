# Form implementation generated from reading ui file '.\main.ui'
#
# Created by: PyQt6 UI code generator 6.1.0
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(985, 888)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.frame = QtWidgets.QFrame(self.centralwidget)
        self.frame.setGeometry(QtCore.QRect(0, 0, 981, 98))
        self.frame.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.frame.setObjectName("frame")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.frame)
        self.verticalLayout.setObjectName("verticalLayout")
        self.comboModulesPath = QtWidgets.QComboBox(self.frame)
        self.comboModulesPath.setObjectName("comboModulesPath")
        self.verticalLayout.addWidget(self.comboModulesPath)
        self.comboModules = QtWidgets.QComboBox(self.frame)
        self.comboModules.setObjectName("comboModules")
        self.verticalLayout.addWidget(self.comboModules)
        self.labelVersion = QtWidgets.QLabel(self.centralwidget)
        self.labelVersion.setGeometry(QtCore.QRect(948, 870, 31, 20))
        self.labelVersion.setObjectName("labelVersion")
        self.labelStatus = QtWidgets.QLabel(self.centralwidget)
        self.labelStatus.setGeometry(QtCore.QRect(10, 870, 901, 16))
        self.labelStatus.setText("")
        self.labelStatus.setObjectName("labelStatus")
        self.widget = QtWidgets.QWidget(self.centralwidget)
        self.widget.setGeometry(QtCore.QRect(10, 90, 971, 781))
        self.widget.setObjectName("widget")
        self.gridLayout = QtWidgets.QGridLayout(self.widget)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")
        self.frameClass = QtWidgets.QFrame(self.widget)
        self.frameClass.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.frameClass.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.frameClass.setObjectName("frameClass")
        self.labelSelectedClasses = QtWidgets.QLabel(self.frameClass)
        self.labelSelectedClasses.setGeometry(QtCore.QRect(0, 20, 321, 16))
        self.labelSelectedClasses.setObjectName("labelSelectedClasses")
        self.listWidgetClasses = QtWidgets.QListWidget(self.frameClass)
        self.listWidgetClasses.setGeometry(QtCore.QRect(0, 40, 321, 741))
        self.listWidgetClasses.setObjectName("listWidgetClasses")
        self.searchClass = QtWidgets.QLineEdit(self.frameClass)
        self.searchClass.setGeometry(QtCore.QRect(0, 0, 321, 22))
        self.searchClass.setObjectName("searchClass")
        self.gridLayout.addWidget(self.frameClass, 0, 0, 1, 1)
        self.frameMember = QtWidgets.QFrame(self.widget)
        self.frameMember.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.frameMember.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.frameMember.setObjectName("frameMember")
        self.labelSelectedMemebers = QtWidgets.QLabel(self.frameMember)
        self.labelSelectedMemebers.setGeometry(QtCore.QRect(10, 20, 311, 16))
        self.labelSelectedMemebers.setObjectName("labelSelectedMemebers")
        self.listWidgetMemebers = QtWidgets.QListWidget(self.frameMember)
        self.listWidgetMemebers.setGeometry(QtCore.QRect(0, 40, 321, 741))
        self.listWidgetMemebers.setObjectName("listWidgetMemebers")
        self.searchMember = QtWidgets.QLineEdit(self.frameMember)
        self.searchMember.setGeometry(QtCore.QRect(0, 0, 321, 22))
        self.searchMember.setObjectName("searchMember")
        self.gridLayout.addWidget(self.frameMember, 0, 1, 1, 1)
        self.frameHelp = QtWidgets.QFrame(self.widget)
        self.frameHelp.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.frameHelp.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.frameHelp.setObjectName("frameHelp")
        self.labelHelp = QtWidgets.QLabel(self.frameHelp)
        self.labelHelp.setGeometry(QtCore.QRect(0, 20, 321, 16))
        self.labelHelp.setObjectName("labelHelp")
        self.textEditHelp = QtWidgets.QTextEdit(self.frameHelp)
        self.textEditHelp.setGeometry(QtCore.QRect(0, 40, 321, 741))
        self.textEditHelp.setReadOnly(True)
        self.textEditHelp.setObjectName("textEditHelp")
        self.searchHelp = QtWidgets.QLineEdit(self.frameHelp)
        self.searchHelp.setGeometry(QtCore.QRect(0, 0, 321, 22))
        self.searchHelp.setObjectName("searchHelp")
        self.gridLayout.addWidget(self.frameHelp, 0, 2, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.comboModulesPath.setToolTip(_translate("MainWindow", "Paths Of Modules Detected.. "))
        self.comboModulesPath.setPlaceholderText(_translate("MainWindow", "Paths of Modules"))
        self.comboModules.setStatusTip(_translate("MainWindow", "MODULE DETECTED.."))
        self.labelVersion.setText(_translate("MainWindow", "V2.0"))
        self.labelSelectedClasses.setText(_translate("MainWindow", "Selected Class: "))
        self.labelSelectedMemebers.setText(_translate("MainWindow", "Selected Member: "))
        self.labelHelp.setText(_translate("MainWindow", "Help Information:"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec())