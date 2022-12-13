FROM python:3.9

#ENV PYTHONPATH "${PYTHONPATH}:/Finalproject"
#ENV PYTHONDONTWRITEBYTECODE 1
#ENV PYTHONUNBUFFERED 1

WORKDIR /seq_converter

COPY requirements.txt .
RUN pip install -r requirements.txt

COPY ./app ./app

CMD ["python", "app/main.py"]
