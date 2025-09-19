from fastapi import FastAPI, Depends, HTTPException
from pydantic import BaseModel

app = FastAPI()

class Calc(BaseModel):
    num1: int
    num2: int

def get_num(calc: Calc):
    if calc.num1 is None or calc.num2 is None:
        raise HTTPException(status_code=400, detail="Both num1 and num2 required")
    return calc

@app.get("/home")
def operation():
    return {"message": "Welcome to calculator app"}

@app.post("/add")
def addition(calc: Calc = Depends(get_num)):
    add=calc.num1+calc.num2
    return {"result": add}

@app.post("/substract")
def substraction(calc:Calc = Depends(get_num)):
    sub=calc.num1-calc.num2
    return {"result": sub}
    
@app.post("/multiply")
def multiplication(calc:Calc = Depends(get_num)):
    multi=calc.num1*calc.num2
    return {"result": multi}

@app.post("/divide")
def division(calc:Calc = Depends(get_num)):
    if calc.num2==0:
        return {"error": "Division by zero is not allowed"}
    div=calc.num1/calc.num2
    return {"result": div}
