
import gui.widget.widget as wid
import gui.misc.color as col
import gui.misc.event as ev

class Button(wid.Widget) :

	def __init__(self,text = "") :
		super().__init__()
		self._color = col.DynColor(50,50,50,255)

		self._text = text
		self._text_color = col.get_white()
		self._text_size = 48.0

		self._border_radius = 50.0

	def update(self,window,page) :
		super().update(window,page)
		self._color.update()

	def draw(self,paint,window,page) :
		super().draw(paint,window,page)

		#render button background
		paint.set_paint_color(self._color.to_color())
		paint.draw_rounded_rect(self.get_x(),self.get_y(),self.get_width(),self.get_height(),self._border_radius)

		#render text
		xText = self.get_x() + self.get_width() / 2.0
		yText = self.get_y() + self.get_height() / 2.0
		paint.set_font_size(self._text_size)
		paint.set_paint_color(self._text_color)
		paint.draw_text(xText,yText,self._text)

	def on_event(self,event,window,page) :
		super().on_event(event,window,page)
		if event.get_event_type() == ev.EventType.MouseButtonDown :
			if event.get_mouse_button() == ev.MouseButton.LeftButton :
				x = event.get_mouse_x()
				y = event.get_mouse_y()
				if self._pos.is_inside(x, y):
					self._color.set(255,0,0)
				else:
					self._color.set(self.get_color())

	def set_text(self,text) :
		self._text = text

	def get_text(self) :
		return self._text

	def set_color(self, color):
		self._color = color

	def get_color(self):
		return self._color