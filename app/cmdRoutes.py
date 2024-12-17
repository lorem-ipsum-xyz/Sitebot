from flask import (
  Blueprint,
  render_template
)
from bs4 import BeautifulSoup
import requests

cmd = Blueprint('cmd',__name__)

@cmd.route('/paster/<path>')
def paster(path):
  res = requests.get(f"https://pastebin.mozilla.org/{path}/raw")
  return render_template('other/paster.html', text=res.text),200