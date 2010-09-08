import re

class INFO:
	auth_parse = re.compile(r"^\s*([^\s]+)\s+<([^@]+@[^>]+)>\s*$")

	def __init__(self,name,version,desc,author,url):
		self.__n = name
		self.__v = version
		self.__d = desc
		self.__u = url
		self.__a , self.__m = self._parse(author)

	def _parse(self,s):
		a,m = [],[]
		for i in s.split('\n'):
			t = self.auth_parse.match(i)
			if t:
				a.append(t.group(1))
				m.append(t.group(2))
		return " and ".join(a)," or ".join(m)

	@property
	def NAME(self):
		return self.__n

