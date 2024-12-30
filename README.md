# UPI QR Code Generator

This web application allows users to generate UPI QR codes easily. Users can input their UPI ID and the transaction amount, and the application generates a QR code that can be used for payments. The application supports popular UPI IDs and provides a user-friendly interface to make payment requests.

## Features

- **UPI ID Input:** Users can enter their UPI ID to generate a QR code.
- **Amount Input:** Users can specify the transaction amount for the payment.
- **Dynamic Background:** The background changes according to the UPI ID entered (e.g., Google Pay, Paytm, PhonePe).
- **QR Code Generation:** Generates a UPI QR code based on the entered details.
- **Clear and Simple Interface:** The layout is clean, easy to use, and responsive.
- **Live Updates:** Background and details update in real-time as the user enters their UPI ID and amount.

## How to Use

1. Open the web application.
2. Enter your UPI ID (e.g., `tokyo@okbizaxis`) or select from the pre-defined ones.
3. Enter the payment amount.
4. The application will generate a UPI QR code that you can scan for payments.

## Technologies Used

- **Flask:** A Python web framework used to build the application.
- **Flask-Qrcode:** An extension to generate QR codes within Flask.
- **HTML/CSS/JS:** For the front-end layout and interactivity.
- **Bootstrap:** For responsive design and layout.
- **Python:** For server-side logic and QR code generation.

## Installation

To run the application locally, follow these steps:

1. Clone the repository:
   ```bash
   git clone https://github.com/div-bhati/upi-qr.git
