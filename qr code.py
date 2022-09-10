import qrcode
text=input('enter your text: ')
address=input('write your text address: ')
qr=qrcode.make(text,address)
qr.save('qrcode.jpg')