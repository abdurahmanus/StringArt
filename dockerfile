FROM python:3.13

WORKDIR /app

ADD requirements.txt /app/
ADD api.py /app/

RUN pip install --upgrade pip
RUN pip install --no-cache-dir -r requirements.txt

EXPOSE 8000 

CMD ["python", "api.py"]