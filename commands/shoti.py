from requests import post
from random import choice
from bs4 import BeautifulSoup
import json

def getShoti(link):
  try:
    url = "https://ttsave.app/download"
    headers = {"Content-Type": 'application/json',"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36"}
    data = {"query": link,"languange_id": "1"}
    
    res = post(url, json=data, headers=headers, timeout=10)
    html = BeautifulSoup(res.content, 'html.parser')
    
    buttons = html.find('div', id='button-download-ready')
    mdiv = html.find('div', class_="flex flex-row items-center justify-center gap-1 mt-5 w-3/4")
    row = html.find('div',class_="flex flex-row items-center justify-center gap-2 mt-2")
    
    if html.text == 'Error unknown':
      return {"error": "⚠️ Error while proccessing the data"}
    cols = row.find_all('div',class_='flex-row')
    
    username = html.find('a', class_="font-extrabold text-blue-400 text-xl mb-2").text
    description = html.find('p', class_="text-gray-600 px-2 text-center break-all w-3/4 oneliner").text or 'No description'
    views = cols[0].text.strip() or '0'
    comments = cols[2].text.strip() or '0'
    shares = cols[4].text.strip() or '0'
    music = mdiv.find('span', class_="text-gray-500").text or 'unknown'
    videoLink = html.find('a', attrs={'type':"no-watermark"}).get('href')
    data = {
      "username": username,
      "description": description,
      "views": views,
      "comments": comments,
      "shares": shares,
      "music": music,
      "videoSource": videoLink
    }
    print(data)
    return data
  except Exception as e:
    print("ERROR: ", e)
    return {"error": str(e)}

def shoti(bot, data):
  if data.args:
    return bot.sendMessage("⚠️ This command dont need an argument.")
  loading = bot.sendMessage("⏳ Generating a random shoti video...")
  try:
    jayson = json.load(open('commands/cache/shoti.json', 'r'))
    print(jayson)
    print(res)
    res = getShoti(choice(jayson['link']))
    if "error" in res:
      bot.unsendMessage(loading['id'])
      return bot.sendMessage(res['error'])#("⚠️ An error accured while fetching the data, please try again.")
    line = "━━━━━━━━━━━━━━━"
    text = line + '\n'
    text += "username: " + res.get('username') + '\n'
    text += "views: " + res.get('views') + '\n'
    text += "comments: " + res.get('comments') + '\n'
    text += "shares: " + res.get('shares') + '\n'
    text += "music: " + res.get('music') + '\n'
    text += line + '\n'
    text += res.get('description') if res.get('description') != 'No description' else ''
    message = {
      "body": text,
      "attachment": {
        "src": res['videoSource'],
        "type": 'video'
      }
    }
    bot.unsendMessage(loading['id'])
    return bot.sendMessage(message)
  except Exception as e:
    print("ERROR: ", e)
    bot.unsendMessage(loading['id'])
    return bot.sendMessage("⚠️ An error accured while fetching the data, please try again.")

config = {
  "name": 'shoti',
  "def": shoti,
  "description": 'Generate a random sexy girl videos',
  "credits": 'Greegmon'
}