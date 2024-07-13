from flask import Flask, request, jsonify
from pydantic import BaseModel, ValidationError, validator
import logging


logging.basicConfig(level=logging.INFO)

app = Flask(__name__)

class Address(BaseModel):
    city: str
    district: str
    street: str

class Order(BaseModel):
    id: str
    name: str
    address: Address
    price: float
    currency: str

    @validator('currency')
    def validate_currency(cls, v):
        if v not in ['TWD', 'USD', 'JPY']:
            raise ValueError('Unsupported currency')
        return v.upper()

@app.route('/api/orders', methods=['POST'])
def process_order():
    try:
        order = Order(**request.json)
    except ValidationError as e:
        logging.error(f"Data validation error: {e}")
        return jsonify({"error": str(e)}), 400
    
    logging.info(f"Order processed: {order.dict()}")
    processed_data = {"status": "success", "data": order.dict()}
    return jsonify(processed_data), 200

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
