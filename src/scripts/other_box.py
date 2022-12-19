import amino
from src import configs
from src.utils import Chats
from tabulate import tabulate
from concurrent.futures import ThreadPoolExecutor
		
		
		# -- other box functions by auroraflow & roger --
		

class OtherBox:
	def __init__(self, client: amino.Client, sub_client: amino.SubClient):
		self.client = client
		self.sub_client = sub_client


	def start(self):
		while True:
			try:
				print(
					f"{configs.COLORS[3]}{tabulate(configs.OTHER_BOX_MENU, headers=[configs.CATEGORIES[5]], tablefmt='grid')}"
				)
				select = int(input("[Select = "))
				if select == 1:
					self.send_system_message()
				elif select == 2:
					self.get_community_info()
				elif select == 3:
					self.check_in_all_communities()
				elif select == 0:
					break
			except Exception as e:
				print(e)


	def send_system_message(self):
		chat_id = Chats.chats(self.sub_client)
		while True:
			try:
				self.sub_client.send_message(
					chatId=chat_id,
					message=input("Message - "),
					messageType=int(input("Message type - ")))
				print("[Message is sent!")
			except Exception as e:
				print(e)


	def get_community_info(self):
		com_id = self.client.get_from_code(
				input("[Community link = ")).json["extensions"]["community"]["ndcId"]
		community_info = self.client.get_community_info(comId=com_id).json
		icon = community_info["icon"]
		tagline = community_info["tagline"]
		endpoint = community_info["endpoint"]
		content = community_info["content"]
		created_time = community_info["createdTime"]
		community_cover = str(community_info["promotionalMediaList"]).split("'")[1]
		print(
			f"""
[Community icon link = {icon}
[Community cover link = {community_cover}
[Community tagline = {tagline}
[Community endpoint = {endpoint}
[Community created time = {created_time}
"""
	)


	def check_in_all_communities():
		try:
			clients = self.client.sub_clients(start=0, size=100).comId
			with ThreadPoolExecutor(max_workers=100) as executor:
				for com_id in clients:
					self.sub_client = amino.SubClient(
						comId=com_id, profile=self.client.profile)
					executor.submit(
						self.sub_client.check_in,
						self.sub_client.lottery)
				print("[Checked in all communities!")
		except Exception as e:
			print(e)
	
	
		# -- other box functions by auroraflow & roger --
	
	
