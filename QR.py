import qrcode as qrqrcode
qr = qrqrcode.QRCode(
    version=1, 
    error_correction=qrqrcode.constants.ERROR_CORRECT_L,
    box_size=40, 
    border=4,    
)
try:
    qr.add_data("bonne  anne'e howa matkolich bonne annee'e")
    qr.make(fit=True)
    img = qr.make_image(fill_color="black", back_color="white")
    img = img.resize((3840, 3840)) 
    img.save("M.png")
    print("QR code saved.")
except Exception as e:
    print(f"An error occurred: {e}")