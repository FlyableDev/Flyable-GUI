import gui.widget.widget as wid
import gui.misc.color as col
import gui.misc.event as ev
import gui.misc.rect as rec
import gui.widget.scrollbar



class TextArea (wid.Widget) :

	def __init__(self, str = ""):
		super().__init__()
		self.__current_text = str
		self.__is_in_edit = False
		self.__frame_update = -1
		self.__click_zone = rec.Rect()
		self.__text_scroll = 0.0
		self.__manual_scroll = False

		#self.__font =

		self.__fonts_rect = []

		self.__background_color = col.get_white()
		self.__cursor_color = col.color_to_dyn_color(col.get_black())


		self.__selection_min = 0
		self.__selection_max = 0
		self.__current_index = 0
		self.__hold = False
		self.__font_size = 20.0

		self.__vertical_scroll = scrollbar.ScrollBar()
		self.__vertical_scroll.set_horizontal(False)
		self.__horizontal_scroll = scrollbar.ScrollBar()


	def update(self, window, page):
		super().update(window,page)
		self.__vertical_scroll.update(window, page)
		self.__horizontal_scroll.update(window, page)



		self.__cursor_color.update(10)

		if self.__cursor_color.is_changing() == False:
			if self.__cursor_color.alpha() == 255:
				self.__cursor_color.set(0,0,0,0)
			else:
				self.__cursor_color.set(0,0,0,255)

		self.__vertical_scroll.update(window, page)
		self.__horizontal_scroll.update(window, page)


		#update the scroll bars
		longest_line = 0.0
		for e in self.__get_lines():
			window.get_paint().set_font_size(self.__font_size)
			longest_line = max(longest_line, window.get_paint().text_bound(0,0,e).w)


		self.__horizontal_scroll.set_range(self.get_width())
		self.__horizontal_scroll.set_max_value(longest_line)
		self.__horizontal_scroll.set_position(self.get_x(),self.get_y() + self.get_height() - 50.0)
		self.__horizontal_scroll.set_size(self.get_width(),50.0)


		self.__vertical_scroll.set_range(self.get_height())
		self.__vertical_scroll.set_max_value(len(self.__get_lines()) * self.__font_size)
		self.__vertical_scroll.set_size(50.0, self.get_height() - 40.0)
		self.__vertical_scroll.set_position(self.get_x() + self.get_width() - 30 , self.get_y())
		

	def draw(self,paint,window,page) :
		super().draw(paint,window,page)

		paint.set_paint_color(col.get_white())
		paint.draw_rounded_rect(self.get_x(),self.get_y(),self.get_width(),self.get_height(),3.0)


		#render text
		paint.set_font_size(self.get_height() * 0.8)
		paint.set_paint_color(col.get_black())
		paint.set_font_size(self.__font_size)

		textLines = self.__current_text.split("\n")
		for i in range(0,len(textLines)):
			paint.draw_text(self.get_x() - self.__horizontal_scroll.get_current_min_value(),self.get_y() + self.__font_size * (i + 1) - self.__vertical_scroll.get_current_min_value(),textLines[i])


		#render selection highlight
		paint.set_paint_color(col.Color(0,255,0,70))
		if self.__selection_min != self.__selection_max:
			currentLine = 0
			currentIndex = 0
			for i in range(0,len(textLines)):
				lineLenght = len(textLines[i])
				if self.__current_index < currentIndex + lineLenght and self.__current_index >= currentIndex : #test for an highlight in the line
					start = paint.text_bound(0,self.__selection_min - currentIndex,textLines[i]).w
					end = paint.text_bound(self.__selection_max - currentIndex,lineLenght,textLines[i]).w
				currentIndex += len(textLines[i]) + 1
				currentLine += 1

		#render cursor
		selectionPos = self.__get_char_position(paint,self.__current_index)
		paint.set_paint_color(self.__cursor_color.to_color())
		paint.draw_rect(selectionPos[0] + 4.0 - self.__horizontal_scroll.get_current_min_value(),selectionPos[1] + self.__font_size / 4 - self.__vertical_scroll.get_current_min_value(),2,self.__font_size )

		if self.__horizontal_scroll.get_max_value() > self.get_width():
			self.__horizontal_scroll.draw(paint, window, page)
		if self.__vertical_scroll.get_max_value() > self.get_height():
			self.__vertical_scroll.draw(paint, window, page)


	def on_event(self, event, window, page):
		super().on_event(event, window,page)

		self.__horizontal_scroll.on_event(event, window,page)
		self.__vertical_scroll.on_event(event, window, page)

		if event.get_event_type() == ev.EventType.TextInput and self.is_in_edit():
			input = event.get_input_text()
			self.write_text(input)
		elif event.get_event_type() == ev.EventType.KeyDown:
			input = event.get_key()
			self.__handle_special_key(input)
		elif event.get_event_type() == ev.EventType.MouseButtonDown:
			if event.get_mouse_button() == ev.MouseButton.LeftButton:
				x = event.get_mouse_x()
				y = event.get_mouse_y()
				if self._pos.is_inside(x,y):
					self.__is_in_edit = True
					event.start_text_input()	
					self.__current_index = self.__get_index_pos(window.get_paint(),x,y)



	def __get_char_position(self,paint,index):
		textLines = self.__current_text.split("\n")
		currentIndex = 0
		currentLine = 0
		for e in textLines: 
			if index >= currentIndex and index <= currentIndex + len(e):
				#found the good line
				rect = paint.text_bound(self.get_x(), self.get_y(), e[0:index - currentIndex])
				return (rect.w,currentLine * self.__font_size)
			currentIndex += len(e) + 1
			currentLine += 1
		return (0.0,currentLine * self.__font_size)

	def __handle_special_key(self, key):
		if key == "Backspace":
			self.__current_text = self.__current_text[0 : self.__current_index - 1]  + self.__current_text[ self.__current_index: len(self.__current_text)]
			if self.__current_index > 0:
				self.__current_index -= 1
		elif key == "Delete":
			self.__current_text = self.__current_text[0 : self.__current_index]  + self.__current_text[ self.__current_index + 1: len(self.__current_text)]
		elif key == "Return":
			self.write_text("\n")
		elif key == "Left":
			if self.__current_index > 0:
				self.__current_index -= 1
		elif key == "Right":
			if self.__current_index < len(self.__current_text):
				self.__current_index += 1
		elif key == "Up":
			lineId =self.__get_current_line()
			if lineId > 0:
				indexOnLine = self.__get_index_on_line(self.__current_index)
				self.__current_index -= indexOnLine
				lines = self.__get_lines()
				self.__current_index -= len(lines[lineId - 1]) - indexOnLine  + 1
				if self.__current_index < 0:
					self.__current_index = 0
		elif key == "Down":
			lines = self.__get_lines()
			lineId =self.__get_current_line()
			if lineId < len(lines) - 1:
				indexOnLine = self.__get_index_on_line(self.__current_index)
				self.__current_index += len(lines[lineId]) - indexOnLine #reach the end on line
				lines = self.__get_lines()
				self.__current_index += indexOnLine + 1
				if self.__current_index > len(self.__current_text):
					self.__current_index = len(self.__current_text)
		elif key == "A":
			self.select_all()

	def write_text(self, txt):

		if self.is_selection_active():
			self.__current_text = self.__current_text[0 : self.__selection_min] + self.__current_text[self.__selection_min : len(self.__current_text)]

		leftText = self.__current_text[0 : self.__current_index]
		rightText = self.__current_text[ self.__current_index : len(self.__current_text) + len(txt)]

		self.__current_text = leftText + txt + rightText
		self.__current_index += len(txt)

	def select_all_line(self):
		self.__selection_min = self.__get_index_on_line(0)
		self.__selection_max = self.__selection_min + len(self.__get_lines()[self.__get_current_line()])

	def select_all(self):
		self.__selection_min = 0
		self.__selection_max = len(self.__current_text)

	def is_selection_active(self):
		return self.__selection_min != 0 and self.__selection_max != 0

	def __get_index_pos(self, paint, x, y):
		#return the index pointed by the x and y point
		lines = self.__get_lines()
		lineId = self.__get_line_from_pos(y)
		line = lines[lineId]
		if x < self.get_x():
			return 0

		currentIndex = 0
		currentLine = 0
		for i in lines:
			if currentLine == lineId:
				for e in range(0,len(i) - 1):
					rectLeft = paint.text_bound(0,0,i[0 : e])
					rectRight = paint.text_bound(0,0,i[0 : e + 1])
					if x >= rectLeft.w and x <= rectRight.w:
						return currentIndex + e
			currentIndex += len(i) + 1
			currentLine += 1
		return currentIndex - 1
		
	def __get_line_from_pos(self, y):
		#return the line at the y pos
		return min(int(y / self.__font_size),len(self.__get_lines()) - 1)

	def __get_current_line(self):
		index = self.__current_index
		textLines = self.__current_text.split("\n")
		currentIndex = 0
		currentLine = 0
		for e in textLines: 
			if index >= currentIndex and index <= currentIndex + len(e):
				return currentLine
			currentIndex += len(e) + 1
			currentLine += 1
		return 0

	def __get_index_on_line(self, index):
		#return what index is the index on the current line
		textLines = self.__current_text.split("\n")
		currentIndex = 0
		currentLine = 0
		for e in textLines: 
			if index >= currentIndex and index <= currentIndex + len(e):
				return index - currentIndex
			currentIndex += len(e) + 1
			currentLine += 1
		return 0

	def __get_lines(self):
		#return every lines in the text area
		return self.__current_text.split("\n")

	def get_total_width(self):
		return len(self.__get_lines()) * self.__font_size

	def is_in_edit(self):
		return self.__is_in_edit

	def set_text(self, txt):
		self.__current_text = txt

	def get_text(self):
		return self.__current_text