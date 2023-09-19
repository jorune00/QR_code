#!/usr/bin/env python 
# jorune00 -- 2023-09-19 10:56:21

import qrcode
from PIL import Image

value = input("Enter the value: ") # enter the value to be converted to QR code

qr_code = qrcode.QRCode(version=1, box_size=10, border=5)
qr_code.add_data(value)
qr_code.make(fit=True)

qr_code = qr_code.make_image(fill="black", back_color="white")

filename = input("Enter the filename: ") # enter the filename to save the QR code

qr_code.save(f"{filename}.png") # save the image
