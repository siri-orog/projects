import pyshorteners
import qrcode

# Function to Shorten URL
def shorten_url(long_url):
    s = pyshorteners.Shortener()
    return s.tinyurl.short(long_url)

# Function to Generate QR Code
def generate_qr(short_url):
    qr = qrcode.QRCode(version=1, box_size=10, border=5)
    qr.add_data(short_url)
    qr.make(fit=True)

    img = qr.make_image(fill="black", back_color="white")
    img.save("short_url_qr.png")
    print("QR Code saved as 'short_url_qr.png'")

# User Input
long_url = input("Enter the URL to shorten: ").strip()

# Generate and Display Shortened URL & QR Code
short_url = shorten_url(long_url)
print(f"Shortened URL: {short_url}")
generate_qr(short_url)
