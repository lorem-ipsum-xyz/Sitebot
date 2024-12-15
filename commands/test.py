def test(bot, data):
  message = {
    "body": "This is test only",
    "attachment": {
      "src": 'video.mp4',
      "title": 'My Fucking WELCOME'
    }
  }
  bot.sendMessage(message)

config = {
  "name": 'test',
  "def": test
}