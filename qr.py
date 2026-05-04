import qrcode

url = input("Enter the URL to generate QR code: ").strip()
file_path = "C:\\Users\\Omkar\\Desktop\\qrcode.png"

qr = qrcode.make(url)
qr.save(file_path)

print("QR code generated successfully at", file_path)
