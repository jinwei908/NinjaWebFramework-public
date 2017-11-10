from mongoengine import Document, EmbeddedDocument, fields

class ToolInput(EmbeddedDocument):
    value = fields.StringField(required=True)
    name = fields.StringField(required=True)

class ImageInstance(EmbeddedDocument):
    username = fields.StringField(required=False)
    logged_user = fields.StringField(required=False)
    image_secure_url = fields.StringField(required=False)
    computer_name = fields.StringField(required=False)
    log_time = fields.StringField(required=False)
    
class HostActivityInstance(EmbeddedDocument):
    _id = fields.StringField(required=False)
    count = fields.IntField(required=False)
    
class PacketDataInstance(EmbeddedDocument):
    username = fields.StringField(required=False)
    click_count = fields.IntField(required=False)
    computer_name = fields.StringField(required=False)
    all_tags = fields.ListField(required=False)
    current_window = fields.StringField(required=False)
    log_time = fields.DateTimeField(required=False)
    logged_user = fields.StringField(required=False)
    string_content = fields.StringField(required=False)
    
    
class TagCountInstance(EmbeddedDocument):
    _id = fields.StringField(required=False)
    General = fields.IntField(required=False)
    WhatsApp = fields.IntField(required=False)
    YouTube = fields.IntField(required=False)
    GoogleChrome = fields.IntField(required=False)
    Instagram = fields.IntField(required=False)
    InternetExplorer = fields.IntField(required=False)
    Firefox = fields.IntField(required=False)
    Gmail = fields.IntField(required=False)
    MicrosoftWord = fields.IntField(required=False)
    MicrosoftPowerpoint = fields.IntField(required=False)
    Steam = fields.IntField(required=False)
    MicrosoftVisualStudio = fields.IntField(required=False)
    Hotmail = fields.IntField(required=False)
    Unity = fields.IntField(required=False)
    GoogleSearch = fields.IntField(required=False)
    Forums = fields.IntField(required=False)
    Telegram = fields.IntField(required=False)
    Outlook = fields.IntField(required=False)
    Excel = fields.IntField(required=False)
    AdobeReader = fields.IntField(required=False)
    Skype = fields.IntField(required=False)
    OpenOffice = fields.IntField(required=False)
    VLCMediaPlayer = fields.IntField(required=False)
    LiveMessenger = fields.IntField(required=False)
    ITunes = fields.IntField(required=False)
    Search = fields.IntField(required=False)
    Amazon = fields.IntField(required=False)
    eBay = fields.IntField(required=False)
    Paypal = fields.IntField(required=False)
    Pinterest = fields.IntField(required=False)
    Wikipedia = fields.IntField(required=False)
    Twitter = fields.IntField(required=False)
    Spotify = fields.IntField(required=False)
    Qoo10 = fields.IntField(required=False)
    LinkedIn = fields.IntField(required=False)
    Tumblr = fields.IntField(required=False)
    Reddit = fields.IntField(required=False)
    Quora = fields.IntField(required=False)
    Bing = fields.IntField(required=False)
    Yahoo = fields.IntField(required=False)
    Taobao = fields.IntField(required=False)
    Netflix = fields.IntField(required=False)
    Porn = fields.IntField(required=False)
    Sex = fields.IntField(required=False)
    SoundCloud = fields.IntField(required=False)
    Twitch = fields.IntField(required=False)
    StackOverflow = fields.IntField(required=False)
    Adobe = fields.IntField(required=False)
    Acrobat = fields.IntField(required=False)
    Photos = fields.IntField(required=False)
    Login = fields.IntField(required=False)
    Hotel = fields.IntField(required=False)
    Accounting = fields.IntField(required=False)
    Dropbox = fields.IntField(required=False)
    Netflix = fields.IntField(required=False)