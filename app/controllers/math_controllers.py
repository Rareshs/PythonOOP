from flask import Blueprint, request, jsonify
from werkzeug.exceptions import HTTPException
from pydantic import ValidationError
from app.services.math_services import calculate_pow, calculate_fibonacci, calculate_factorial
from app.models.schemas import PowRequest, FibonacciRequest, FactorialRequest
from app.db.database import log_request
from app.utils.auth_decorator import login_required


math_bp = Blueprint("math", __name__)


@math_bp.route("/pow", methods=["GET"])
@login_required
async def pow_route():
    params = request.args.to_dict()
    data = PowRequest.model_validate(params)
    result = calculate_pow(data.a, data.b)
    await log_request("/pow", data.model_dump(), {"result": result}, 200)
    return jsonify({"result": result})


@math_bp.route("/fibonacci", methods=["GET"])
@login_required
async def fibonacci_route():
    params = request.args.to_dict()
    data = FibonacciRequest.model_validate(params)
    result = calculate_fibonacci(data.n)
    await log_request("/fibonacci", data.model_dump(), {"result": result}, 200)
    return jsonify({"result": result})


@math_bp.route("/factorial", methods=["GET"])
@login_required
async def factorial_route():
    params = request.args.to_dict()
    data = FactorialRequest.model_validate(params)
    result = calculate_factorial(data.n)
    await log_request("/factorial", data.model_dump(), {"result": result}, 200)
    return jsonify({"result": result})


@math_bp.errorhandler(Exception)
async def handle_error(error):
    if isinstance(error, ValidationError):
        status_code = 400
        errors_list = error.errors()
        message = {
            "errors": [
                {
                    "field": ".".join(err["loc"]),
                    "msg": err["msg"]
                }
                for err in errors_list
            ]
        }
    elif isinstance(error, HTTPException):
        status_code, message = error.code, error.description
    elif isinstance(error, (ValueError, TypeError)):
        status_code, message = 400, {"error": str(error)}
    else:
        status_code, message = 500, {"error": str(error)}

    endpoint = request.path
    request_data = request.args.to_dict()
    await log_request(endpoint, request_data, message, status_code)
    return jsonify(message), status_code
