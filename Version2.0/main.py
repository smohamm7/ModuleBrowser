import sys
import pkgutil as pkg
# pip install PyQt5 to install the library
# from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QLineEdit, QTextEdit, QListWidget, QComboBox, QVBoxLayout, QHBoxLayout
from PyQt6.QtWidgets import QMainWindow, QApplication, QWidget, QLabel, QLineEdit, QTextEdit, QListWidget, QComboBox, QVBoxLayout, QHBoxLayout
# from PyQt5.QtCore import QStringListModel, QFile, QTextStream, Qt
from PyQt6.QtCore import QStringListModel, QFile, QTextStream, Qt
# from PyQt5.QtGui import QIcon
from PyQt6 import QtCore
from ui_main import Ui_MainWindow
# import packages to make the information available
import json
import sqlite3
import asyncio
# libPath = 'C:\\Program Files (x86)\\Python3.9.10\\lib\\site-packages'
libPath = ['C:\\Program Files (x86)\\Python3.9.10\\lib',
		   'C:\\Users\\sa.mohammad.CORP\\source\\repos\\NavigateLibraries\\Version2.0',
		   'C:\\Program Files (x86)\\Python3.9.10\\DLLs',
		   'C:\\Program Files (x86)\\Python3.9.10\\lib\\site-packages'
			]
