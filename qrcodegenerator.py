import qrcode

def qr_generator(text):
    
    qr = qrcode.QRCode(
        version = 1,
        error_correction = qrcode.constants.ERROT_CORRECT_L,
        box_size=10,
        border=4,
    )

    qr.add_data(text)
    qr.make(fit=True)
    img = qr.make_image(fill_color="black", back_color="white")
    img.save("qrimg.png")

generate_qrcode("https://www.wifiqrcode.com")