
external void* fly__gui__readImage(void*)
external void fly__gui__freeImage(void*)

class __InternalImage:

	def __init__(self):
		self.__image_ref = null

	def __del__(self):
		if self.__image_ref != null:
			fly__gui__freeImage(self.__image_ref)

	def __load_from_bytes(self, byte_array):
		self.__image_ref = fly__gui__readImage(byte_array)

	def __load_from_files(self, file):

	def is_loaded(self):
		return self.__image_ref != null