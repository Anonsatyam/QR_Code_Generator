import pyqrcode
from pyqrcode import QRCode
from pyzbar.pyzbar import decode
from PIL import Image

target = "https://focused-lamport-ae0eba.netlify.com/"

url = pyqrcode.create(target)

url.svg("myqrc.jpeg", scale=8)
