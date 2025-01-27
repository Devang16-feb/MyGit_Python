import qrcode

# UPI Details
upi_id = "devang10pro@okaxis"
payee_name = "Devang"
note = "Pay to Devang Bhalerao"

# UPI URL format
upi_url = f"upi://pay?pa={upi_id}&pn={payee_name}&cu=INR&tn={note}"

# Print the UPI URL (for reference)
print("UPI URL:", upi_url)

# Generate the QR code
qr = qrcode.QRCode(version=1, box_size=10, border=5)
qr.add_data(upi_url)
qr.make(fit=True)

# Create an image of the QR code
img = qr.make_image(fill="black", back_color="white")

# Save the QR code as a file
img.save("bank_payment_qr.png")

print("QR Code has been generated and saved as 'bank_payment_qr.png'.")
