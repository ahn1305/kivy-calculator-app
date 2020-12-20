import kivy
kivy.require("1.9.0")

from kivy.app import App ## app
from kivy.uix.gridlayout import GridLayout #Grid layout
from kivy.loader import Loader
from kivy.uix.image import Image


class CalcGridLayout(GridLayout):
	def calculate(self,calculation):
		if calculation:
			try:
				self.display.text = str(eval(calculation))
			except Exception:
				self.display.text = "Error"

class CalculatorApp(App):
	def build(self):
		self.title = "Pycalculator"
		return CalcGridLayout()

calcApp = CalculatorApp()
calcApp.run() 

##Recommended 256x256 or 1024x1024? for GNU/Linux and Mac OSX 32x32 for Windows7 or less. <= 256x256 for windows 8 256x256 does work (on Windows 8 at least), but is scaled down and doesn’t look as good as a 32x32 icon.
##
