import sys
import numpy as np
import math, cmath
from itertools import permutations
from PyQt4 import QtCore, QtGui, uic

qtCreatorFile = "TheJuliaGenerator.ui" # Enter file here.
Ui_MainWindow, QtBaseClass = uic.loadUiType(qtCreatorFile)

class JuliaGenerator(QtGui.QMainWindow, Ui_MainWindow):

	####BUTTON METHODS###
	
	#generate: method of btnGenSet. Generates the julia set for the chosen function and displays the image on screen (label 'view'). 
	def generate(self):
		image = self.julia_grid(500,500)	##width of the label view
		QtGui.QApplication.processEvents()
		self.display_image(image)		

	#saveImage: method of btnSaveImage. Creates an image at the specified resolution to save 
	def saveImage(self):
		x = str(self.resX.text())
		y = str(self.resY.text())
		if(not x.isdigit() or not y.isdigit()):
			alert=QtGui.QMessageBox()
			alert.setText("That's not a number!")
			alert.exec_()
		elif((int(x) > 2000) or (int(y) > 2000)):
			alert=QtGui.QMessageBox()
			alert.setText("That's too big, you're gonna crash the program!")
			alert.exec_()
		else:
			image = self.julia_grid(int(x),int(y))		
			try:
				fileName = QtGui.QFileDialog.getSaveFileName(self, "Save Image","","Images (*.jpg *.png *.xpm)")
				image.save(fileName)
			except: 
				pass
	
	#saveTxt: Saves the text of the function as it would appear in a calculator or wolfram alpha to a txt file
	def saveTxt(self):
		fstring = self.getFunc()
		try:
			fileName = QtGui.QFileDialog.getSaveFileName(self, "Save Function","",".txt")
			save = open(fileName, "w+")
			save.write(fstring)
			save.close()
		except: 
			pass

	####END BUTTON METHODS###
	
	###FUNCTION METHODS###

	#chooseFunc: returns the current function the user combobox is set to. 
	#Special functions return codes for handling by julia in math methods
	def chooseFunc(self):
		f = self.cbFunction.currentIndex()
		if(f==0):
			return None
		elif(f==1):
			return cmath.sin
		elif(f==2):
			return cmath.cos
		elif(f==3):
			return cmath.tan
		elif(f==4):
			return cmath.exp
		elif(f==5):
			return "cmath.exp^2"
		elif(f==6):
			return "cmath.exp-"
		elif(f==7):
			return "cmath.exp-^2"
		elif(f==8):
			return cmath.log
		elif(f==9):
			return cmath.sinh
		elif(f==10):
			return cmath.cosh
		elif(f==11):
			return cmath.tanh

		
	#getFunc: returns the format for the function's text output
	#example: f(z)=1*z^2+(0.285+0.01i)
	def getFunc(self):
		return ("f(z)="+self.sbQ.cleanText()+\
			str(self.cbFunction.currentText())+"^"+self.sbN.cleanText() +\
			"+("+self.sbRealC.cleanText()+"+"+self.sbImC.cleanText()+"i)")
		
	#updateFunc: updates the label displaying the function
	def updateFunc(self):
		fstring = self.getFunc()
		self.lblTxt.setText(fstring)
		
	###END FUNCTION METHODS###	
		
	###MATH METHODS###
	#returns an image (QImage) made from a NxM grid 
	#with each point iterated through the generator function. 
	#N	the horizontal pixel width. 
	#M	the vertical pixel width. 

	#The progress of this method is tracked by self.progressBar
	def julia_grid(self,N,M):
		r = self.sbRange.value()
		horiz = -self.sbHoriz.value()
		vert = self.sbVert.value()
		p=0
		x = np.linspace(-r+horiz, r+horiz, N)
		y = np.linspace(-r+vert, r+vert, M)
		X, Y = np.meshgrid(x, y)
		z = np.empty([N,N])
		image = QtGui.QImage(N-1, N-1, QtGui.QImage.Format_RGB32) 
		re = self.sbRealC.value()
		im = self.sbImC.value()
		c = re+im*1j  #complex seed, example 0.285+0.01i   -0.4+0.6i
		for ix in range(0, N-1):
			QtGui.QApplication.processEvents()
			self.progressBar.setValue(round(float(ix)/float(N)*100))
			for iy in range(0, N-1):
				inx = x[ix]
				iny = y[iy]
				inz = inx + iny*1j
				out = int(self.julia(inz, c, 360,self.getExponent()))
				mults=self.getColorScheme()
				pix = QtGui.QColor(out % mults[0][0]*mults[0][1],\
					out% mults[1][0]*mults[1][1] ,\
					out% mults[2][0]*mults[2][1])				
				
				image.setPixel(ix, iy, pix.rgb())
				
		return image
		
	#julia: the generator function for the julia set 
	#Takes a point f, a complex seed c, exponent ex, and maximum maxi 
	#such that each successive value of f is func(f)^ex + c 
	#where func is the function the user chose until f diverges (i.e. f >>> maxi). 
	#returns ic, the number of times the function can act on itself without 
	#going towards infinity
	#see https://rosettacode.org/wiki/Julia_set#Python
	def julia(self,f, c, maxi, ex):
		ic = 0
		func = self.chooseFunc()
		while (ic<maxi):
			if(abs(f) > 2):
				break
			if(func == None):
				f = pow(f,ex) +c
			elif(func == "cmath.exp^2"):
				f = pow(cmath.exp(f*f),ex) +c
			elif(func == "cmath.exp-"):
				f = pow(cmath.exp(-f),ex) +c
			elif(func == "cmath.exp-^2"):
				f = pow(cmath.exp(-f*f),ex) + c
			else:
				f = pow(func(f),ex) + c
			ic+=1
		return ic

	#getExponent: returns the exponent chosen by the user (i.e. the value in the textbox)
	def getExponent(self):
		return self.sbN.value()

	###END MATH METHODS###


	###IMAGE METHODS###

	#getColorScheme: returns the multipliers to create an RGB color scheme
	def getColorScheme(self):
		pairs = [(8,32), (32,8), (16,16), (4,64),(64,4)]
		p=list(permutations(pairs,3))
		p.append(((16,16),(16,16),(16,16)))
		return p[self.cbColor.currentIndex()]

	#display_image: displays a Qimage img on label view	
	def display_image(self, img):
		pmap = QtGui.QPixmap.fromImage(img)
		self.view.setPixmap(pmap)
		
	
	#adds the number of schemes (61 total themes) to the dropdown menu cbColor
	def populateColors(self):
		for i in range(61):
			self.cbColor.addItem("Scheme %d" % (i+1) )
	
	###END IMAGE METHODS###

	####STARTUP####	
	#Typical function to set up the interface
	#basically just edited this: 
	#http://pythonforengineers.com/your-first-gui-app-with-python-and-pyqt/
		
	def __init__(self):
		QtGui.QMainWindow.__init__(self)
		Ui_MainWindow.__init__(self)
		self.setupUi(self)
		self.populateColors()
		self.btnGenSet.clicked.connect(self.generate)
		self.btnSaveImage.clicked.connect(self.saveImage)
		self.btnSaveTxt.clicked.connect(self.saveTxt)
		

#Typical main function, see above link
if __name__ == "__main__":
	app = QtGui.QApplication(sys.argv)
	window = JuliaGenerator()
	window.show()
	#The timer is used for making the labels change when you change the text
	timer = QtCore.QTimer()  # set up your QTimer
	timer.timeout.connect(window.updateFunc)  # connect it to your update function
	timer.start(10)  # set it to timeout in ms
	sys.exit(app.exec_())
	





