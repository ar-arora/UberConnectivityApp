from flask import Flask, render_template
from products import products_bp
from booking import booking_bp

app = Flask(__name__)


@app.route('/')
def welcome():
    """
    Homepage
    """
    return render_template("index.html")


# Registering the apis spcified as part of other files
app.register_blueprint(products_bp, url_prefix='/products')
app.register_blueprint(booking_bp, url_prefix='/booking')


if __name__ == "__main__":
    app.run(port=5000)
