from flask import Flask, jsonify

app = Flask(__name__)

# Existing CORS setup (assumed from context)
@app.after_request
def after_request(response):
    response.headers.add('Access-Control-Allow-Origin', '*')
    return response

# Error handler for 401 Unauthorized
@app.errorhandler(401)
def unauthorized(error):
    return jsonify({"error": "Unauthorized"}), 401
