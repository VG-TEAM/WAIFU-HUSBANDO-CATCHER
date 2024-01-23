class Config(object):
    LOGGER = True

    # Get this value from my.telegram.org/apps
    OWNER_ID = "5932230962"
    sudo_users = "6375797149", "5778743582", "5396889141", "5852831718", "6375797149"
    GROUP_ID = -1002134558679
    TOKEN = "6437630510:AAHJ7qBp6vkCUIkP4T9p3e8eRgikSvuLEfo"
    mongo_url = "mongodb+srv://tanjiro1564:tanjiro1564@cluster0.pp5yz4e.mongodb.net/?retryWrites=true&w=majority"
    PHOTO_URL = ["https://telegra.ph/file/b925c3985f0f325e62e17.jpg", "https://telegra.ph/file/4211fb191383d895dab9d.jpg"]
    SUPPORT_CHAT = "VG_SUPPORT_CHAT"
    UPDATE_CHAT = "TEAMS_VG"
    BOT_USERNAME = "Waifu_x_robot"
    CHARA_CHANNEL_ID = "-1002134558679"
    api_id = 26626068
    api_hash = "bf423698bcbe33cfd58b11c78c42caa2"

    
class Production(Config):
    LOGGER = True


class Development(Config):
    LOGGER = True
