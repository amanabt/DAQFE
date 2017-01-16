#! /bin/env python3

import sys
from PyQt5.QtWidgets import QApplication, QWidget, QMainWindow, QMenuBar, QAction, \
	QMessageBox
from PyQt5.QtGui import QIcon
import QWinThumbnailToolBar
#from PyQt5.QtCore import QString

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
		self.statusBar().showMessage ("Welcome to DAQFE")
		menu_bar = self.menuBar()
		mFile = menu_bar.addMenu ("&File")
		Fnew = QAction ("New", self)
		Fnew.triggered.connect (self.start_new)
		mFile.addAction (Fnew)
		
		mTools = menu_bar.addMenu ("&Tools")
		
		mHelp = menu_bar.addMenu ("&Help")
		self.Habout = QAction ("About", self)
		self.Habout.triggered.connect (self.start_about)
		mHelp.addAction (self.Habout)
		self.show()
		
	def start_new (self) :
		print ("New Menu Selected")
		
	def start_about (self) :
		string =  ("\
DAQFE - Data Acquisition Front End \n\n \
(c) 2016 Aman Abhishek Tiwari \n\n \
http://github.com/amanabt/DAQFE \n\n \
Licence: MIT Licence")
		about_box = QMessageBox (self)
		about_box.setText (string)
		about_box.setIcon (QMessageBox.Information)
		about_box.exec()
		#about_box = QHelpContentWidget (self)
		

if __name__ == '__main__':
	app = QApplication (sys.argv)
	ex = App()
	sys.exit (app.exec_())
