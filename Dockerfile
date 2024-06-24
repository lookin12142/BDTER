FROM python:3.10

WORKDIR /app

COPY requirements.txt /app/
RUN pip install -r requirements.txt


EXPOSE 8000

CMD ["gunicorn", "--bind", "0.0.0.0:8000", "baseteran .wsgi:application"]
