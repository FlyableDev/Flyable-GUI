import gui.widget.widget as wid
import gui.misc.color as col
import gui.misc.rect as rect


class Page :

	def __init__(self) :
		self._widget = wid.Widget()
		self._background = col.get_white()

	def update(self,window) :
		self._widget.update(window,self)

	def draw(self,window,paint) :
		self._widget.set_position(0.0,0.0)
		self._widget.set_size(float(window.get_width()),float(window.get_height()))
		self._widget.apply_margin()
		self._widget.draw(paint,window,self)

	def on_event(self,event,window) :
		self._widget.on_event(event,window,self)

	def set_widget(self,set_wid) :
		self._widget = set_wid
		
	def get_widget(self,wid) :
		return self._widget

	def set_background(self,color) :
		self._background = color

	def get_background(self) :
		return self._background


