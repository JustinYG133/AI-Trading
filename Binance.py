import os
from dotenv import load_dotenv
from binance.client import Client
import binance.exceptions

load_dotenv()

api_key = os.environ.get('binance_api')
api_secret = os.environ.get('binance_secret')

if not api_key or not api_secret:
    raise ValueError("API key or secret not found in .env file!")

client = Client(api_key, api_secret)
client.API_URL = 'https://demo-fapi.binance.com'

try:
    balance = client.futures_account_balance()
    print(balance)
except binance.exceptions.BinanceAPIException as e:
    print(f"Error: {e}")