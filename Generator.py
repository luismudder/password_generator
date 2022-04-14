# Created by: Luis Müdder
# Github: Luis Müdder
from random import choice as rchoice
class generator:
	def __init__(self,service, user, size, Type=1):
		password = ""
		for x in range(size):
			key = self.choice(Type = Type)
			password += key
		self.save(service ,user , password)
	def choice(self, Type):
		array = [0,1,2,3,4,5,6,7,8,9]
		if Type == 1:
			array = ['!','"','#','$','%','&',"'",'(',')','*','+',',','-','.','/','0','1','2','3','4','5','6','7','8','9',':',';','<','=','>','?','@','A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z','[',chr(33+60),']','^','_','`','a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z','{','|','}','~']
			return rchoice(array)
		if Type == 2:
			pass
	def save(self, service, user, password):
		f = open("users.txt","a")
		f.write(f"Service: {service} | User: {user} | Password: {password}\n")
		f.close()
def loop():
	while True:
		try:
			generator(input("Service: "), input("Users: "), int(input("Size of password: ")))
		except:
			print("failed, try again '-'")
			loop()
		print("Successful OwO")
loop()