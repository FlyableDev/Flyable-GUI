
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

	root = filetree.Treeitem([],"root")

	folder1 = filetree.Treeitem([], "folder","folder1")
	folder2 = filetree.Treeitem([], "folder", "folder2")
	file1 = filetree.Treeitem([], "file", "file1", "This is a sample")
	file2 = filetree.Treeitem([], "file", "file2", "This is another sample")	
	root.add_item(folder1)
	root.add_item(folder2)
	root.add_item(file1)
	root.items[1].add_item(file1)
	print(root)

	print(root.items[0])
	print(root.items[1])
	
	print(len(root.items))

	root.print_items()
	root.items[1].print_items()	


	page = pag.Page()
	
	page.set_widget(filetree.Filetree())
	#page.set_widget(text.Text("Pokemon"))

	a.add_page(page)

	a.show()