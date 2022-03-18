import pyqrcode
import qrcode
from barcode import EAN13

# url = pyqrcode.create('http://uca.edu')
# # big_code = pyqrcode.create('0987654321', error='L', version=27, mode='binary')
# # big_code.png('code.png', scale=6, module_color=[0, 0, 0, 128], background=[0xff, 0xff, 0xcc])
# url.svg('uca-url.svg', scale=6)
# print(url.terminal(quiet_zone=1))

#######################################################################################

# qr = qrcode.QRCode(
#     version=1,
#     box_size=15,
#     border=10
# )
#
# # adding a link for the QR code to open
# data = 'https://www.google.co.in/'
# qr.add_data(data)
# qr.make(fit=True)
#
# # adding the color
# img = qr.make_image(fill='black', back_color='white')
# img.save('qrcode.png')

#######################################################################################
########################### Bar-Code ######################################

number = '8801689040992'
my_code = EAN13(number)
my_code.save("bar_code")
