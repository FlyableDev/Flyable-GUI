import gui.widget.widget as wid
import gui.misc.event as ev
import gui.misc.color as color
import gui.render.internal.image


def image_from_file(path):

	return Image()

def image_from_data():

	return Image()

class Image(wid.Widget):

	def __init__(self):
		super().__init__()
		self.__image_ref = image.__InternalImage()

	def update(self, window, page) :
		super().update(window,page)

	def draw(self, paint, window, page) :
		super().draw(paint,window,page)

	def on_event(self, event, window, page):
		super().on_event(event, window, page)