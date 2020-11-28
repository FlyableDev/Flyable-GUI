
class Rect :

	def __init__(self, x = 0.0, y = 0.0, w = 0.0, h = 0.0) :
		self.x = x
		self.y = y
		self.w = w
		self.h = h

	def set(self, x = 0.0, y = 0.0, w = 0.0, h = 0.0) :
		self.x = x
		self.y = y
		self.w = w
		self.h = h

	def __copy__(self) :
		return Rect(self.x,self.y,self.w,self.h)

	def is_inside(self, x, y) :
		return x > self.x and x < self.x + self.w and y > self.y and y < self.y + self.h 


class Margin :

	def __init__(self, top = 0.0, bot = 0.0, left = 0.0, right = 0.0) :
		self.top = top
		self.bot = bot
		self.left = left
		self.right = right

	def __copy__(self) :
		return Margin(self.top,self.bot,self.left,self.right)

def apply_margin(pos, margin) :
	pos.x += margin.left
	pos.w -= margin.left + margin.right
	pos.y += margin.top
	pos.h -= margin.top + margin.bot