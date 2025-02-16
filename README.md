# stripePayment


## About

Creating Webhook for payment link in Stripe (goal, in progress). 

## In this Repo

- checkAPIKeys.py - to check if API Keys are correctly assigned & can be accessed properly
- stripeCheck.py - to check if Stripe connection is successfully established

## How to use

1. Input your secret & public API Keys in .env ("API_secret_KEY" & "API_publisher_KEY" respectively)
2. Run checkAPIKeys.py to check if your API keys can be appropriately accessed
3. Run stripeCheck.py & enter https://127.0.0.1:5000/check_stripe (local machine) on browser to check if connection to Stripe is successful (you'll get the message "Stripe connection successful" when it's properly established)
