import gui.misc.rect as r

class Widget :

	def __init__(self) :
		self._pos = r.Rect(0.0,0.0,100.0,100.0)
		self._margin = r.Margin(5.0,5.0,5.0,5.0)
		

	def update(self,window,page) :

	def draw(self,paint,window,page) :

	def on_event(self,event,window,page) :

	def set_position(self,x,y) :
		self._pos.x = x
		self._pos.y = y

	def set_size(self,w,h) :
		self._pos.w = w
		self._pos.h = h

	def set_shape(self, x, y, w, h) :
		self.set_position(x,y)
		self.set_size(w,h)

	def get_x(self) :
		return self._pos.x

	def get_y(self) :
		return self._pos.y

	def get_width(self) :
		return self._pos.w

	def get_height(self) :
		return self._pos.h

	def apply_margin(self) :
		r.apply_margin(self._pos,self._margin)
