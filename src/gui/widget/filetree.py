import gui.widget.widget as wid
import gui.misc.color as col
import gui.misc.event as ev
import gui.misc.rect as rec
import gui.widget.slider

class Treeitem:

#	give each file a filename and a space as content
	def __init__(self, items = [], type = "file", name = "", filetext = "" ):
#	if the item is a file, it will have the "_file_text" attribute, which can be assumed to be text. items attribute will remain an empty list
#	if the item is a folder, the items list will be filled with other "Treeitems", that will be either files or folders
#	The object must know it's own name, which is not necessarily the name of the variable that stores the object
#	Should introduce logic to only allow "file" and "folder" types
		self.type = type
		self.name = name
		self.items = items
		self._file_text = filetext
		self.open = False

#	calling print on the object will return only the name
	def __str__(self):
		return self.name

	def __repr__(self):
		return self.name

#	Instead of using print(object), this function will print the contents of the object (files in a folder)
#	Could eventually be made in a recursive function that can print out multiple levels
	def print_items(self):

		i = 0
		while i < len(self.items):
			print(self.items[i])
			i += 1

#Assign text to the Treeitem. This is what would be accessed when the file is open
	def replace_text(self, new_string):
		self._file_text = new_string

#	Add a new item to the items list
	def add_item(self, new_item):
		self.items.append(new_item)


#	Open or close a file/folder
	def open(self):
		self.open = True

	def close(self):
		self.open = False

#	return the state of the item
	def get_open(self):
		return self.open

	def rename(self,new_name):
		self.name = new_name

	def get_name(self):
		return self.name

#	Missing a method to sort items in the list so that they are presented as alpabetical files, and alphabetical folders

class Filetree(wid.Widget):

#	localroot is the folder that is first openend in the IDE, like a main project folder
	def __init__(self, localroot):
		super().__init__()
		self.localroot = localroot
		self._text_size = 50
#	Colors
		self._background_color = col.get_black()
#	Colors will be used to indicate whether the item is open in the text editor or not
		self._text_color = col.get_white()
		self._file_color = col.get_black()
		self._folder_color = col.Color(125,125,125,255)
		self._selected_color = col.Color(0,150,250,255)
#	Optional Colors: If a file/folder is open in the text editor or not
		self._file_open_color = col.Color(200,200,200,255)
		self._folder_open_color = col.Color(50,50,50,255)


#	Will need to sort the items list to show files alphabetically, and then folders alphabetically

#		type (file/folder) 
#		color assignment
#		name (text to be displayed)
#		indentation level

#	The criteria for being displayed is whether the parent folder is open.

	def visible_items(self, filesystem):
		pass


#	render the widget. Remember that tyhis is working through the recursive filetree
	def draw(self,paint,window,page):
		super().draw(paint,window,page)

#	define 1 large rectangle to be the background of the widget
		paint.set_paint_color(self._background_color)
		paint.draw_rect(self.get_x(),self.get_y(),self.get_width(),self.get_height())

#	Go through the list, and create a rectangle of the appropriate color for each item of the list
#	Shift down by an amount that is proportional to the font size
#	Define specific areas within the widget that correspond to each item (needs index, top and bottom y boundaries. X boundaries taken from Widget

#	Start with just rendering  the root level rectangle. This part isn't recursive yet.

		paint.set_paint_color(self._folder_color)
		paint.draw_rect(self.get_x(),self.get_y(),self.get_width(),self.get_height()*0.1)
		paint.set_paint_color(self._text_color)
		
		xText = self.get_x() + self.get_width() * 0.1
		yText = self.get_y() + self.get_height() * 0.05
		paint.draw_text(xText,yText,self.localroot.name)

		i = 1
		while i <= len(self.localroot.items):
			#xText = self.get_x() + self.get_width() * 0.1
			yText = self.get_y() + self.get_height() * 0.05 * i
			paint.draw_text(xText,yText,self.localroot.items[i].name)
			i +=1

#	Define the actions that will occur for clicking and double clicking on different areas of the Filetree
#	Include time calculation between 1st and 2nd click to define double click
#	Single click: Select the file or folder (highlight and change color)
#	Doubleclick on folder: Flip folder "expanded" attribute to either show or hide contents
#	Doubleclick on file: open file in text editor
	def on_event(self,event,window,page) :
		super().on_event(event,window,page)
		if event.get_event_type() == ev.EventType.MouseButtonDown :
			if event.get_mouse_button() == ev.MouseButton.LeftButton :
				#self.mousecounter += 1
				x = event.get_mouse_x()
				y = event.get_mouse_y()
				# Determine which item was clicked on by comparing y coordinate with the y boundaries of invidual items. Use binary search to find it? Not sure if big enough to justify
				#self.selected_item = null #This will eventually be the index

		