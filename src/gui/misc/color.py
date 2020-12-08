
def color_to_dyn_color(color):
	return DynColor(color.red(), color.green(), color.blue(), color.alpha())


class Color :

	def __init__(self,r,g,b,a) :
		self._r = r
		self._g = g
		self._b = b
		self._a = a

	def red(self) :
		return self._r

	def green(self) :
		return self._g

	def blue(self) :
		return self._b

	def alpha(self) :
		return self._a


class DynColor :

	def __init__(self,r = 255,g = 255,b = 255,a = 255) :
		self._r = r
		self._g = g
		self._b = b
		self._a = a

		self._r_reach = self._r
		self._g_reach = self._g
		self._b_reach = self._b
		self._a_reach = self._a


	def set(self,r = 255,g = 255,b = 255,a = 255,direct = False) :


		if isinstance(r,DynColor):
			self._r_reach = r._r
			self._g_reach = r._g
			self._b_reach = r._b
			self._a_reach = r._a
		elif isinstance(r,int):
			self._r_reach = r
			self._g_reach = g
			self._b_reach = b
			self._a_reach = a
		elif isinstance(r,Color):
			self._r_reach = r._r
			self._g_reach = r._g
			self._b_reach = r._b
			self._a_reach = r._a
	
		if direct == True :
			self.skip()

	def update(self, frame = 10) :

		for e in range(0,frame):
			if self._r_reach > self._r :
				self._r += 1
			elif self._r_reach < self._r :
				self._r -= 1
	
			if self._g_reach > self._g :
				self._g += 1
			elif self._g_reach < self._g :
				self._g -= 1
	
			if self._b_reach > self._b :
				self._b += 1
			elif self._b_reach < self._b :
				self._b -= 1
	
			if self._a_reach > self._a :
				self._a += 1
			elif self._a_reach < self._a :
				self._a -= 1

	def skip(self):
		self._r = self._r_reach
		self._g = self._g_reach
		self._b =self._b_reach
		self._a = self._a_reach

	def red(self) :
		return self._r

	def green(self) :
		return self._g

	def blue(self) :
		return self._b

	def alpha(self) :
		return self._a

	def to_color(self) :
		return Color(int(self._r),int(self._g),int(self._b),int(self._a))

	def is_changing(self):
		if self._r == self._r_reach:
			if self._b == self._b_reach:
				if self._g == self._g_reach:
					if self._a == self._a_reach:
						return False
		return True


def get_black() :
	return Color(0,0,0,255)

def get_white() :
	return Color(255,255,255,255)

def get_red() :
	return Color(255,0,0,255)

def get_grey():
	return Color(50, 50, 50, 255)