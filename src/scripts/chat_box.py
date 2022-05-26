import amino
from time import sleep
from src import configs
from src.utils import Chats
from tabulate import tabulate
from concurrent.futures import ThreadPoolExecutor


		# -- chat box functions by azayakasa --
		
		
class ChatBox:
	def __init__(self, client: amino.Client, sub_client: amino.SubClient):
		self.client = client
		self.sub_client = sub_client
	
	
	def start(self):
		chat_id = Chats().chats(self.sub_client)
		while True:
			try:
				print(
					f"{configs.COLORS[4]}{tabulate(configs.CHAT_BOX_MENU, headers=[configs.CATEGORIES[4]], tablefmt='pipe')}"
				)
				select = int(input("Select >>> "))
				if select == 1:
					self.kick_all_users_from_chat(chat_id)
				elif select == 2:
					self.clear_chat_from_messages(chat_id)
				elif select == 3:
					duration = int(input("Duration in seconds >>> "))
					self.set_view_mode_with_timer(chat_id, duration)
				elif select == 4:
					self.copy_chat(chat_id)
				elif select == 5:
					self.invite_users_to_chat(chat_id)
				elif select == 0:
					break
			except Exception as e:
				print(e)
	
	
	def kick_all_users_from_chat(self, chat_id: str):
		with ThreadPoolExecutor(max_workers=100) as executor:
			try:
				users_count = self.sub_client.get_chat_thread(
					chatId=chat_id).membersCount
				if users_count > 10:
					chat_users = self.sub_client.get_chat_users(
						chatId=chat_id,
						start=0,
						size=100).userId
					for user_id, nickname in zip(
						chat_users.userId, chat_users.nickname):
						if user_id != self.sub_client.profile.userId:
							print("Kicked >>> {nickname}!")
							executor.submit(self.sub_client.kick, user_id, chat_id)
			except Exception as e:
				print(e)


	def clear_chat_from_messages(self, chat_id: str):
		page_token = None
		while True:
			print("Deleting messages")
			with ThreadPoolExecutor(max_workers=100) as executor:
				try:
					messages = self.sub_client.get_chat_messages(
						chatId=chat_id,
						size=100,
						pageToken=page_token)
					page_token = messages.nextPageToken
					for message_id in messages.messageId:
						executor.submit(self.sub_client.delete_message, chat_id, message_id)
				except Exception as e:
					print(e)


	def set_view_mode_with_timer(self, chat_id: str, duration: int):
		try:
			self.sub_client.edit_chat(chatId=chat_id, viewOnly=True)
			print("Chat mode is set to viewOnly")
			while duration > 0:
				print(f"{duration} seconds left")
				duration -= 1
				sleep(1)
			self.sub_client.edit_chat(chatId=chat_id, viewOnly=False)
			print("ViewOnly mode is disabled")
		except Exception as e:
			print(e)


	def copy_chat(self, chat_id: str):
		try:
			chat_info = self.sub_client.get_chat_thread(
				self.client.get_from_code(
						input("Chat link >>> ")
					).objectId
				).json
			title = chat_info["title"]
			content = chat_info["content"]
			icon = chat_info["icon"]
			keywords = chat_info["keywords"]
			chat_style = chat_info["extensions"]
			fans_only = chat_style["fansOnly"]
			background_image = chat_style["bm"][1]
			self.sub_client.edit_chat(
				chatId=chat_id,
				title=title,
				content=content,
				icon=icon,
				keywords=keywords,
				fansOnly=fans_only)
			print("Copied chat")
		except Exception as e:
			print(e)
	
	
	def invite_users_to_chat(self, chat_id: str):
		while True:
			with ThreadPoolExecutor(max_workers=100) as executor:
				try:
					online_users = self.sub_client.get_online_users(start=0, size=100)
					for user_id, nickname in zip(
							online_users.profile.userId, online_users.nickname):
						print(f"Invited >>> {nickname} to chat")
						executor.submit(self.sub_client.invite_to_chat, user_id, chat_id)]
                except Exception as e:
                      print(e)
                      
                      
		# -- chat box functions by azayakasa --

