from flask import Blueprint, request, jsonify
from werkzeug.exceptions import HTTPException
from app.services.math_services import calculate_pow, calculate_fibonacci, calculate_factorial
from app.models.schemas import PowRequest, FibonacciRequest, FactorialRequest
from app.db.database import log_request

math_bp = Blueprint("math", __name__)


@math_bp.route("/pow", methods=["GET"])
async def pow_route():
    data = PowRequest(a=int(request.args.get("a")), b=int(request.args.get("b")))
    result = calculate_pow(data.a, data.b)
    await log_request("/pow", data.model_dump(), {"result": result}, 200)
    return jsonify({"result": result})


@math_bp.route("/fibonacci", methods=["GET"])
async def fibonacci_route():
    data = FibonacciRequest(n=int(request.args.get("n")))
    result = calculate_fibonacci(data.n)
    await log_request("/fibonacci", data.model_dump(), {"result": result}, 200)
    return jsonify({"result": result})


@math_bp.route("/factorial", methods=["GET"])
async def factorial_route():
    data = FactorialRequest(n=int(request.args.get("n")))
    result = calculate_factorial(data.n)
    await log_request("/factorial", data.model_dump(), {"result": result}, 200)
    return jsonify({"result": result})


@math_bp.errorhandler(Exception)
async def handle_error(error):
    if isinstance(error, HTTPException):
        status_code = error.code
        message = error.description
    else:
        status_code = 500
        message = str(error)

    # Încearcă să extragi datele requestului, dacă există
    try:
        endpoint = request.path
        request_data = request.args.to_dict()
    except Exception:
        endpoint = "unknown"
        request_data = {}

    await log_request(endpoint, request_data, {"error": message}, status_code)
    return jsonify({"error": message}), status_code
