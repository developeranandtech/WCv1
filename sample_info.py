# Bot information
SESSION = 'WatchingCenterbot'
USER_SESSION = 'User_Bot'
API_ID = 12345
API_HASH = '0123456789abcdef0123456789abcdef'
BOT_TOKEN = '123456:WatchingCenterbot-zyx57W2v1u123ew11'
USERBOT_STRING_SESSION = 'WatchingCenterbot'

# Bot settings
CACHE_TIME = 300
USE_CAPTION_FILTER = False

# Admins, Channels & Users
ADMINS = [12345789, 'admin123', 987654321]
CHANNELS = [-10012345678, -100987654321, 'WatchingCenter']
AUTH_USERS = []
AUTH_CHANNEL = None

# MongoDB information
DATABASE_URI = "mongodb://[WatchingCenterbot:WatchingCenterbot@]host1[:port1][,...hostN[:portN]][/[defaultauthdb]?retryWrites=true&w=majority"
DATABASE_NAME = 'WatchingCenterbot'
COLLECTION_NAME = 'channel_files'  # If you are using the same database, then use different collection name for each bot

# Messages
START_MSG = """
**Hi, I'm Media Search bot**

Here you can search files in inline mode. Just press follwing buttons and start searching.
"""

SHARE_BUTTON_TEXT = 'Checkout {username} for searching files'
INVITE_MSG = 'Please join @.... to use this bot'
