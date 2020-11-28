import gui.widget.widget as wid
import gui.misc.event as ev
import gui.misc.color as color

class Aligment(Enum) :
	StartAlign
	EndAlign
	CenterAlign


class Text(wid.Widget):

	def __init__(self,txt = "", font_size = 40.0):
		super().__init__()
		self.__text = txt
		self.__font_size = 40.0
		self.__color = color.get_black()

		self.__xAlign = Aligment.CenterAlign
		self.__yAlign = Aligment.CenterAlign


	def update(self, window, page) :
		super().update(window,page)

	def draw(self, paint, window, page) :
		super().draw(paint,window,page)

		paint.set_paint_color(self.__color)
		paint.set_font_size(self.__font_size)


		xText = 0.0
		yText = 0.0

		textW = paint.text_bound(0,0,self.__text).w
		if self.__xAlign == Aligment.StartAlign:
			xText = self.get_x()
		elif self.__xAlign == Aligment.CenterAlign:
			xText = self.get_x() + (self.get_width() - textW) / 2.0
		elif self.__xAlign == Aligment.EndAlign:
			xText = self.get_x() + self.get_width()+ textW



		if self.__xAlign == Aligment.StartAlign:
			yText = self.get_y()
		elif self.__xAlign == Aligment.CenterAlign:
			yText = self.get_y() + self.get_height() / 2.0 +self.__font_size / 2
		elif self.__xAlign == Aligment.EndAlign:
			yText = self.get_y() + self.__font_size

		paint.draw_text(xText,yText,self.__text)

	def on_event(self, event, window, page):
		super().on_event(event, window, page)

	def set_font_size(self, size):
		self.__font_size = size

	def get_font_size(self):
		return self.__font_size

	def  set_color(self, scolor):
		self.__color = scolor

	def get_color(self):
		return self.__color

	def set_align(self, x, y = Aligment.CenterAlign):
		self.__xAlign = x
		self.__yAlign = y

	def get_x_align(self):
		return self.__xAlign

	def get_y_align(self):
		return self.__yAlign
