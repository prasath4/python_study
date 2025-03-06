from flask import Flask
import os
import pymongo
import urllib.parse

# Encode the username and password properly
username = urllib.parse.quote_plus("Admin")
password = urllib.parse.quote_plus("Admin@01")  # If your password contains @, :, or other special characters, they must be encoded.

# Correct MongoDB connection string
MONGODB_URL = f'mongodb+srv://{username}:{password}@pythontomangodb.dwjv2.mongodb.net/?retryWrites=true&w=majority'

try:
    client = pymongo.MongoClient(MONGODB_URL)
    print("Connected successfully:", client.server_info())  # Test connection
except Exception as e:
    print("MongoDB Connection Error:", e)

# Flask App Setup
app = Flask(__name__)

if __name__ == '__main__':
    port = int(os.environ.get("PORT", 5000))
    app.run(debug=True, host='0.0.0.0', port=port)
