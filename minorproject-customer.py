from flask import Flask, render_template, request
import stripe

app = Flask(__name__)

# Set your Stripe secret key
stripe.api_key = "your_stripe_secret_key"

@app.route('/')
def index():
    return render_template('payment_form.html')

@app.route('/charge', methods=['POST'])
def charge():
    amount = 5000  # Amount in cents
    customer = stripe.Customer.create(
        email='customer@example.com',
        source=request.form['stripeToken']
    )
    stripe.Charge.create(
        customer=customer.id,
        amount=amount,
        currency='usd',
        description='Service payment'
    )
    return render_template('payment_success.html')

@app.route('/payment')
def payment():
    # This renders the payment form where users enter card details
    return render_template('payment_form.html')

if __name__ == '__main__':
    app.run(port=5098)
