FROM python:3.9-slim

WORKDIR /the/workdir/path

COPY requirements.txt .

RUN pip install -r requirements.txt

COPY . .

CMD ["flask", "run", "--host=0.0.0.0"]