#!/usr/bin/env python 
# jorune00 -- 2023-09-19 10:56:21

import qrcode
from PIL import Image

value = "twitter/jorune00"

qr_code = qrcode.QRCode(version=1, box_size=10, border=5)
qr_code.add_data(value)
qr_code.make(fit=True)

qr_image = qr_code.make_image(fill="black", back_color="white")

qr_image.save("qr_code.png")