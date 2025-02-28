import stripe
from flask import Flask, request, jsonify
from dotenv import load_dotenv
import os
import requests
import json


load_dotenv()  # Load environment variables from .env file
stripe_keys = {
            "secret_key": os.getenv("API_secret_KEY"),
            "publishable_key": os.getenv("API_publisher_KEY"),
        }

def create_stripe_product(name, description, images, metadata=None, active=True):
    try:     
        stripe.api_key = stripe_keys["secret_key"]
        if not stripe.api_key:
            raise ValueError("STRIPE_SECRET_KEY environment variable not set.")

        product = stripe.Product.create(
            name=name,
            description=description,
            images=images,
            metadata=metadata,
            active=active,
        )
        return product
    except stripe.error.StripeError as e:
        print(f"Error creating Stripe product: {e}")
        return None
    except ValueError as ve:
        print(f"Value Error: {ve}")
        return None
    except Exception as e:
        print(f"An unexpected error occured: {e}")
        return None

def create_stripe_price(product_id, unit_amount, currency, recurring=None, metadata=None):
    try:
        stripe.api_key = stripe_keys["secret_key"]

        if recurring:
            price = stripe.Price.create(
                product=product_id,
                unit_amount=unit_amount,
                currency=currency,
                recurring=recurring,
                metadata=metadata,
            )
        else:
            price = stripe.Price.create(
                product=product_id,
                unit_amount=unit_amount,
                currency=currency,
                metadata=metadata,
            )
        return price
    except stripe.error.StripeError as e:
        print(f"Error creating Stripe price: {e}")
        return None
    except ValueError as ve:
        print(f"Value Error: {ve}")
        return None
    except Exception as e:
        print(f"An unexpected error occured: {e}")
        return None

def create_multiple_products(product_list):
    for product_data in product_list:
        try:
            product_name = product_data["name"]
            product_description = product_data["description"]
            product_images = product_data.get("images")
            product_metadata = product_data.get("metadata", None)
            product_active = product_data.get("active", True)
            price_data = product_data["price"] #This is now mandatory for each product.

            created_product = create_stripe_product(
                product_name, product_description, product_images, product_metadata, product_active
            )

            if created_product:
                print(f"Product created: {created_product.id}")

                price_amount = price_data["unit_amount"]
                price_currency = price_data["currency"]
                price_recurring = price_data.get("recurring", None)
                price_metadata = price_data.get("metadata", None)

                created_price = create_stripe_price(
                    created_product.id, price_amount, price_currency, price_recurring, price_metadata
                )

                if created_price:
                    print(f"Price created: {created_price.id}")
                else:
                    print(f"Failed to create price for product: {product_name}")
            else:
                print(f"Failed to create product: {product_name}")
        except KeyError as ke:
            print(f"Key Error: Missing required key in product data: {ke}")
        except Exception as e:
            print(f"An unexpected error occurred during product creation: {e}")

#input product details
if __name__ == "__main__":
    products = [
        {
            "name": "Product 1",
            "description": "Description of Product 1",
            "price": {"unit_amount": 1000, "currency": "gbp"}, #Required
        },
        {
            "name": "Product 2",
            "description": "Description of Product 2",
            "metadata": {"category": "electronics"},
            "price": {"unit_amount": 2000, "currency": "gbp", "recurring": {"interval": "month"}}, #Required
        },
        {
            "name": "Product 3",
            "description": "Product 3 Description",
            "price": {"unit_amount": 500, "currency": "gbp"}, #Required
        },
    ]

    create_multiple_products(products)