
COLORS = [
	"\033[38;5;196m", # RED
	"\033[38;5;113m", # GREEN
	"\033[38;5;137m", # BROWN
	"\033[38;5;214m", # ORANGE 
	"\033[38;5;45m", # LIGHT_BLUE
	"\033[38;5;36m" # DARK GREEN
]

AUTHORS = [
	"deluvsushi",
	"Savier",
	"Azayakasa",
	"Auroraflow",
	"Roger",
	"Morphine",
	"Moriarti"
]
CATEGORIES = [
	"Main Menu",
	"Raid Box",
	"Activity Box",
	"Profile Box",
	"Chat Box",
	"Other Box",
	"Account Box",
	"Login Menu"
]

LOGO = """
▄▄▄       ███▄ ▄███▓ ██▓ ███▄    █  ▒█████   ▄▄▄▄    ▒█████  ▒██   ██▒▓█████   ██████ 
▒████▄    ▓██▒▀█▀ ██▒▓██▒ ██ ▀█   █ ▒██▒  ██▒▓█████▄ ▒██▒  ██▒▒▒ █ █ ▒░▓█   ▀ ▒██    ▒ 
▒██  ▀█▄  ▓██    ▓██░▒██▒▓██  ▀█ ██▒▒██░  ██▒▒██▒ ▄██▒██░  ██▒░░  █   ░▒███   ░ ▓██▄   
░██▄▄▄▄██ ▒██    ▒██ ░██░▓██▒  ▐▌██▒▒██   ██░▒██░█▀  ▒██   ██░ ░ █ █ ▒ ▒▓█  ▄   ▒   ██▒
 ▓█   ▓██▒▒██▒   ░██▒░██░▒██░   ▓██░░ ████▓▒░░▓█  ▀█▓░ ████▓▒░▒██▒ ▒██▒░▒████▒▒██████▒▒
 ▒▒   ▓▒█░░ ▒░   ░  ░░▓  ░ ▒░   ▒ ▒ ░ ▒░▒░▒░ ░▒▓███▀▒░ ▒░▒░▒░ ▒▒ ░ ░▓ ░░░ ▒░ ░▒ ▒▓▒ ▒ ░
  ▒   ▒▒ ░░  ░      ░ ▒ ░░ ░░   ░ ▒░  ░ ▒ ▒░ ▒░▒   ░   ░ ▒ ▒░ ░░   ░▒ ░ ░ ░  ░░ ░▒  ░ ░
  ░   ▒   ░      ░    ▒ ░   ░   ░ ░ ░ ░ ░ ▒   ░    ░ ░ ░ ░ ▒   ░    ░     ░   ░  ░  ░  
      ░  ░       ░    ░           ░     ░ ░   ░          ░ ░   ░    ░     ░  ░      ░  
                                                   ░                                   
"""

LOGIN_MENU = [
	[1, "Login with email & password"],
	[2, "Login with sid"]
]

MAIN_MENU = [
	[1, "Raid Box", f"By {AUTHORS[0]}"],
	[2, f"{COLORS[0]}Activity Box", f"By {AUTHORS[0]}"],
	[3, f"{COLORS[1]}Profile Box", f"By {AUTHORS[1]}"],
	[4, f"{COLORS[4]}Chat Box", f"By {AUTHORS[2]}"],
	[5, f"{COLORS[3]}Other Box", f"By {AUTHORS[3]} & {AUTHORS[4]}"],
	[6, f"{COLORS[2]}Account Box", f"By {AUTHORS[5]} & {AUTHORS[6]}"]
]

RAID_BOX_MENU = [ 
	[1, f"{COLORS[5]}Spam wall with comments"],
	[2, "Spam blog with comments"],
	[3, "Spam chat with messages"],
	[4, "Kick user from chat"]
]

ACTIVITY_BOX_MENU = [
	[1, f"{COLORS[0]}Follow online users"],
	[2, "Unfollow from followed users"],
	[3, "Like recent blogs"],
	[4, "Play quizzes"]
]

PROFILE_BOX_MENU = [
	[1, f"{COLORS[1]}Copy profile"],
	[2, "Copy blog"],
	[3, "Clear profile from blogs"],
	[4, "Clear profile wall from comments"]
]

CHAT_BOX_MENU = [
	[1, f"{COLORS[4]}Kick all users from chat"],
	[2, "Clear chat from messages"],
	[3, "Set view mode with timer"],
	[4, "Copy chat"]
]

OTHER_BOX_MENU = [
	[1, f"{COLORS[3]}Send system message"],
	[2, "Get community info"],
	[3, "Check in all communities"]
]

ACCOUNT_BOX_MENU = [
	[1, f"{COLORS[2]}Get account info"],
	[2, "Get blocker users"],
	[3, "Get blocked users"]
]
