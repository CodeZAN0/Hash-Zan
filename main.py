import hashlib
from colorama import *

init(autoreset=True)
class Main(object):
	"""docstring for Main"""
	def __init__(self):
		super(Main, self).__init__()
		print(Fore.RED +
			"""
			██╗░░██╗░█████╗░░██████╗██╗░░██╗  ███████╗░█████╗░███╗░░██╗
			██║░░██║██╔══██╗██╔════╝██║░░██║  ╚════██║██╔══██╗████╗░██║
			███████║███████║╚█████╗░███████║  ░░███╔═╝███████║██╔██╗██║
			██╔══██║██╔══██║░╚═══██╗██╔══██║  ██╔══╝░░██╔══██║██║╚████║
			██║░░██║██║░░██║██████╔╝██║░░██║  ███████╗██║░░██║██║░╚███║
			╚═╝░░╚═╝╚═╝░░╚═╝╚═════╝░╚═╝░░╚═╝  ╚══════╝╚═╝░░╚═╝╚═╝░░╚══╝

                      Github:CodeZANKO   Telegram:ZANKO_LEGEND
			""")

		self.target_hash = input(Fore.YELLOW + "Enter Your Hash: ")
		self.hash_type = input(Fore.YELLOW + "Type Of hash (Eg:md5,sha1): ").lower()
		self.wordlist_path = input(Fore.YELLOW + "Path of wordlist: ")
		
		try:
			with open(self.wordlist_path, "r",encoding="utf-8") as wordlist_file:
				for word in wordlist_file:
					word = word.strip()
					hashed_word = self.hash_word(word)
					if hashed_word == self.target_hash:
						print(Fore.GREEN + f"Hash is Cracked: {word}")
						return
				print(Fore.RED + "Hash is Not Found Wordlist")
		except FileNotFoundError:
			print(Fore.RED + "Wordlist is Not Found")

	def hash_word(self,word):
		try:
			hash_func = getattr(hashlib,self.hash_type)
			return hash_func(word.encode()).hexdigest()
		except AttributeError:
			print(Fore.RED + f"Unsupported hash type")
			exit()



if __name__ == '__main__':
	Main()