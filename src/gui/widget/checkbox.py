
import gui.widget.widget as wid
import gui.misc.event as ev
import gui.misc.color as color

class CheckBox(wid.Widget):

	def __init__(self):
		super().__init__()
		self.checked = False
		self.__is_over = True


	def update(self, window, page) :
		super().update(window,page)

	def draw(self, paint, window, page) :
		super().draw(paint,window,page)


		minSize = min(self.get_width(),self.get_height())


		paint.set_stroke(5.0)
		paint.draw_rounded_rect(self.get_x(),self.get_y(),minSize,minSize,0.0)
		if self.checked:
			paint.set_paint_color(color.get_red())
			paint.draw_rect(self.get_x() + minSize * 0.1,self.get_y() + minSize * 0.1,minSize * 0.9,minSize * 0.9)

	def on_event(self, event, window, page):
		super().on_event(event, window, page)
		
		if self.__is_over:
			if event.get_event_type() == ev.EventType.MouseMotion:
				x = event.get_mouse_x()
				y = event.get_mouse_y()
			elif event.get_event_type() == ev.EventType.MouseButtonDown:
				if event.get_mouse_button() == ev.MouseButton.LeftButton:
					if self.checked:
						self.checked = False
					else:
						self.checked = True