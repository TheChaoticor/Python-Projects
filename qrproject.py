import qrcode as qr
from PIL import Image

img = qr.make("https://www.linkedin.com/in/arpit-mishra-87b943242/")
img.save("Arpit_Mishra_Linkedin.png")





q=qr.QRCode(version=1,error_correction=qr.constants.ERROR_CORRECT_H,box_size=10,border=4)
q.add_data("https://chat.openai.com/c/614e62b5-91d8-428a-81b7-41b8613eef4e")
q.make(fit=True)
img1=q.make_image(fill_color="red",back_color="blue")
img1.save("wow image.png")