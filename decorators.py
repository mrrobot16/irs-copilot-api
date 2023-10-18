from flask import jsonify
from functools import wraps
from config import APP_ENABLED

def app_enabled_required(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
          # Adjust this value to enable or disable endpoints
        if APP_ENABLED:
            return func(*args, **kwargs)
        else:
            return jsonify({"error": "This endpoint is not available."}), 503

    return wrapper