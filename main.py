import amino
from json import loads
from src import configs
from requests import get
from src.service import MainApp


def main():
	info = get("https://github.com/deluvsushi/Amino-Boxes/raw/master/version.json").text
	version = info["version"]
	authors = info["authors"]
	github = info["github"]
	telegram = info["telegram"]
	current_version = loads(open("version.json").read())["version"]
	if version != current_version:
		print(
			f"{configs.COLORS[5]}[New version of Amino-Boxes is available!]::: {version}"
		)
	print(
		f"""{configs.COLORS[5]}{configs.LOGO}
[Tell my mom that I'm sorry
I'm just fucking flossing]
[Authors]::: {authors}
[Version]::: {current_version}
[GitHub]::: {github}
[Telegram]::: {telegram}
"""
	)
	try:
		MainApp().start()
	except Exception as e:
		print(e)


if __name__ == "__main__":
	main()
