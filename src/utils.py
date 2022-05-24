import amino
from src import configs
from tabulate import tabulate

class Login:
	@staticmethod
	def login(client: amino.Client):
		try:
			print(tabulate(configs.LOGIN_MENU, headers=[configs.CATEGORIES[7]], tablefmt="fancy_grid"))
			select = int(input("[Select]::: "))
			if select == 1:
				email = input("[Email]::: ")
				password = input("[Password]::: ")
				client.login(email=email, password=password)
			elif select == 2:
				client.login_sid(input("[SID]::: "))
			except Exception as e:
				print(e)
			
					
class Communities:
	@staticmethod
	def communities(client: amino.Client):
		while True:
			try:
				clients = client.sub_clients(start=0, size=100)
				for x, name in enumerate(clients.name, 1):
					print(f"[{x}][{name}]")
				return clients.comId[int(input("[Select the community]::: ")) - 1]
			except Exception as e:
				print(e)

class Chats:
	@staticmethod
	def chats(sub_client: amino.SubClient):
		while True:
			try:
				chats = sub_client.get_chat_threads(start=0, size=100)
				for z, title in enumerate(chats.title, 1):
					print(f"[{z}][{title}]")
				return chats.chatId[int(input("[Select the chat]::: ")) - 1]
			except Exception as e:
				print(e)

