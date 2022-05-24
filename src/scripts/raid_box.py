import amino
from src import configs
from src.utils import Chats
from tabulate import tabulate
from concurrent.futures import ThreadPoolExecutor
		
		
		# -- raid box functions by deluvsushi --


class RaidBox:
	def __init__(self, client: amino.Client, sub_client: amino.SubClient):
		self.client = client
		self.sub_client = sub_client


	def start(self):
		while True:
			try:
				print(
					f"{configs.COLORS[5]}{tabulate(configs.RAID_BOX_MENU, headers=[configs.CATEGORIES[1]], tablefmt='fancy_grid')}"
				)
				select = int(input("[Select = "))
				if select == 1:
					self.spam_wall_with_comments()
				elif select == 2:
					self.spam_blog_with_comments()
				elif select == 3:
					self.spam_chat_with_messages()
				elif select == 4:
					self.kick_user_from_chat()
				elif select == 0:
					break
			except Exception as e:
				print(e)


	def spam_wall_with_comments(self):
		user_id = self.client.get_from_code(input("[User link]:::")).objectId
		message = input("[Message]::: ")
		while True: 
			self.sub_client.comment(message=message, userId=user_id)
			print("[Comment is sent!]")
	
	def spam_blog_with_comments(self):
		blog_id = self.client.get_from_code(input("[Blog link]:::")).objectId
		message = input("[Message]::: ")
		while True: 
			self.sub_client.comment(message=message, blogId=blog_id)
			print("[Comment is sent!]")
	
	
	def spam_chat_with_messages(self):
		chat_id = Chats().chats(self.sub_client)
		message = input("[Message]::: ")
		message_type = int(input("[Message type]::: "))
		while True:
			with ThreadPoolExecutor(max_workers=100) as executor:
				[executor.submit(
					self.sub_client.send_message,
					chat_id,
					message,
					message_type) for _ in range(100_000_000)]
	
	
	def kick_user_from_chat(self):
		chat_id = Chats().chats(self.sub_client)
		user_id = self.client.get_from_code(input("-- [User link]:::")).objectId
		try:
			self.sub_client.kick(chatId=chat_id, userId=user_id)
			print("[Kicked user from chat!]")
		except Exception as e:
			print(e)
			
		
		# -- raid box functions by deluvsushi --
