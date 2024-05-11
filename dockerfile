FROM python:3.9.6-slim-buster

WORKDIR D:/Scaler-DSML/13-MLOPS/04-Aws-Deployment/loan-app-project

COPY requirements.txt ./
RUN python -m pip install --upgrade pip
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

CMD ["python3", "-m", "flask", "--app", "loan_app.py", "run", "--host=0.0.0.0"]