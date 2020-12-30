import gui.widget.widget as wid
import gui.misc.event as ev
import gui.misc.color as color
import gui.render.internal.image
import gui.widget.image as img
import gui.render.internal.image as intimg


class Image(wid.Widget):

	def __init__(self, data = None):
		super().__init__()
		self.__image_ref = image.__InternalImage(data)

	def update(self, window, page) :
		super().update(window,page)

	def draw(self, paint, window, page) :
		super().draw(paint,window,page)

	def on_event(self, event, window, page):
		super().on_event(event, window, page)