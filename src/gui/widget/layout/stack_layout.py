import gui.widget.layout.layout as layout
import gui.widget.widget as widget

class StackLayout(layout.Layout) :

	def __init__(self) :
		super().__init__()
		self._widgets = [widget.Widget()]
		self._widgets.clear()
		#self._widgets = widgets


	def update(self,window,page) :
		super().update(window,page)
		for e in self._widgets :
			e.update(window,page)


	def draw(self,paint,window,page) :
		for e in self._widgets :
			e.draw(paint,window,page)

	def on_event(self,event,window,page) :
		super().on_event(event,window,page)

		for e in self._widgets : 
			e.on_event(event,window,page)


	def add(self,wid) :
		self._widgets.append(wid)


	def pop(self,id) :
		self._widgets.remove(id)