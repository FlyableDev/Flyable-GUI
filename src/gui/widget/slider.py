import gui.widget.widget as wid
import gui.misc.event as ev
import gui.misc.color as color

class Slider(wid.Widget):

	def __init__(self,min = 0.0,max = 100.0):
		super().__init__()
		self.__min_value = min
		self.__max_value = max
		self.__value = 0.0
		self.__horizontal = True

		self.__circle_x = 0.0
		self.__circle_y = 0.0
		self.__circle_radius = 0.0

		self.__is_sliding = False


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
			self.__circle_radius = realH * 0.45
			paint.draw_rounded_rect(self.get_x(),self.get_y(),self.get_width(),realH,20.0)

			self.__circle_x = self.get_x() + (self.get_width() - self.__circle_radius * 2) * valueRatio + self.__circle_radius
			self.__circle_y = self.get_y() + self.get_height() / 2

			paint.set_paint_color(color.get_white())
			paint.draw_circle(self.__circle_x, self.__circle_y, self.__circle_radius)
		else:
			realW = max(20.0,self.get_width())
			paint.draw_rounded_rect(self.get_x() + self.get_width() / 2 - realW, self.get_y(), realW,self.get_height(),20.0)


	def on_event(self, event, window, page):
		super().on_event(event, window, page)
		if event.get_event_type() == ev.EventType.MouseMotion:
			x = event.get_mouse_x()
			y = event.get_mouse_y()
			diff = self.get_max_value() - self.get_min_value()
			if self.is_sliding():
				if self.is_horizontal():
					oldValue = self.get_value()
					zeroedX = x - self.get_x()
					self.__value = (  ( zeroedX / self.get_width() )* diff) + self.get_min_value()
				else:
					oldValue = self.get_value()
					zeroedY = y - self.get_y()
					self.set_value( (  ( zeroedY / self.get_height() ) *  diff) + self.get_min_value())
		elif event.get_event_type() == ev.EventType.MouseButtonDown:
			if event.get_mouse_button() == ev.MouseButton.LeftButton:
				x = event.get_mouse_x()
				y = event.get_mouse_y()
				if self.collision_circle_pointer(self.__circle_x,self.__circle_y,self.__circle_radius,x,y):
					self.__is_sliding = True
				else:
					self.__is_sliding = False
		elif event.get_event_type() == ev.EventType.MouseButtonUp:
			self.__is_sliding = False


	def set_horizontal(self, hor):
		self.__horizontal = hor

	def is_horizontal(self):
		return self.__horizontal

	def set_value(self, value):
		self.__value = float(value)

	def get_value(self):
		return self.__value

	def is_sliding(self):
		return self.__is_sliding

	def set_min_value(self, min):
		self.__min_value = min

	def get_min_value(self):
		return self.__min_value

	def set_max_value(self,max):
		self.__max_value = max

	def get_max_value(self):
		return self.__max_value

	def collision_circle_pointer(self, circleX, circleY, circleRadius, x, y):
		d2 = (x-circleX)*(x-circleX) + (y-circleY)*(y-circleY)
		if d2 > circleRadius * circleRadius :
			return False
		return True