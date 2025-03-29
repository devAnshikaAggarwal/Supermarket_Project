# Supermarket Billing System

## Overview
The Supermarket Billing System is a Python-based application that calculates the total bill for purchased products, including GST (Goods and Services Tax). It also generates a bill receipt and sends it via email to the customer.

## Features
- Add multiple products with name, price, and quantity.
- Automatically calculate subtotal, GST, and grand total.
- Generate a formatted bill receipt.
- Send the bill receipt via email.

## Technologies Used
- Python 3
- Object-Oriented Programming (OOP)
- SMTP (Simple Mail Transfer Protocol) for email

## Requirements
- Python 3.x installed
- Internet connection (for email service)
- SMTP email service credentials

## Installation
1. Clone the repository or copy the script.
2. Install required dependencies:
   ```sh
   pip install smtplib
   ```
3. Update the SMTP server, sender email, and password in the script:
   ```python
   SMTP_SERVER = "smtp.example.com"
   SENDER_EMAIL = "your_email@example.com"
   SENDER_PASSWORD = "your_email_password"
   ```

## Usage
1. Run the script:
   ```sh
   python supermarket_billing.py
   ```
2. Enter customer email.
3. Input product details (name, price, quantity) until finished.
4. The bill is displayed and sent via email to the customer.

## Bill Format
```
===== Supermarket Bill =====
Product              Price      Qty       Total      
--------------------------------------------------
Milk                 50.0       2        100.0      
Bread                40.0       1         40.0      
--------------------------------------------------
Subtotal: 140.00 INR
GST (18%): 25.20 INR
Grand Total: 165.20 INR
Customer Email: customer@example.com
Thank you for shopping with us!
```

## Future Enhancements
- Add product categories.
- Implement a GUI version.
- Store customer purchase history.
