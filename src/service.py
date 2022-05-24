import amino
from tabulate import tabulate
from src import configs
from src.utils import Login
from src.utils import Communities
from src.utils import Chats
from scripts.raid_box import RaidBox
from scripts.activity_box import ActivityBox
from scripts.profile_box import ProfileBox
from scripts.chat_box import ChatBox
from scripts.other_box import OtherBox
from scripts.account_box import AccountBox


class MainApp:
	def start(self):
		self.client = amino.Client()
		Login().login(self.client)
		self.sub_client = amino.SubClient(
			comId=Communities().communities(
			self.client), profile=self.client.profile)
		while True:
			try:
				print(
					tabulate(
						configs.MAIN_MENU,
						headers=[
							"",
							configs.CATEGORIES[0],
							"Authors"],
						tablefmt="fancy_grid"))
				select = int(input("[Select]::: "))
				if select == 1:
					RaidBox(self.client, self.sub_client).start()
				elif select == 2:
					ActivityBox(self.sub_client).start()
				elif select == 3:
					ProfileBox(self.client, self.sub_client).start()
				elif select == 4:
					ChatBox(self.client, self.sub_client).start()
				elif select == 5:
					OtherBox(self.client, self.sub_client).start()
				elif select == 6:
					AccountBox(self.client).start()
			except Exception as e:
				print(e)
