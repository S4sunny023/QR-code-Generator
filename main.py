import qrcode as qr
from PIL import Image

img = qr.make("https://www.linkedin.com/in/sunnygupta023")
img.save('linkedin-sunny.png')