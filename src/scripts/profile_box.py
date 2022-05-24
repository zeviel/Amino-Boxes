import amino
from io import BytesIO
from src import configs
from requests import get
from tabulate import tabulate
from concurrent.futures import ThreadPoolExecutor


		# -- profile box functions by savier --


class ProfileBox:
	def __init__(self, client: amino.Client, sub_client: amino.SubClient):
		self.client = client
		self.sub_client = sub_client


	def start(self):
		while True:
			try:
				print(
					f"{configs.COLORS[1]}{tabulate(configs.PROFILE_BOX_MENU, headers=[configs.CATEGORIES[3]], tablefmt='rst')}"
				)
				select = int(input("Select:- "))
				if select == 1:
					self.copy_profile()
				elif select == 2:
					self.copy_blog()
				elif select == 3:
					self.clear_profile_from_blogs()
				elif select == 4:
					self.clear_profile_wall_from_comments()
				elif select == 0:
					break
			except Exception as e:
				print(e)


	def copy_profile(self):
		user_id = self.client.get_from_code(input("User link:- ")).objectId
		user_info = self.sub_client.get_user_info(userId=user_id).json
		icon = BytesIO(get(user_info["icon"]).content)
		profile_style = user_info["extensions"]["style"]
		image_list = [
			BytesIO(get(str(user_info["mediaList"]).split("'")[1]).content)]
		if "backgroundColor" in profile_style:
			self.sub_client.edit_profile(
				backgroundColor=profile_style["backgroundColor"])
		elif "backgroundMediaList" in profile_style:
			self.sub_client.edit_profile(
				backgroundImage=str(profile_style["backgroundMediaList"]).split("'")[1])
		self.sub_client.edit_profile(
			nickname=user_info["nickname"],
			content=user_info["content"],
			icon=icon,
			imageList=image_list)
		print("Successfully copied profile!")


	def copy_blog(self):
		blog_id = self.client.get_from_code(input("Blog link:- ")).objectId
		blog_info = self.sub_client.get_blog_info(blogId=blog_id).json["blog"]
		blog_style = blog_info["extensions"]["style"]
		captions_and_images = str(blog_info["mediaList"]).split()
		image_list = []
		caption_list = []
		for caption in captions_and_images:
			if "']" in caption:
				caption_list.append(caption.strip("'],"))
		for image in captions_and_images:
			if "http" in image:
				image_list.append(BytesIO(get(image.strip("',")).content))
		if "backgroundColor" in blog_style:
			self.sub_client.post_blog(
				title=blog_info["title"],
				content=blog_info["content"],
				imageList=image_list,
				captionList=caption_list,
				backgroundColor=blog_style["backgroundColor"])
		elif "backgroundMediaList" in blog_style:
			background_image = [
				[100, str(blog_style["backgroundMediaList"]).split("'")[1], None]]
			self.sub_client.post_blog(
				title=blog_info["title"],
				content=blog_info["content"],
				imageList=image_list,
				captionList=caption_list,
				extensions={
					"style": {
						"backgroundMediaList": background_image}})
		print("Successfully copied blog!")


	def clear_profile_from_blogs(self):
		with ThreadPoolExecutor(max_workers=100) as executor:
			try:
				blogs_count = self.sub_client.get_user_info(
					userId=self.sub_client.profile.userId).blogsCount
				if blogs_count > 0:
					created_blogs = self.sub_client.get_user_blogs(
						userId=self.sub_client.profile.userId, start=0, size=100).blogId
					for blog_id in created_blogs:
						executor.submit(self.sub_client.delete_blog, blog_id)
				elif blogs_count == 0:
					print("Deleted all blogs!")
			except Exception as e:
				print(e)


	def clear_profile_wall_from_comments(self):
		with ThreadPoolExecutor(max_workers=100) as executor:
			try:
				comments_count = self.sub_client.get_user_info(
					userId=self.sub_client.profile.userId).commentsCount
				if comments_count > 0:
					wall_comments = self.sub_client.get_wall_comments(
						userId=self.sub_client.profile.userId,
						sorting="newest",
						start=0,
						size=100).commentId
					for comment_id in wall_comments:
						executor.submit(
							self.sub_client.delete_comment,
							comment_id,
							self.sub_client.profile.userId)
				elif comments_count == 0:
					print("Deleted all comments!")
			except Exception as e:
				print(e)

	
		# -- profile box functions by savier --
		
		
