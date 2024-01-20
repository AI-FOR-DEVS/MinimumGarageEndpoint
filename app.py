from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/run')
def spare_parts():
    # Hardcoded array of spare parts
    spare_parts = [
        {"name": "Oil Filter", "availability": "In stock", "price": "$15.99"},
        {"name": "Brake Pads", "availability": "Limited stock", "price": "$35.50"},
        {"name": "Air Filter", "availability": "In stock", "price": "$12.00"},
        {"name": "Spark Plugs", "availability": "Out of stock", "price": "$5.99 each"},
        {"name": "Timing Belt", "availability": "In stock", "price": "$22.99"},
        {"name": "Fuel Pump", "availability": "Limited stock", "price": "$89.99"},
        {"name": "Battery", "availability": "In stock", "price": "$79.99"},
        {"name": "Alternator", "availability": "Out of stock", "price": "$149.99"},
        {"name": "Radiator", "availability": "In stock", "price": "$99.99"},
        {"name": "Shock Absorbers", "availability": "Limited stock", "price": "$68.99 each"}
    ]

    # Returning the spare parts as JSON
    return jsonify({"spare_parts": spare_parts})

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=80)