print ("Outside Loop Path value is: ",libPath, type(libPath))
class PythonNavigator(QMainWindow):
    
	def __init__(self):
		QMainWindow.__init__(self)
		self.ui = Ui_MainWindow()
		self.ui.setupUi(self)

		self.displayModulePath()
		# available_modules = sorted(tuple(module_item.name for module_item in pkg.iter_modules() if module_item.module_finder.path == libPath and module_item.ispkg))
		# print ("Available Modules are: ", available_modules)
		# # combobox widget
		
		# self.ui.comboModules.addItems(available_modules)
		
		self.ui.comboModulesPath.currentIndexChanged.connect(self.displayModules)
		self.ui.comboModules.currentIndexChanged.connect(self.updateModuleList)
		
		self.ui.searchClass.textChanged.connect(self.filter_items_class)
		self.ui.searchMember.textChanged.connect(self.filter_items_members)

		self.ui.listWidgetClasses.itemSelectionChanged.connect(self.updateClassList)
		self.ui.listWidgetClasses.itemSelectionChanged.connect(lambda : self.displayHelper('class'))

		self.ui.listWidgetMemebers.itemSelectionChanged.connect(self.updateMemeberlabel)
		self.ui.listWidgetMemebers.itemSelectionChanged.connect(lambda : self.displayHelper('member'))


		self.updateModuleList()
	def displayModulePath(self):
		# moduleList = list(pkg.iter_modules())
		# seen = set()
		# uniq = []
		# pathList = []
		# for i in moduleList:
		# 	pathList.append(i[0])

		# for x in pathList:
		# 	if x not in seen:
		# 		uniq.append(x)
		# 		seen.add(x)

		# uniqStr = []
		# for i in uniq:
		# 	i = str(i)
		# 	uniqStr.append(i)

		# for i in uniqStr:
		# 	actualPath = i[12:-2]
		# 	# print ("Before raw data:",actualPath, type(actualPath) )
		# 	# actualPath = r"{}".format(actualPath)
		# 	# print ("After raw data:",actualPath, type(actualPath) )
		# 	self.ui.comboModulesPath.addItem(actualPath)
		self.ui.comboModulesPath.addItems(libPath)
	def displayModules(self):
		modPath = self.ui.comboModulesPath.currentText()
		print ("Selected path is : ",modPath)
		display_modules = self.available_modules(modPath)
		# available_modules = sorted(tuple(module_item.name for module_item in pkg.iter_modules() if module_item.module_finder.path == libPathLocal and module_item.ispkg))
		# print ("Available Modules are: ",available_modules)
		self.ui.comboModules.addItems(display_modules)
	def available_modules(self, modulePath):
		available_modules = sorted(tuple(module_item.name for module_item in pkg.iter_modules() if module_item.module_finder.path == modulePath and module_item.ispkg))
		print ("available_modules output: ",available_modules)
		if available_modules == []:
			self.ui.comboModules.setCurrentText("No Modules found.. ")
		return available_modules

	
	

	def displayHelper(self, by_type: str):
		try:
			if by_type == 'class':
				class_name = self.ui.listWidgetClasses.currentItem().text()
				obj = getattr(self.module_object, class_name)
			elif by_type == 'member':
				class_name = self.ui.listWidgetClasses.currentItem().text()
				memeber_name = self.ui.listWidgetMemebers.currentItem().text()
				obj = getattr(getattr(self.module_object, class_name), memeber_name)
			else:
				self.ui.labelStatus.setText('No information available')
				return
			help_text = obj.__doc__
			self.ui.textEditHelp.setText(help_text)
			if help_text == "":
				self.ui.textEditHelp.setText("No information.. ")
		except Exception as e:
			self.ui.labelStatus.setText(str(e))

	def updateMemeberlabel(self):
		try:
			member_name = self.ui.listWidgetMemebers.currentItem().text()
			self.ui.labelSelectedMemebers.setText('Selected Member: {0}'.format(member_name))
		except Exception as e:
			self.ui.labelStatus.setText(str(e))

	def updateClassList(self):
		self.ui.listWidgetMemebers.clear()

		class_name = self.ui.listWidgetClasses.currentItem().text()

		try:
			obj = getattr(self.module_object, class_name)			
		except AttributeError as e:
			self.ui.labelStatus.setText(str(e))
			return 

		self.ui.listWidgetMemebers.addItems(dir(obj))
		self.ui.labelStatus.clear()

		try:
			self.ui.labelSelectedClasses.setText('Selected Class: {0}'.format(class_name))
		except Exception as e:
			self.status.setText(str(e))
		
	def updateModuleList(self):
		module_name = self.ui.comboModules.currentText()
		self.module_object = sys.modules.get(module_name)
		self.reset_fields()

		if self.module_object is None:
			self.ui.labelStatus.setText('Information is not available')
			return

		module_dir = dir(self.module_object)

		self.model = QStringListModel()
		self.model.setStringList(module_dir)

		self.ui.listWidgetClasses.addItems(module_dir)

		self.ui.labelStatus.clear()

	def reset_fields(self):
		self.ui.listWidgetClasses.clear()
		self.ui.listWidgetMemebers.clear()
		self.ui.labelSelectedClasses.setText('Selected Class: ')
		self.ui.labelSelectedMemebers.setText('Selected Member: ')

	def filter_items_class(self):#WHILE SEARCHING SHOW ONLY SEARCH FIELD IN listWidgetClasses.
		filtered_text = str(self.ui.searchClass.text()).lower()

		if self.model:
			for row in range(self.model.rowCount()):
				if filtered_text in str(self.model.index(row).data()).lower():
					self.ui.listWidgetClasses.setRowHidden(row, False)
				else:
					self.ui.listWidgetClasses.setRowHidden(row, True)
	def filter_items_members(self):#WHILE SEARCHING SHOW ONLY SEARCH FIELD IN listWidgetClasses.
		filtered_text = str(self.ui.searchMember.text()).lower()

		if self.model:
			for row in range(self.model.rowCount()):
				if filtered_text in str(self.model.index(row).data()).lower():
					self.ui.listWidgetMemebers.setRowHidden(row, False)
				else:
					self.ui.listWidgetMemebers.setRowHidden(row, True)
if __name__ == '__main__':
	app = QApplication(sys.argv)


	# css_file = QtCore.QFile('light_theme.css')
	# css_file.open(QFile.readAll)
	# # css_file.readAll()
	# stream = QTextStream(css_file)

	pyNavigator = PythonNavigator()
	# pyNavigator.setStyleSheet(stream.readAll())
	pyNavigator.show()

	try:
		sys.exit(app.exec())
	except SystemExit:
		print('Closing Window...')