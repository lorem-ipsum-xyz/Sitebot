import requests

def fact(bot, data):
  if data.args:
    return bot.sendMessage("⚠️ This command dont need an argument")
  load = bot.sendMessage("⏳ Fetching random fact.")
  try:
    res = requests.get("https://uselessfacts.jsph.pl/api/v2/facts/random")
    bot.unsendMessage(load['id'])
    if not res.status_code == 200:
      return bot.sendMessage("⚠️ An error accured while fetching the data")
    data = res.json()
    bot.sendMessage(data['text'])
  except Exception as e:
    print("Error: ", e)
    bot.sendMessage(e)

config = {
  "name": 'fact',
  "def": fact,
  "credits": "Greegmon",
  "description": "Generate a random facts"
}