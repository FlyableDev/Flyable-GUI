
import gui.misc.color as col
import math
import gui.misc.rect
import gui.widget.image as img
import gui.misc.color as col

external void* alesia_create_paint()
external void alesia_free_paint(void*)
external void alesia_clear(void*,int,int,int,int)
external void alesia_set_render_size(void*,float,float)

external void alesia_begin_path(void*,float,float)
external void alesia_begin_sub_path(void*,float,float)
external void alesia_add_line(void*,float,float)
external void alesia_add_bezier_cubic(void*,float,float,float,float,float,float)
external void alesia_add_bezier(void*,float,float,float,float)
external void alesia_close(void*)

external void fly__gui__drawText(void*,void*,float,float)
external void fly__gui__textPos(void*, void*, void*, float, float)

external void alesia_set_render_size(void*,float,float)
external void alesia_set_fill_color(void*,int,int,int,int)
external void alesia_set_surface_region(void*,float,float,float,float)
external void alesia_set_surface(void*,void*)
external void alesia_set_surface_rotation(void*,float)
external void alesia_set_surface_rotation_pos(void*,float,float)

external void alesia_set_font_size(void*,float)



class Paint :

	def __init__(self) :
		self._context = alesia_create_paint()
		self._color_fill = col.get_white()
		self._stroke_size = 0.0
		self.__current_image =  img.Image()
		self.__font_size = 14.0

		self.reset()

	def set_surface(self, image):
		if isinstance(image,img.Image):
			self.__current_image = image
			alesia_set_surface(self._context, self.__current_image.__image_ref)
		else:
			self.__current_image = img.Image()
			alesia_set_surface(self._context,null)

	def set_surface_size(self,w,h):
		alesia_set_render_size(self._context,w,h)

	def clear(self,color):
		alesia_clear(self._context,color.red(),color.green(),color.blue(),color.alpha())

	def begin_path(self,x,y):
		alesia_begin_path(self._context,x,y)

	def close_path(self):
		alesia_close(self._context)

	def add_line(self,x,y) :
		alesia_add_line(self._context,x,y)

	def add_bezier(self,xc,yc,x_end,y_end) :
		alesia_add_bezier(self._context,xc,yc,x_end,y_end)

	def add_bezier_cubic(self,x,y,x2,y2,x_end,y_end) :
		alesia_add_bezier_cubic(self._context,x,y,x2,y2,x_end,y_end)

	def set_paint_color(self, color) :
		self._color_fill = color
		alesia_set_fill_color(self._context,self._color_fill.red(),self._color_fill.green(),self._color_fill.blue(),self._color_fill.alpha())

	def set_paint_image(self, image):
		self.__current_image = image
		alesia_set_surface(self._context, image.__image_ref)

	def set_text_align(self,align) :

	def set_font_size(self,size) :
		self.__font_size = size

	def set_font(self,font) :

	def set_stroke_color(self,color) :

	def set_stroke(self, stroke) :
		self._stroke_size = stroke

	def draw_arc(self,xc,yc,x1,y1,x4,y4,radius) :
			self.begin_path(xc,yc)
			self.add_line(x1,y1)

			ax = x1 - xc
			ay = y1 - yc
			bx = x4 - xc
			by = y4 - yc
			q1 = (ax * ax) + (ay * ay)
			q2 = q1 + (ax * bx) + (ay * by)
			k2 = (4.0 / 3.0) * (math.sqrt(2.0 * q1 * q2) - q2) / (ax * by - ay * bx)
			
			x2 = xc + ax - (k2 * ay)
			y2 = yc + ay + (k2 * ax)
			x3 = xc + bx + (k2 * by)                                 
			y3 = yc + by - (k2 * bx)
			self.add_bezier_cubic(x2,y2,x3,y3,x4,y4)
			self.close_path()

	def draw_rect(self,x,y,w,h) :
		self.begin_path(x,y)
		self.add_line(x + w,y)
		self.add_line(x + w,y + h)
		self.add_line(x,y + h)
		self.close_path()

	def draw_rounded_rect(self,x,y,w,h,radiusArg) :
			radius = radiusArg
			K = 4.0 * (math.sqrt(2.0) - 1.0) / 3.0 #constant for circles using Bezier curve.
			left = x
			top = y
			right= left + w
			bottom= top + h
			self.begin_path(left + radius,top)
			self.add_line(right - radius,top)
			self.add_bezier_cubic(right + radius * (K-1.0),top,right,top + radius * (1.0 - K),right,top + radius)
			self.add_line(right,bottom - radius)
			self.add_bezier_cubic(right,bottom + radius * (K - 1.0),right + radius * (K - 1.0),bottom,right - radius,bottom)
			self.add_line(left + radius,bottom)
			self.add_bezier_cubic(left + radius * ( 1.0 - K),bottom,left,bottom + radius * ( K - 1.0),left,bottom - radius)
			self.add_line(left,top + radius)
			self.add_bezier_cubic(left,top + radius*(1.0 - K),left+radius*(1.0 - K),top,left + radius,top)
			self.close_path()

	def draw_ellipse(self,cx,cy,rx,ry) :

	def draw_circle(self,x,y,radius) :
		approx = 0.552284 * radius
		self.begin_path( x + radius,y) #right point
		self.add_bezier_cubic(x + radius,y + approx,x + approx,y + radius,x,y + radius) #up point
		self.add_bezier_cubic(x - approx,y + radius,x - radius,y + approx,x - radius,y) #left point
		self.add_bezier_cubic(x - radius,y - approx ,x - approx,y - radius,x,y - radius) #down point
		self.add_bezier_cubic(x + approx,y - radius,x + radius,y - approx,x + radius,y) #right point again
		self.close_path()

	def draw_triangle(self,x1,y1,x2,y2,x3,y3) :
		self.begin_path(x1,y1)
		self.add_line(x2, y2)
		self.add_line(x3, y3)
		self.close_path()

	def draw_shape(self,points) :
		if len(points)  > 0:
			self.begin_path(points[0].x,points[0].y)
			for e in range(1,len(points)) :
				self.add_line(points[e].x,points[e].y)
		self.close_path()

	def set_font_size(self,size):
		self.__font_size = size
		alesia_set_font_size(self._context,size)

	def get_font_size(self):
		return self.__font_size

	def draw_text(self,x,y,txt):
		fly__gui__drawText(self._context,txt,x,y)

	def text_bound(self,x,y,txt):
		result = rect.Rect()
		fly__gui__textPos(self._context,txt,result,x,y)
		return result

	def reset(self) :
		self.set_font_size(14.0)
		self.set_paint_color(col.get_white())
		self.__current_image =  img.Image()
		self.reset_scissor()

	def reset_scissor(self) :

