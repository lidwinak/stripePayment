import os
import stripe
from flask import Flask, jsonify
from dotenv import load_dotenv

load_dotenv()  # Load environment variables from .env file

app = Flask(__name__)

# Securely load Stripe API keys from environment variables
stripe_keys = {
    "secret_key": os.getenv("API_secret_KEY"),
    "publishable_key": os.getenv("API_publisher_KEY"),
}
stripe.api_key = stripe_keys["secret_key"]

@app.route("/check_stripe")
def check_stripe_connection():
    try:
        # Attempt a simple Stripe API call to verify the connection
        # For example, retrieve a list of customers (even if it's empty)
        stripe.Customer.list(limit=1)  # Limit to 1 to avoid retrieving a huge list

        return jsonify({"status": "success", "message": "Stripe connection successful!"})

    except stripe.error.StripeError as e:
        # Handle Stripe errors (e.g., invalid API key, network issues)
        return jsonify({"status": "error", "message": str(e)})

    except Exception as e:  # Catch any other unexpected errors
        return jsonify({"status": "error", "message": "An unexpected error occurred: " + str(e)})


if __name__ == "__main__":
    app.run(debug=True)  # debug=True for development
