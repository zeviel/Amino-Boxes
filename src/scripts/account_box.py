import amino
from src import configs
from tabulate import tabulate

		
		# -- account box functions by morphine & morirarti --


class AccountBox:
	def __init__(self, client: amino.Client):
		self.client = client


	def start(self):
		while True:
			try:
				print(
					tabulate(
						configs.ACCOUNT_BOX_MENU,
						headers=[configs.CATEGORIES[6]],
						tablefmt="fancy_grid"))
				select = int(input(">> Select-: "))
				if select == 1:
					self.get_account_info()
				elif select == 2:
					self.get_blocker_users()
				elif select == 3:
					self.get_blocked_users()
				elif select == 0:
					break
			except Exception as e:
				print(e)
	
	
	def get_account_info(self):
		account_info = self.client.get_account_info().json
		email = account_info["email"]
		user_id = account_info["uid"]
		phone_number = account_info["phoneNumber"]
		amino_id = account_info["aminoId"]
		created_time = account_info["createdTime"]
		print(
			f"""
>> email-: {email}
>> userId-: {user_id}
>> phoneNumber-: {phone_number}
>> aminoId-: {amino_id}
>> createdTime-: {created_time}
"""
	)


	def get_blocker_users(self):
		try:
			blocker_users = self.client.get_blocker_users(
				start=0, size=100)
			for user_id in blocker_users:
				nickname = self.client.get_user_info(userId=user_id).nickname
				print(
					f">> userId-: {user_id}, nickname-: {nickname}"
				)
		except Exception as e:
			print(e)


	def get_blocked_users(self):
		try:
			blocked_users = self.client.get_blocked_users(
				start=0, size=100)
			for user_id, nickname in zip(
					blocked_users.userId, blocked_users.nickname):
				print(
					f">> userId-: {user_id}, nickname-: {nickname}"
				)
		except Exception as e:
			print(e)
	
		
		# -- account box functions by morphine & morirarti --
		
		
