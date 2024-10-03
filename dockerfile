FROM python:3.10.6

COPY /python .

RUN pip install --no-cache-dir -r requirements.txt 

RUN chmod a+x src/*.sh
# CMD gunicorn main:app --workers 4 --worker-class uvicorn.workers.UvicornWorker --bind=0.0.0.0:8000
