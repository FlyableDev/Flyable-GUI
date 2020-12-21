import gui.widget.widget as wid
import gui.misc.color as col
import gui.misc.event as ev
import gui.misc.rect as rec
import gui.widget.slider

class File:

#	give each file a filename and a space as content
	def __init__(self, filename = "filename", filecontent = " "):
		self.filename = filename
		self.filecontent = filecontent
		self.isopen = False

class Folder:
	def __init__(self,foldername = "foldername"):
		self.foldername = foldername
#	foldercontents is a list that can contain files or other folders
		self.foldercontents = [null]
#	self.expanded defines whether the folder is expanded in the filetree or not
		self.expanded = False
#	self.opencontent defines whether any files in the folder are open in the IDE
		self.opencontent = False

#	How to add a new item
	def additem(self, foldercontents, newitem):
		self.foldercontents.append(newitem)

#	This class brings together the Folder and Fileclasses to allow folder to be nested in other folder alongside files..		
class Filesystem:
	def __init__(self):
		pass




class Filetree(wid.Widget):

#	localroot is the folder that is first openend in the IDE, like a main project folder
	def __init__(self, localroot = null):
		super().__init__()
		self.localroot = localroot
		self._text_size = 14
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


#	The visibile_items function takes the Filesystem object and returns a sequential list of the items that need to be displayed along with

#		type (file/folder) 
#		color assignment
#		name (text to be displayed)
#		indentation level

#	The criteria for being displayed is whether the parent folder is expanded.

	def visible_items(self, filesystem):
		pass


#	render the widget
	def draw(self,paint,window,page):
		super().draw(paint,window,page)

#	define 1 large rectangle to be the background of the widget
		paint.set_paint_color(self._background_color)
		paint.draw_rect(self.get_x(),self.get_y(),self.get_width(),self.get_height())

#	Go through the list, and create a rectangle of the appropriate color for each item of the list
#	Shift down by an amount that is proportional to the font size
#	Define specific areas within the widget that correspond to each item (needs index, top and bottom y boundaries. X boundaries taken from Widget


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

		