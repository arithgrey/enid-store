FROM python:3.8-alpine

WORKDIR /enid

COPY requirements.txt /enid/
RUN pip install --no-cache-dir -r requirements.txt

COPY . /enid/

CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
