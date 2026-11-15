
import qrcode

# Memasukkan link atau teks
data = input("Masukkan link atau teks: ")

# Membuat QR Code
qr = qrcode.QRCode(
    version=1,
    error_correction=qrcode.constants.ERROR_CORRECT_H,
    box_size=10,
    border=4
)

qr.add_data(data)
qr.make(fit=True)

# Membuat gambar QR Code
img = qr.make_image(
    fill_color="black",
    back_color="white"
)

# Menyimpan gambar QR Code
img.save("qrcode_hasil.png")

# Menampilkan gambar QR Code
img.show()

print("================================")
print("QR CODE BERHASIL DIBUAT!")
print("File: qrcode_hasil.png")
print("================================")

