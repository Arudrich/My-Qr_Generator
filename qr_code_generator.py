import qrcode

qr = qrcode.QRCode(
        version = 1 ,
        error_correction =qrcode.constants.ERROR_CORRECT_L,
        box_size = 6 ,
        border = 3 
)

img = qr.add_data("https://github.com/Arudrich")
img = qr.make_image()
with open('QRCODE/MyGithub.png', 'wb') as f: #('QRCODE/qrcode.png', 'wb')  is the path where the qrcode PNG will save.
        img.save(f)