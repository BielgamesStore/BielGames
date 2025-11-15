import qrcode

url = "https://bielgamesstore.github.io/BielGames/"

qr = qrcode.make(url)
qr.save("qr_site.png")

print("QR gerado: qr_site.png")
