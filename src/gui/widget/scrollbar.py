import gui.widget.widget
import gui.misc.color
import gui.misc.rect
import gui.misc.event as ev

class ScrollBar(widget.Widget):

	def __init__(self):
		super().__init__()
		self.__current_min_value = 0.0
		self.__current_max_value = 10.0
		self.__range = 10.0
		self.__max_value = 100.0
		self.__pressed = False
		self.__is_sliding = False
		self.__is_horizontal = True

		self.__slider_button_color = color.Color(170,170,170,255)

		self.__selected_bar_rect = rect.Rect()

		self.__initial_mouse_pos = [0.0,0.0]
		self.__initial_click_value = 0.0

		self.__validate_bounce()

	def update(self, window, page):
		super().update(window,page)

	def draw(self, paint, window, page):
		super().draw(paint, window, page)

		h = self.get_height()
		w = self.get_width()
		x = self.get_x()
		y = self.get_y()
		selectionRatio = self.__range / self.__max_value
		paint.set_paint_color(self.__slider_button_color)
		if self.is_horizontal():
			realH = min(20.0,self.get_height())
			paint.draw_rounded_rect(x,y + self.get_height() / 2.0  - realH / 2.0,w,realH, 10.0)
			paint.set_paint_color(color.get_black())
			paint.draw_rounded_rect(x +  ( w *  (self.__current_min_value / self.__max_value)) + 5.0,y + h / 2.0  - realH / 2.0 + 5.0,w * selectionRatio - 10.0,realH - 10.0, 10.0)
			self.__selected_bar_rect.set(x +  ( w *  (self.__current_min_value / self.__max_value)),y + h / 2.0  - realH / 2.0,w * selectionRatio,realH)
		else:
			realW = min(20.0,self.get_width())
			paint.draw_rounded_rect(x + w / 2.0 - realW,y,realW,h, 10.0)
			paint.set_paint_color(color.get_black())
			paint.draw_rounded_rect(x + w / 2.0 - realW + 5.0,y +  ( h *  (self.__current_min_value / self.__max_value)) + 5.0,realW - 10.0,h * selectionRatio - 10.0, 10.0)
			self.__selected_bar_rect.set(x + w / 2.0 - realW,y +  ( h *  (self.__current_min_value / self.__max_value)),realW,h * selectionRatio)

	def on_event(self, event, window, page):
		super().on_event(event, window, page)
		if event.get_event_type() == ev.EventType.MouseMotion:
			x = event.get_mouse_x()
			y = event.get_mouse_y()
			if self.__is_sliding:
				oldValue = self.__current_min_value
				if self.is_horizontal():
					distanceX = x - self.__initial_mouse_pos[0]
					self.set_value(self.__initial_click_value + ( distanceX / self.get_width() ) * self.get_max_value())
					self.__validate_bounce()
				else:
					distanceY = y - self.__initial_mouse_pos[1]
					self.set_value(self.__initial_click_value + ( distanceY / self.get_height() ) * self.__max_value)
					self.__validate_bounce()
		elif event.get_event_type() == ev.EventType.MouseButtonDown:
			if event.get_mouse_button() == ev.MouseButton.LeftButton:
				x = event.get_mouse_x()
				y = event.get_mouse_y()
				if self.__selected_bar_rect.is_inside(x,y):
					self.__is_sliding = True
				else:
					self.__is_sliding = False
				self.__initial_click_value = self.__current_min_value
				self.__initial_mouse_pos = [float(x), float(y)]
		elif event.get_event_type() == ev.EventType.MouseButtonUp:
			self.__is_sliding = False

	def set_value(self, value):
		initialValue = self.__current_min_value
		self.__current_min_value = max(0.0,value)
		self.__validate_bounce()

	def set_current_min_value(self, value):
		initialValue = self.__current_min_value
		minValue = value - self.get_range() / 2.0
		self.__current_min_value = max(0.0,minValue)
		self.__validate_bounce()

	def get_current_min_value(self):
		return self.__current_min_value

	def get_current_max_value(self):
		return self.__current_max_value

	def set_range(self, range):
		self.__range = range

	def get_range(self):
		return self.__range

	def set_max_value(self, max):
		self.__max_value = max

	def get_max_value(self):
		return self.__max_value

	def set_horizontal(self, hor):
		self.__is_horizontal = hor

	def is_horizontal(self):
		return self.__is_horizontal

	def __validate_bounce(self):
		if self.__current_min_value + self.__range > self.__max_value:
			self.__current_min_value = max(0.0, self.__max_value - self.__range)
		self.__current_max_value = min(self.__max_value, self.__current_min_value + self.__range)