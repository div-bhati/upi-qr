from flask import Flask, render_template, request, redirect
import qrcode
import os
import uuid
import threading

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = 'static/qr_codes'

# Ensure the QR folder exists
if not os.path.exists(app.config['UPLOAD_FOLDER']):
    os.makedirs(app.config['UPLOAD_FOLDER'])

# Function to automatically delete QR code files
def delete_qr_after_delay(file_path, delay=60):
    def delete_file():
        if os.path.exists(file_path):
            os.remove(file_path)
    threading.Timer(delay, delete_file).start()

# Mapping UPI domains to their respective images
upi_images = {
    "okaxis": "static/images/google_pay.png",
    "oksbi": "static/images/google_pay.png",
    "okhdfc": "static/images/google_pay.png",
    "okicici": "static/images/google_pay.png",
    "okbizaxis": "static/images/google_pay.png",
    "axl": "static/images/phonepe.png",
    "ibl": "static/images/phonepe.png",
    "ybl": "static/images/phonepe.png",
    "ptyes": "static/images/paytm.png",
    "ptaxis": "static/images/paytm.png",
}

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        # Get UPI ID and amount from the form
        upi_id = request.form.get('upi_id')
        amount = request.form.get('amount')

        if upi_id and amount:
            # Extract the UPI domain (e.g., "okaxis" from "tokyo@okaxis")
            upi_domain = upi_id.split('@')[-1]

            # Determine the corresponding image (default to None if no match)
            app_icon = upi_images.get(upi_domain)

            # Generate a unique transaction reference ID
            transaction_id = f"divBh{uuid.uuid4().hex[:10]}"
            # Create UPI link
            upi_link = f"upi://pay?pa={upi_id}&am={amount}&cu=INR&tr={transaction_id}"

            # Generate QR code
            qr = qrcode.QRCode(version=1, box_size=10, border=5)
            qr.add_data(upi_link)
            qr.make(fit=True)

            qr_image_path = os.path.join(app.config['UPLOAD_FOLDER'], f"{transaction_id}.png")
            qr.make_image(fill='black', back_color='white').save(qr_image_path)

            # Schedule QR code deletion after 1 minute
            delete_qr_after_delay(qr_image_path, delay=60)

            return render_template('index.html', qr_path=qr_image_path, upi_link=upi_link, app_icon=app_icon)

    return render_template('index.html')


@app.route('/redirect', methods=['GET'])
def redirect_to_upi():
    upi_link = request.args.get('upi_link')
    if upi_link:
        return redirect(upi_link)
    return "Invalid UPI link", 400


if __name__ == '__main__':
    app.run(debug=True)
