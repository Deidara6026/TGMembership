
**TGMembership Readme**

This is  a Telegram bot application that manages subscriptions for premium groups or channels. The bot is built using the pytelegrambotapi library and integrates with a Flask server for webhook handling. It also uses the SQLAlchemy ORM for database interactions and the Coinbase Commerce API for handling payments.
Key Features

1. *Subscription Management*: The bot manages subscriptions for premium groups or channels. It can add or remove users from groups based on their subscription status.

2. *Payment Handling*: The bot integrates with the Coinbase Commerce API to handle payments. Users can deposit funds into their wallet, which are then used to pay for subscriptions.

3. *Webhook Handling*: The bot uses Flask to handle incoming webhooks from both Telegram and Coinbase Commerce.

4. *Database Interactions*: The bot uses SQLAlchemy to interact with the database. It stores information about users, groups, and subscriptions in the database.
Key Functions

This script requires the following Python libraries:

- pytelegrambotapi
- flask
- sqlalchemy
- coinbase_commerce
- datetime
- collections
- logging