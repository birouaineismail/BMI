from fastapi import FastAPI, Query
from fastapi.responses import FileResponse
from pydantic import BaseModel

app = FastAPI()

class BMIOutput(BaseModel):
    bmi: float
    message: str

@app.get('/')
def server_home_page() :
    return FileResponse('index.html')


@app.get('/calculateBMI', response_model=BMIOutput)
def calculate_bmi(
    height: float = Query(..., gt=1, lt=2, description='Height in meters'),
    weight: float = Query(..., gt=25, lt=100, description='Weight in kilograms')
):
    calculated_bmi = weight / (height ** 2)

    if calculated_bmi < 18.5:
        message = 'You are underweight. You should eat more.'
    elif 18.5 <= calculated_bmi < 25:
        message = 'Your weight is normal.'
    elif 25 <= calculated_bmi < 30:
        message = 'You are overweight. You should exercise.'
    else:
        message = 'You are obese. You must consider a diet.'

    return BMIOutput(bmi=round(calculated_bmi, 2), message=message)