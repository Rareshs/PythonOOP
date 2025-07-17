from pydantic import BaseModel, Field


class PowRequest(BaseModel):
    a: int = Field(..., description="Base number")
    b: int = Field(..., description="Exponent")


class FibonacciRequest(BaseModel):
    n: int = Field(..., ge=0, description="Fibonacci index")


class FactorialRequest(BaseModel):
    n: int = Field(..., ge=0, description="Number for factorial")
