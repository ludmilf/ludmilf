# Генериране на QR-код
from PIL import Image
import pyqrcode
import png
link = input('Въведете линк за съдържание на QR-кода: ')
qr_code = pyqrcode.create(link)
qr_code.png('QRCode.png', scale=5)
Image.open('QRCode.png')
