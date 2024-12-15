import os
import config
import secrets
import mimetypes
from dataclasses import dataclass

class Bot:
  def __init__(self):
    self.__io = config.io
    
    self.prefix = config.PREFIX
    self.commands = config.COMMANDS
    self.developer = config.DEVELOPER
  def __file(self,file_path):
    mime_type, encoding = mimetypes.guess_type(file_path)
    if mime_type:
      return mime_type.split('/')[0]
    else:
      return 'invalid'
  def sendMessage(self, datos):
    messageID = f"MSG-{secrets.token_hex(20)}"
    data = {
      "id": messageID,
      "data": {}
    }
    if type(datos) == str:
      data["data"] = {"body":datos}
    if type(datos) == dict:
      if "body" in datos:
        data["data"]["body"] = datos["body"]
      base = datos["attachment"]
      if type(base) == dict:
        house1 = list()
        house2 = base
        if 'type' not in base:
          house2['type'] = self.__file(base['src'])
        house1.append(house2)
        data["data"]["attachment"] = house1
      if type(base) == list:
        bahay1 = list()
        for attch in base:
          bahay2 = attch
          if 'type' not in attch:
            bahay2['type'] = self.__file(attch['src'])
          bahay1.append(bahay2)
        data["data"]["attachment"] = bahay1
    self.__io.emit('sendMessage',data)
    return {"id": messageID}
  def unsendMessage(self, messageID):
    self.__io.emit('unsendMessage', {
      "id": messageID
    })

@dataclass
class Data:
  cmd: str
  args: str
  prefix: str =  config.PREFIX
  developer: str = config.DEVELOPER

def messageHandler(txt):
  bot = Bot()
  
  if not txt.startswith(config.PREFIX):
    return
  if len(txt) == 1:
    return
  
  text = txt[1:].split()
  cmd, args = [text[0], ' '.join(text[1:])] if len(text)>=1 else [text,'']
  
  if cmd not in config.COMMANDS:
    return bot.sendMessage(f"⚠️ Command '{cmd}' not found.")
    
  function = config.COMMANDS[cmd]["def"]
  data = Data(
    cmd = cmd,
    args = args
  )
  function(bot, data)