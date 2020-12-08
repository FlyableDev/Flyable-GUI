import gui.widget.widget as wid
import gui.misc.event as ev
import gui.misc.color as color

class Slider(wid.Widget):

	def __init__(self,min = 0,max = 100):
		super().__init__()
		self.__min_value = min
		self.__max_value = max
		self.__value = 0
		self.__horizontal = True


	def update(self, window, page) :
		super().update(window,page)

	def draw(self, paint, window, page) :
		super().draw(paint,window,page)

		diff = self.__max_value - self.__min_value
		valueRatio = (self.__value - self.__min_value)  / float((self.__min_value - self.__max_value))
		valueRatio = max(0.0,valueRatio)
		valueRatio = min(1.0,valueRatio)


		paint.set_paint_color(color.get_grey())

		if self.is_horizontal():
			realH = max(20.0,self.get_height())
			circleRadius = realH * 0.45
			paint.draw_rounded_rect(self.get_x(),self.get_y(),self.get_width(),realH,20.0)

			circleX = self.get_x() + self.get_width() * valueRatio
			circleY = self.get_y() + self.get_height() / 2

			paint.set_paint_color(color.get_white())
			paint.draw_circle(circleX,circleY,circleRadius)
		else:
			realW = max(20.0,self.get_width())
			paint.draw_rounded_rect(self.get_x() + self.get_width() / 2 - realW, self.get_y(), realW,self.get_height(),20.0)


	def on_event(self, event, window, page):
		super().on_event(event, window, page)


	def set_horizontal(self, hor):
		self.__horizontal = hor

	def is_horizontal(self):
		return self.__horizontal

	def set_value(self, value):
		self.__value = value

	def get_value(self):
		return self.__value


	def set_max_value(self,max):
		self.__max_value = max

	def get_max_value(self):
		return self.__max_value