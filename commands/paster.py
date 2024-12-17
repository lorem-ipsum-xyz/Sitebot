import requests
from bs4 import BeautifulSoup

def Request(paste):
  try:
    session = requests.Session()
    url = "https://pastebin.mozilla.org";
    
    headers = {
      "Content-Type": 'application/x-www-form-urlencoded',
      "User-Agent": 'Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/131.0.0.0 Mobile Safari/537.36',
      "Referer": url
    }
    data = {}
    
    res = session.get(url).content
    soup = BeautifulSoup(res, 'html.parser')
    form = soup.find('form')
    token = form.find('input', attrs={"name":"csrfmiddlewaretoken"}).get('value')
    
    data["csrfmiddlewaretoken"] = token
    data["title"] = ''
    data["lexer"] = '_text'
    data["expires"] = 86400
    data["content"] = paste
    
    response = session.post(url, data=data, headers=headers)
    resHtml = BeautifulSoup(response.content, 'html.parser')
    
    ul = resHtml.find('ul',id="snippetOptions")
    resTitle = resHtml.find('title').getText()
    
    expire = ul.find('li',class_='option-type').getText().split('in: ')[1].strip()
    path = resTitle.split('Pastebin')[1].split(' ')[0]
    text = ul.find("textarea", id="copySnippetSource").getText()
    return {
      "path": path,
      "text": text,
      "expire": ' '.join(expire.split('\xa0'))
    }
  except Exception as e:
    print("Exception: ", e)
    return None

def Paster(bot, data):
  if not data.args:
    return bot.sendMessage("⚠️ No text provided. Please use the format /paster <text>.")
  loading = bot.sendMessage("⏳ Pasting your text, please wait...")
  yui = Request(data.args)
  bot.unsendMessage(loading['id'])
  if not yui:
    return bot.sendMessage("⚠️ An error accured while pasting the text")
  message = ""
  message += f"expires in: {yui['expire']}\n\n"
  message += f"Path: ![/paster{yui['path']}](/paster{yui['path']})"
  bot.sendMessage(message)

config = {
  "name": 'paster',
  "credits": 'Greegmon',
  "def": Paster,
  "usage": f"/paster <text>",
  "description": "Paste your text and allow other to see it"
}