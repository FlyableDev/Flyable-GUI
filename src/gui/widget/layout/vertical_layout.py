import gui.widget.layout.stack_layout

class VerticalLayout(stack_layout.StackLayout) :

	def __init__(self) :
		super().__init__()

	def draw(self,paint,window,page) :
		hByIndex = self.get_height() / float(len(self._widgets))
		for i in range(0,len(self._widgets)) :
			self._widgets[i]._pos.set(self._pos.x,self._pos.y + (hByIndex * float(i)),self._pos.w,hByIndex)
			self._widgets[i].apply_margin()
			self._widgets[i].draw(paint,window,page)


		super().draw(paint,window,page) #now render