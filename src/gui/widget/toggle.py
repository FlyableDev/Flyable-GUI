import gui.widget.widget as wid
import gui.misc.color as col
import gui.misc.event as ev

class Toggle(wid.Widget) :

	
	def __init__(self,enabled = False, feature = "") :
		super().__init__()
		#Define colours
		self._color = col.DynColor(125,125,125,255)
		self._color_off = col.DynColor(125,125,125,255)
		self._color_on = col.DynColor(24,171,26,255)
		self._color_circle = col.DynColor(255,255,255,255)
		self._text_color = col.get_white()
		#Define Text and circle positions
		self.xText_offset = 0.75
		self.xCircle_offset = 0.3
		#Define Text
		self._text = "OFF"
		#Define Proportions
		self._text_size = 48.0
		self._radius = 200.0
		self._border_radius = 300.0
		#Define Functionality. Feature refers to what the toggle controls (ex. Dark mode, autosave)
		self.enabled = enabled
		self.feature = feature
		

	def update(self,window,page) :
		super().update(window,page)
		self._color.update(20)


	def change_state(self):
		if self.enabled == True:
			self.enabled = False
			self._color = self._color_off
			self._text = "OFF"
			self.xText_offset =  0.75
			self.xCircle_offset = 0.3

		elif self.enabled == False:
			self.enabled = True
			self._color = self._color_on
			self._text = "ON"
			self.xText_offset = 0.25
			self.xCircle_offset = 0.7

	def draw(self,paint,window,page) :

		super().draw(paint,window,page)


		paint.set_paint_color(self._color.to_color())
		paint.draw_rounded_rect(self.get_x(),self.get_y(),self.get_width(),self.get_height(),self._border_radius)

		#render text
		xText = self.get_x() +  self.get_width() * self.xText_offset
		yText = self.get_y() + self.get_height() / 2.0
		paint.set_font_size(self._text_size)
		paint.set_paint_color(self._text_color)
		paint.draw_text(xText,yText,self._text)

		#render circle
		xCircle = self.get_x() +  self.get_width() * self.xCircle_offset
		yCircle = self.get_x() + self.get_height() / 2.0
		paint.set_paint_color(self._color_circle.to_color())
		paint.draw_circle(xCircle, yCircle,self._radius)
		

	def on_event(self,event,window,page) :
		super().on_event(event,window,page)
		if event.get_event_type() == ev.EventType.MouseButtonDown :
			if event.get_mouse_button() == ev.MouseButton.LeftButton :
				x = event.get_mouse_x()
				y = event.get_mouse_y()
				if self._pos.is_inside(x, y):
				
					self.change_state()
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

	def get_state(self):
		return self.enabled

	def set_state(self, state):
		self.enabled = state
