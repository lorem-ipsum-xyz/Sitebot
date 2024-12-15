from config import COMMANDS, PREFIX
from . import font

def get_page(commands, page=1):
  if page > len(commands):
    return f"⚠️ Page not found, total command page is {len(commands)}"
  message = font('bold',"Command Lists\n")
  message += "━━━━━━━━━━━━━━━\n"
  for cmd in commands[page-1]:
    message += f"{PREFIX}{cmd['name']} - {cmd['description']}\n"
  message += "━━━━━━━━━━━━━━━\n"
  message += f"'/help <page>' to see other command.\n"
  message += f"{font('bold','PAGE')}: ({page}/{len(commands)})"
  return message

def get_all(commands):
  message = font('bold',"Command Lists\n")
  message += "━━━━━━━━━━━━━━━\n"
  for command in commands:
    for cmd in command:
      message += f"{PREFIX}{cmd['name']} - {cmd['description']}\n"
  message += "━━━━━━━━━━━━━━━\n"
  return message

def get_command(commands, name):
  for command in commands:
    for cmd in command:
      if cmd['name'] == name:
        message = f"━━━━━( {font('bold', name)} )━━━━━\n"
        message += f"{font('bold', 'Credits')}: {cmd['credits']}\n"
        message += f"{font('bold', 'Usage')}: {cmd['usage']}\n"
        message += f"{font('bold', 'Description')}: {cmd['description']}"
        return message
  return f"⚠️ Command '{name}' not found."

def help(bot, data):
  _cmdArray = [{
    "name": v.get('name'),
    "def": v.get('def'),
    "usage": v.get('usage', f"{PREFIX}{v['name']}") or f"{config.PREFIX}{v['name']}",
    "description": v.get('description', 'No description!') or 'No discription!',
    "credits": v.get('credits')
  } for key,v in COMMANDS.items()]
  
  commands = [_cmdArray[i:i+10] for i in range(0, len(_cmdArray), 10)]
  args = data.args
  isPage = True
  
  if not args:
    return bot.sendMessage(get_page(commands))
  if args.lower() == 'all':
    return bot.sendMessage(get_all(commands))
  
  _01j = [str(i) for i in range(1,11)]
  for char in list(args):
    if char not in _01j:
      isPage = False
  
  if isPage:
    return bot.sendMessage(get_page(commands, page=int(args)))
  else:
    return bot.sendMessage(get_command(commands, args))

config = {
  "name": 'help',
  "def": help,
  "credits": "Greegmon",
  "usage": "help [none|all|<page>|<cmdName>]",
  "description": "Get all command list/usage"
}