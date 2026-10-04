import qrcode

data="hello i am satwik"

img=qrcode.make(data)

img.save("C:/Users/WELCOME/Pictures/Saved Pictures/qr.png")