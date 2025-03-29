import smtplib
from email.mime.text import MIMEText

# Constants
GST_RATE = 0.18  # 18% GST
SMTP_SERVER = "smtp.example.com"
SENDER_EMAIL = "your_email@example.com"
SENDER_PASSWORD = "your_email_password"

# Product Class
class Product:
    def __init__(self, name, price, quantity):
        self.name = name
        self.price = price
        self.quantity = quantity

    def total_price(self):
        return self.price * self.quantity

# Bill Class
class Bill:
    def __init__(self):
        self.items = []

    def add_product(self, product):
        self.items.append(product)

    def calculate_total(self):
        subtotal = sum(item.total_price() for item in self.items)
        gst = subtotal * GST_RATE
        grand_total = subtotal + gst
        return subtotal, gst, grand_total

    def generate_bill_text(self, customer_email):
        bill_text = "\n===== Supermarket Bill =====\n"
        bill_text += "{:<20} {:<10} {:<10} {:<10}\n".format("Product", "Price", "Qty", "Total")
        bill_text += "-" * 50 + "\n"

        for item in self.items:
            bill_text += "{:<20} {:<10} {:<10} {:<10}\n".format(
                item.name, item.price, item.quantity, item.total_price()
            )

        subtotal, gst, grand_total = self.calculate_total()

        bill_text += "-" * 50 + "\n"
        bill_text += f"Subtotal: {subtotal:.2f} INR\n"
        bill_text += f"GST ({GST_RATE*100}%): {gst:.2f} INR\n"
        bill_text += f"Grand Total: {grand_total:.2f} INR\n"
        bill_text += f"Customer Email: {customer_email}\n"
        bill_text += "Thank you for shopping with us!\n"

        return bill_text

# Email Service Class
class EmailService:
    @staticmethod
    def send_email(to_email, bill_text):
        msg = MIMEText(bill_text)
        msg["Subject"] = "Supermarket Bill Receipt"
        msg["From"] = SENDER_EMAIL
        msg["To"] = to_email

        try:
            server = smtplib.SMTP(SMTP_SERVER, 587)
            server.starttls()
            server.login(SENDER_EMAIL, SENDER_PASSWORD)
            server.sendmail(SENDER_EMAIL, to_email, msg.as_string())
            server.quit()
            print(f"Bill sent successfully to {to_email}")
        except Exception as e:
            print(f"Error sending email: {str(e)}")

# Supermarket Billing Application
class SupermarketBillingApp:
    def __init__(self):
        self.bill = Bill()

    def main(self):
        print("Welcome to Supermarket Billing System")

        customer_email = input("Enter Customer Email: ")

        while True:
            name = input("Enter product name: ")
            price = float(input("Enter product price: "))
            quantity = int(input("Enter quantity: "))

            product = Product(name, price, quantity)
            self.bill.add_product(product)

            more = input("Do you want to add more items? (yes/no): ").strip().lower()
            if more != "yes":
                break

        bill_text = self.bill.generate_bill_text(customer_email)
        print(bill_text)

        EmailService.send_email(customer_email, bill_text)

# Run the Program
if __name__ == "__main__":
    app = SupermarketBillingApp()
    app.main()
