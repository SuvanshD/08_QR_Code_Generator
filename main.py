import pyqrcode
from pyqrcode import QRCode

link = "https://www.instagram.com/gianapvt/"

url = pyqrcode.create(link)

url.svg("Github.svg", scale=8)