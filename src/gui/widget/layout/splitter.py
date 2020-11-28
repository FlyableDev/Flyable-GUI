import gui.widget.layout.layout as layout
import gui.widget.widget as widget
import gui.misc.event as ev
import gui.misc.rect as rect

class Splitter(layout.Layout) :

	def __init__(self, wid1 = widget.Widget(), wid2 = widget.Widget()):
		super().__init__()
		self._wid1 =  wid1
		self._wid2 = wid2
		self._ratio = 0.5
		self._hor = True
		self._split_distance = 5.0
		self._split_click_zone = rect.Rect()
		self._split_selected = False
		self._user_editable = False
		
	def update( self, window, page):
		super().update(window,page)
		self._wid1.update(window,page)
		self._wid2.update(window,page)

	def draw(self, paint, window, page):
		super().draw(paint,window,page)
		
		x = self.get_x()
		y = self.get_y()
		w = self.get_width()
		h = self.get_height()

		if self._hor : #horizontal placement
			self._wid1.set_shape(x,y,w * self._ratio - self._split_distance,h)
			self._wid2.set_shape(x + w * self._ratio + self._split_distance ,y,w *  (1.0 - self._ratio) - self._split_distance,h)
		else : #vertical
			self._wid1.set_shape(x,y,w,h * self._ratio - self._split_distance)
			self._wid2.set_shape(x,y + h * self._ratio + self._split_distance,w,h *  (1.0 - self._ratio) - self._split_distance)

		#and now we render them
		self._wid1.draw(paint,window,page)
		self._wid2.draw(paint,window,page)

	def on_event(self, event, window, page) :
		super().on_event(event,window,page)

		if event.get_event_type() == ev.EventType.MouseButtonDown and event.get_mouse_button() == ev.MouseButton.LeftButton :
			x = event.get_mouse_x()
			y = event.get_mouse_y()
			if self._split_click_zone.is_inside(x,y) :
				self._split_selected = True
			elif event.get_event_type() == ev.EventType.MouseButtonUp and event.get_mouse_button() == ev.MouseButton.LeftButton :
				self._split_selected = False
			elif event.get_event_type() == ev.EventType.MouseMotion and self._split_selected and self._user_editable :
				x = event.get_mouse_x()
				y = event.get_mouse_y()
				if self._hor :
					self.set_ratio(  ( float(x) - self.get_x() )  / ( self.get_width()) )
				else :
					self.set_ratio(  ( float(y) - self.get_y() )  / ( self.get_height()) )


		#pass the event
		self._wid1.on_event(event,window,page)
		self._wid2.on_event(event,window,page)

	def set_ratio(self, ratio):
		self._ratio = ratio

	def get_ratio(self):
		return self._ratio

	def set_horizontal(self, hor):
		self._hor = hor

	def is_horizontal(self):
		return self._hor