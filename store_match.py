from flask import Flask, request, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

coupons = [
    {"store": "Target", "brand": "Huggies", "discount": "$2.00", "expires": "2025-06-30", "zip": "06450"},
    {"store": "Walmart", "brand": "Colgate", "discount": "$1.50", "expires": "2025-07-01", "zip": "06451"},
    {"store": "CVS", "brand": "Tide", "discount": "$3.00", "expires": "2025-06-28", "zip": "06457"},
    {"store": "Walgreens", "brand": "Dove", "discount": "$1.25", "expires": "2025-07-15", "zip": "06450"}
]

@app.route("/match", methods=["GET"])
def match_store():
    zip_code = request.args.get("zip")
    if not zip_code:
        return jsonify({"error": "ZIP code required"}), 400
    matches = [c for c in coupons if c["zip"] == zip_code]
    return jsonify(matches)