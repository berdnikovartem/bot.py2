class user:
	def __init__(self):
		self.__login = ""
		self.__password = ""
		self.__active = False
	
	def getLogin(self) -> str:
		return self.__login
	
	def getActiveness(self) -> bool:
		return self.__active

	def getPassword(self) -> str:
		return self.__password
	
	def setActiveness(self, active: bool) -> None:
		self.__active = active

	def setLogin(self, login: str) -> None:
		self.__login = login

	def setPassword(self, password: str) -> None:
		self.__password = password