from flask import Blueprint, render_template, request, jsonify
from models import load_time_estimates, load_price_estimates, load_booking_details, load_receipt

booking_bp = Blueprint('booking_bp', __name__,
                       template_folder='templates')


@booking_bp.route('/estimates/<string:product_id>', methods=['POST'])
def booking(product_id):
    """
    Renders page for price and time of a product chosen
    """
    if request.method == 'POST':
        time_estimates = dict(load_time_estimates())
        price_estimates = dict(load_price_estimates())

        time_estimates = time_estimates.get('times', [])
        price_estimates = price_estimates.get('prices', [])

        time_product_searched = {}
        price_product_searched = {}
        for product in time_estimates:
            if product['product_id'] == product_id:
                time_product_searched = product
                break

        for product in price_estimates:
            if product['product_id'] == product_id:
                price_product_searched = product
                break
        return render_template("booking_estimates.html", product_time=time_product_searched,
                               product_price=price_product_searched)


@booking_bp.route('/details/<string:product_id>', methods=['POST'])
def booking_price_estimates(product_id):
    """
    Renders page for booking made
    """
    booking_details = dict(load_booking_details())
    if booking_details.get('product_id', '') == product_id:
        return render_template('current_ride_details.html',
                               booking_details=booking_details)
    else:
        return jsonify("For now you can only book uberx")


@booking_bp.route('/receipt/<string:request_id>')
def booking_receipt(request_id):
    """
    Renders page for the receipt of requested ride
    """
    receipt = dict(load_receipt())
    if receipt.get('request_id', '') == request_id:
        return render_template('receipt.html', receipt=receipt)
    else:
        return jsonify("Couldn't fetch recept for this ride")
