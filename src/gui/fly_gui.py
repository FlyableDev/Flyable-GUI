
import gui.render.window as win
import gui.render.page as pag
import gui.widget.textarea
import gui.widget.checkbox
import gui.widget.button
import gui.widget.text
import gui.widget.toggle
import gui.widget.filetree

import gui.widget.layout.vertical_layout as lay


def main() :
	a = win.Window("Flyable demo",800,600)

	#root = filetree.Folder("root")
	#file1_1 = filetree.File("file1_1","This is file 1 on level 1")
	#print(root.foldername)
	#print(root.foldercontents[0])
	#root.foldercontents.additem("file1")
	#filesystem = [file1_1]
	#filesystem.append("file1")
	#filesystem.append(["subfile1","subfile2"])
	#filesystem.append("samplefile")
	#print(filesystem[0])
	
	page = pag.Page()
	
	page.set_widget(filetree.Filetree())
	#page.set_widget(text.Text("Pokemon"))

	a.add_page(page)

	a.show()