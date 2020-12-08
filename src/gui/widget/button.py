
import gui.widget.widget as wid
import gui.misc.color as col
import gui.misc.event as ev


def __empty_button_click(button, event, window, page):
	print(20)

class Button(wid.Widget) :

	def __init__(self,text = "") :
		super().__init__()


		#set the default color
		self._color = col.DynColor()
		self._base_color = col.get_grey()
		self._color.set(self._base_color)
		self._color.skip()

		self._text = text
		self._text_color = col.get_white()
		self._text_size = 48.0

		self._border_radius = 50.0

		self.on_click = __empty_button_click

	def update(self,window,page) :
		super().update(window,page)

		self._color.update(3)

	def draw(self,paint,window,page) :
		super().draw(paint,window,page)

		#render button background
		paint.set_paint_color(self._color.to_color())
		paint.draw_rounded_rect(self.get_x(),self.get_y(),self.get_width(),self.get_height(),self._border_radius)

		#render text
		xText = self.get_x() + self.get_width() / 2.0
		yText = self.get_y() + self.get_height() / 2.0 + self._text_size / 4
		paint.set_font_size(self._text_size)
		paint.set_paint_color(self._text_color)


		rect = paint.text_bound(0,0,self._text)
		xText -= rect.w / 2
		paint.draw_text(xText,yText,self._text)

	def on_event(self,event,window,page) :
		super().on_event(event,window,page)
		if event.get_event_type() == ev.EventType.MouseButtonDown :
			if event.get_mouse_button() == ev.MouseButton.LeftButton :
				x = event.get_mouse_x()
				y = event.get_mouse_y()
				if self._pos.is_inside(x, y):
					self._color.set(255,0,0)
					self.on_click(self, event, window, page) #execute the on click event
				else:
					self._color.set(self.get_color())
		elif event.get_event_type() == ev.EventType.MouseMotion:
			x = event.get_mouse_x()
			y = event.get_mouse_y()
			if self._pos.is_inside(x, y):
				self._color.set(self._base_color.red() - 30,self._base_color.green() - 30,self._base_color.blue() - 30)
			else:
				self._color.set(self._base_color)

	def set_text(self,text) :
		self._text = text

	def get_text(self) :
		return self._text

	def set_color(self, color):
		self._base_color = color

	def get_color(self):
		return self._base_color