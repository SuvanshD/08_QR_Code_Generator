import pyqrcode
from pyqrcode import QRCode

link = "https://github.com/SuvanshD"

url = pyqrcode.create(link)

url.svg("Github.jpg", scale=8)