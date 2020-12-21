
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

	root = filetree.Treeitem([], "Does this allow me to modify text?")

	folder1 = filetree.Treeitem()
	root.add_item(folder1)
	print(root)

	root.print_items()
	
	page = pag.Page()
	
	page.set_widget(filetree.Filetree())
	#page.set_widget(text.Text("Pokemon"))

	a.add_page(page)

	a.show()