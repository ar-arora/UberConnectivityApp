# implementing models from json files as we don't have a server access token for Uber SDK right now.

import json
import os


def load_products():
    """
    Returns the product available at a particular location from mock data
    """
    try:
        with open('./mock_data_jsons/products.json') as model:
            return json.load(model)
    except Exception as ex:
        print("Some Exception while loading products : ", ex)
        return str({'Some Exception while loading products': ex})


def load_product_details():
    """
    Returns the product details from mock data
    """
    try:
        with open('./mock_data_jsons/product-details.json') as model:
            return json.load(model)
    except Exception as ex:
        print("Some Exception while loading product details : ", ex)
        return str({'Some Exception while loading product details': ex})


def load_time_estimates():
    """
    Returns the time estimates from mock data
    """
    try:
        with open('./mock_data_jsons/time-estimates.json') as model:
            return json.load(model)
    except Exception as ex:
        print("Some Exception while loading time estimates : ", ex)
        return str({'Some Exception while loading time estimates': ex})


def load_price_estimates():
    """
    Returns the price estimates from mock data
    """
    try:
        with open('./mock_data_jsons/price-estimates.json') as model:
            return json.load(model)
    except Exception as ex:
        print("Some Exception while loading price estimates : ", ex)
        return str({'Some Exception while loading price estimates': ex})


def load_booking_details():
    """
    Returns the booking details from mock data
    """
    try:
        with open('./mock_data_jsons/booking-details.json') as model:
            return json.load(model)
    except Exception as ex:
        print("Some Exception while loading booking details : ", ex)
        return str({'Some Exception while loading booking details': ex})


def load_receipt():
    """
    Returns the receipt from mock data
    """
    try:
        with open('./mock_data_jsons/receipt.json') as model:
            return json.load(model)
    except Exception as ex:
        print("Some Exception while loading Receipt : ", ex)
        return str({'Some Exception while loading Receipt': ex})
