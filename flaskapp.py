from flask import Flask, render_template, request
from main import initialize_agent
from yelp_api import yelp_search
from doordash_api import doordash_create_delivery

app = Flask(__name__)

assistant, user_proxy = initialize_agent()

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/search', methods=['POST'])
def search():
    location = request.form.get('location')
    category = request.form.get('category')
    term = request.form.get('term')
    results = yelp_search(location, category, term)
    return render_template('results.html', results=results)

@app.route('/create_delivery', methods=['POST'])
def create_delivery():
    delivery_details = {
        "external_delivery_id": request.form.get('external_delivery_id'),
        "pickup_address": request.form.get('pickup_address'),
        "pickup_business_name": request.form.get('pickup_business_name'),
        "pickup_phone_number": request.form.get('pickup_phone_number'),
        "dropoff_address": request.form.get('dropoff_address'),
        "dropoff_business_name": request.form.get('dropoff_business_name'),
        "dropoff_phone_number": request.form.get('dropoff_phone_number'),
        "order_value": int(request.form.get('order_value')),
        "currency": request.form.get('currency'),
        "contactless_dropoff": request.form.get('contactless_dropoff') == 'true',
        "tip": int(request.form.get('tip')),
    }
    response = doordash_create_delivery(delivery_details)
    return render_template('delivery_confirmation.html', response=response)

if __name__ == '__main__':
    app.run(debug=True)