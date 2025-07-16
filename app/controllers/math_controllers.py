# app/controllers/math_controller.py

from flask import Blueprint, request, jsonify
from app.services.math_services import calculate_pow, calculate_fibonacci, calculate_factorial
from app.models.schemas import PowRequest, FibonacciRequest, FactorialRequest
from app.db.database import log_request

math_bp = Blueprint("math", __name__)


@math_bp.route("/pow", methods=["GET"])
def pow_route():
    data = PowRequest(a=int(request.args.get("a")), b=int(request.args.get("b")))
    result = calculate_pow(data.a, data.b)
    log_request("/pow", data.model_dump(), {"result": result})
    return jsonify({"result": result})


@math_bp.route("/fibonacci", methods=["GET"])
def fibonacci_route():
    data = FibonacciRequest(n=int(request.args.get("n")))
    result = calculate_fibonacci(data.n)
    log_request("/fibonacci", data.model_dump(), {"result": result})
    return jsonify({"result": result})


@math_bp.route("/factorial", methods=["GET"])
def factorial_route():
    data = FactorialRequest(n=int(request.args.get("n")))
    result = calculate_factorial(data.n)
    log_request("/factorial", data.model_dump(), {"result": result})
    return jsonify({"result": result})
