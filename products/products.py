from flask import Blueprint, render_template, jsonify, request
from models import load_products, load_product_details

products_bp = Blueprint('products_bp', __name__,
                        template_folder='templates')


@products_bp.route('/')
def products():
    """
    Renders page for searching products at a location
    """
    return render_template("products.html")


@products_bp.route('/available/', methods=['GET', 'POST'])
def products_available():
    """
    The POST method renders page for products available at a location
    The GET method returns a JSON for products available at a location
    """
    if request.method == 'POST':
        products = dict(load_products())
        return render_template("products_available.html", products=products.get("products", []))

    else:
        try:
            products = load_products()
            return products
        except Exception as ex:
            print("Some exception while fetching products", ex)
            return jsonify({'Some Exception while fetching products': ex})


@products_bp.route('/details/<string:product_id>', methods=['GET'])
def products_pricing(product_id):
    """
    GET method to return details for products available in a JSON format
    """
    try:
        product_details = dict(load_product_details())
        if product_details.get('product_id', '') == product_id:
            return product_details
        else:
            return jsonify("For now we only have details for uberx")
    except Exception as ex:
        print("Some exception while fetching product details", ex)
        return jsonify({'Some Exception while fetching product details': ex})
