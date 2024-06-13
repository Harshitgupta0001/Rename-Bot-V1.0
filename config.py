import re, os

id_pattern = re.compile(r'^.\d+$') 

API_ID = os.environ.get("API_ID", "21551881")

API_HASH = os.environ.get("API_HASH", "6e83e9e1aee5accd4868dc29aa59ebaa")

BOT_TOKEN = os.environ.get("BOT_TOKEN", "7092980872:AAFBjX87iiFT_KpUher6vEslGeTxOKY_ZGg") 

FORCE_SUB = os.environ.get("FORCE_SUB", "moviesworldupdate") 

DB_NAME = os.environ.get("DB_NAME","harshit")     

DB_URL = os.environ.get("DB_URL","mongodb+srv://david:surya@cluster0.s7o0tyw.mongodb.net/")
 
FLOOD = int(os.environ.get("FLOOD", "10"))

START_PIC = os.environ.get("START_PIC", "https://graph.org/Rename-Bot-01-15")

ADMIN = [int(admin) if id_pattern.search(admin) else admin for admin in os.environ.get('ADMIN', '6359874284').split()]

PORT = os.environ.get("PORT", "8080")
