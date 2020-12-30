
import gui.render.window as win
import gui.render.page as pag
import gui.widget.textarea
import gui.widget.checkbox
import gui.widget.button
import gui.widget.text
import gui.widget.toggle
import gui.widget.slider
import gui.widget.scrollbar

import gui.widget.layout.vertical_layout as lay


def click(button, event, window, page):
	print(420)

def main() :
	a = win.Window("Flyable demo",800,600)

	page = pag.Page()

	page.set_widget(textarea.TextArea())

	a.add_page(page)

	a.show()