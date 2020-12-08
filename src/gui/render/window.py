
import gui.widget.widget as wid
import gui.misc.event as event
import gui.render.page as page
import gui.render.paint as paint
import gui.misc.color as color
import time


external void* fly__gui__createWindow()
external void fly__gui__maximizeWindow(void*)
external void SDL_GL_SwapWindow(void*)

external int fly__gui__getWindowX(void*)
external int fly__gui__getWindowY(void*)
external void fly__gui__resizeWindow(void*,int,int)
external void fly__gui__setWindowTitle(void*,void*)
external void fly__gui__setWindowIcon(void*,void*)



class Window :


	def __init__(self,title = " ",w = 800,h = 600) :
		self._windowRef = fly__gui__createWindow()
		self._paint = paint.Paint()
		self._title = title
		self.set_title(title)
		self._pages = [page.Page()]
		self._frame_count = 0

	def show(self) :
		loop = True
		winEvent = event.Event()
		while loop :

			lastPage = self._pages[len(self._pages) - 1]

			while winEvent.poll_event() :
				eventType = winEvent.get_event_type()
				if eventType == event.EventType.Quit :
					loop = False

				if loop  :
					lastPage.on_event(winEvent,self)
	
			lastPage.update(self)
			self._frame_count += 1
			if self._frame_count >= 60:
				self._frame_count = 0

			#render the current page
			self._paint.set_surface_size(self.get_width(),self.get_height())
			self._paint.clear(lastPage.get_background())
			lastPage.draw(self,self._paint)

			SDL_GL_SwapWindow(self._windowRef)
			time.sleep(1.0 / 60.0)

	def add_page(self,new_page) :
		self._pages.append(new_page)

	def set_title(self,title) :
		self._title = title
		fly__gui__setWindowTitle(self._windowRef,title)

	def set_szie(self,x,y) :
		fly__gui__resizeWindow(self._windowRef,x,y)

	def get_title(self) :
		return self._title

	def get_width(self) :
		return fly__gui__getWindowX(self._windowRef)

	def get_height(self) :
		return fly__gui__getWindowY(self._windowRef)
		
	def set_icon(self,icon) :

	def get_paint(self):
		return self._paint

	def get_frame(self):
		return self._frame_count

	def maximize(self) :
		fly__gui__maximizeWindow(self._windowRef)