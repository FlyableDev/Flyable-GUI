import gui.widget.widget as wid
import gui.misc.color as col
import gui.misc.event as ev

class Toggle(wid.Widget) :

	def __init__(self, text = "OFF", enabled = false) :
		super().__init__()
		self._color_off = col.DynColor(100,100,100,255)
		self._color_on = col.DynColor(24,171,26,255)
		self.enabled = enabled
		self._text = text
		self._text_color = col.get_white()
		self._text_size = 20.0
		self._border_radius = 5.0
		self._circle_diameter = 50.0

	def draw(self,paint,window,page) :
		super().draw(paint,window,page)
		paint.set_paint_color(self._color_on.to_color())
		paint.draw_rounded_rect(self.get_x(),self.get_y(),self.get_width(),self.get_height(),self._border_radius)
		#render text
		xText = self.get_x() + self.get_width() / 4.0
		yText = self.get_y() + self.get_height() / 2.0
		paint.set_font_size(self._text_size)
		paint.set_paint_color(self._text_color)
		paint.draw_text(xText,yText,self._text)

        #Render circle

		xCircle = self.get_x()
		yCircle = self.get_y()
		paint.set_paint_color(col.get_white())
		paint.draw_circle(xCircle,yCircle,self._circle_diameter)