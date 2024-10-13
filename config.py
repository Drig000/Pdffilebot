env_vars = {
  # Get From my.telegram.org
  "API_HASH": "388d7300dddeff471f69dfa766a9dbb6",
  # Get From my.telegram.org
  "API_ID": "27939550",
  #Get For @BotFather
  "BOT_TOKEN": "6955924195:AAEzLmDrjRgE115gmY6ZYx6qWDUqCbYXE-w",
  # Get For tembo.io
  "DATABASE_URL_PRIMARY": "postgresql://postgres:5mprSh6FcEAkbXcF@owlishly-guiding-boar.data-1.use1.tembo.io:5432/postgres",
  # Logs Channel Username Without @
  "CACHE_CHANNEL": "",
  # Force Subs Channel username without @
  "CHANNEL": "",
  # {chap_num}: Chapter Number
  # {chap_name} : Manga Name
  # Ex : Chapter {chap_num} {chap_name} @Manhwa_Arena
  "FNAME": "",
  # Put Thumb Link 
  "THUMB": ""
}

dbname = env_vars.get('DATABASE_URL_PRIMARY') or env_vars.get('DATABASE_URL') or 'sqlite:///test.db'

if dbname.startswith('postgres://'):
    dbname = dbname.replace('postgres://', 'postgresql://', 1)
    
