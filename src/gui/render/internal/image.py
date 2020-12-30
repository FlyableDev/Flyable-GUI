
external void* fly__gui__readImage(void*)
external void fly__gui__freeImage(void*)

import __str

class __InternalImage:

	def __init__(self,data):
		self.__image_ref = null
		if isinstance(data,bytes):
			self.__image_ref = self.__load_from_bytes(data)
		elif isinstance(data,__str.str):
			k = 20
			#read = open(data,"r").read()
			#self.__image_ref  = self.__load_from_bytes(readData)
			
	def __del__(self):
		if self.__image_ref != null:
			fly__gui__freeImage(self.__image_ref)

	def __load_from_bytes(self, byte_array):
		return fly__gui__readImage(byte_array)

	def is_loaded(self):
		return self.__image_ref != null