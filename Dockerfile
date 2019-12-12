FROM python:3.6
ENV APP /app
RUN mkdir $APP
WORKDIR $APP

COPY *.py .
COPY requirements.txt .

RUN pip install -r requirements.txt

CMD ["python", "mqtt-esp32.py"]