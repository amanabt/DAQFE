#! /bin/env python3

import sys
from PyQt5.QtWidgets import QApplication, QWidget, QMainWindow, QMenuBar, QAction
from PyQt5.QtGui import QIcon


class App (QMainWindow):
	def __init__ (self):
		super().__init__()
		self.title = "DAQFE"
		self.width = 800
		self.height = 600
		self.wPosition = [10,10]
		self.initUI()
		
	def initUI (self):
		self.setWindowTitle(self.title)
		self.setGeometry (self.wPosition [0], self.wPosition [1], self.width, self.height)
		self.show()
		self.statusBar().showMessage ("Welcome to DAQFE")
		main_menu = self.menuBar()
		mFile = main_menu.addMenu ("&File")
		start_new = QAction ("New", self)
		start_new.triggered.connect (self.start_new)
		mFile.addAction (start_new)
	
	def start_new (self) :
		print ("New Menu Selected")

if __name__ == '__main__':
	app = QApplication(sys.argv)
	ex = App()
	sys.exit (app.exec_())
