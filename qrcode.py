#Downloads and Import the require modules which we are using for this project.
import pyqrcode
from pyqrcode import QRCode
from pyzbar.pyzbar import decode
from PIL import Image

#Here in target put the link where you want your users to land after scanning your QR Code.
target = "https://focused-lamport-ae0eba.netlify.com/"

url = pyqrcode.create(target)

#Here you can use the image formats like(svg, png, jpeg) according to your convenience.
url.svg("myqrc.svg", scale=8)

