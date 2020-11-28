import __str as string


external void* fly__gui__createEvent()
external void fly__gui__freeEvent(void*)
external int SDL_PollEvent(void*)
external int fly__gui__getEventType(void*)

external int fly__gui__getMouseButton(void*)
external int fly__gui__getMouseClick(void*)
external int fly__gui__getMouseX(void*)
external int fly__gui__getMouseY(void*)
external void fly__gui__getKey(void*,void*)
external void fly__gui__startTextInput()
external void fly__gui__stopTextInput()
external void fly__gui__getInputText(void*,void*)

external int fly__gui__isCtrlPressed()
external int fly__gui__isShiftPressed()
external int fly__gui__isAltPressed()

external int fly__gui__getMouseWheelX(void*)
external int fly__gui__getMouseWheelY(void*)

external int fly__gui__setClipboard(void*)
external void fly__gui__getClipboard(void*)
external int fly__gui__hasClipboard()



class EventType(Enum) :
	Invalid,
	Quit,
	MouseButtonDown,
	MouseButtonUp,
	MouseMotion,
	WindowEvent,
	TextInput,
	KeyDown,
	MouseWheel


class MouseButton(Enum) :
	LeftButton,
	MiddleButton,
	RightButton,
	X1Button,
	X2Button


class Event :

	def __init__(self) :
		self._eventRef = fly__gui__createEvent()

	def __del__(self) :
		fly__gui__freeEvent(self._eventRef)
		self._eventRef = null


	def poll_event(self) :
		a = SDL_PollEvent(self._eventRef)
		return a == 1

	def get_event_type(self) :
		type = fly__gui__getEventType(self._eventRef)
		result = EventType.Invalid
		if type == -1 :
			result = EventType.Invalid
		elif type == 1 :
			result = EventType.Quit
		elif type == 2 :
			result = EventType.MouseButtonDown
		elif type == 3 :
			result = EventType.MouseButtonUp
		elif type == 4 :
			result = EventType.MouseMotion
		elif type == 5 :
			result = EventType.WindowEvent
		elif type == 6:
			result = EventType.TextInput
		elif type == 7 :
			result = EventType.KeyDown
		elif type == 8 :
			result = EventType.MouseWheel

		return result

	
	def get_mouse_button(self) :
		button = fly__gui__getMouseButton(self._eventRef)
		result = MouseButton.LeftButton
		if button == 1 :
			result = MouseButton.LeftButton
		elif button == 2 :
			result = MouseButton.MiddleButton
		elif button == 3 :
			result = MouseButton.RightButton
		elif button == 4 :
			result = MouseButton.X1Button
		elif button == 5 :
			result = MouseButton.X2Button
		return result

	def get_mouse_x(self) :
		return fly__gui__getMouseX(self._eventRef)

	def get_mouse_y(self) :
		return fly__gui__getMouseY(self._eventRef)

	def get_mouse_click(self) :

	def get_mouse_wheel_x(self) :
		return fly__gui__getMouseX(self._eventRef)

	def get_mouse_wheel_y(self) :
		return fly__gui__getMouseY(self._eventRef)

	def get_key(self) :
		result = str("")
		fly__gui__getKey(self._eventRef,result)
		result.__index()
		return result

	def get_input_text(self) :
		result = str("")
		fly__gui__getInputText(self._eventRef,result)
		result.__index()
		return result

	def start_text_input(self) :
		fly__gui__startTextInput()

	def stop_text_input(self) :
		fly__gui__stopTextInput()

def is_ctrl_pressed(self) :
	return fly__gui__isCtrlPressed() == 1

def is_shift_pressed(self) :
	return fly__gui__isShiftPressed() == 1

def is_alt_pressed(self) :
	return fly__gui__isAltPressed() == 1

def set_clipboard(self,txt) :
	if isinstance(txt,string.str) :
		fly__gui__setClipboard(txt)

def get_clipboard(self) :
	result = str("")
	fly__gui__getClipboard(result)
	result.__index()
	return result