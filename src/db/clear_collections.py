import os
from pymongo import MongoClient
from dotenv import load_dotenv

# Load .env variables
load_dotenv()

MONGODB_URI = os.getenv("MONGODB_URI")
MONGODB_DB_NAME = os.getenv("MONGODB_DB_NAME")

COLLECTIONS = [
    "product_offering",
    "product_specification",
    "product_characteristic",
    "product_price",
]

client = MongoClient(MONGODB_URI)
db = client[MONGODB_DB_NAME]

for col in COLLECTIONS:
    result = db[col].delete_many({})
    print(f"Cleared {result.deleted_count} documents from collection: {col}")

print("Selected collections have been cleared.")