from bs4 import BeautifulSoup
from requests import get

def getVerse():
  try:
    url = "https://dailyverses.net/random-bible-verse"
    res = get(url)
    soup = BeautifulSoup(res.content, 'html.parser')
    
    content = soup.find('div',class_='content')
    b1 = content.find('div',class_='b1')
    
    text = b1.find('span',class_='v1').getText()
    verse = b1.find('a',class_='vc').getText()
    message = f"{text}\n\n- {verse}"
    return message
  except Exception as e:
    print("ERROR: ", e)
    return "⚠️ Error while getting a random verse"

def bible(bot, data):
  if data.args:
    return bot.sendMessage("⚠️ This command dont need an argument")
  loading = bot.sendMessage("⏳ Fetching data, please wait...")
  bible = getVerse()
  bot.unsendMessage(loading['id'])
  bot.sendMessage(bible)

config = {
  "name": 'bible',
  "credits": "Greegmon",
  "description": "Generate a random bible verse",
  "def": bible
}