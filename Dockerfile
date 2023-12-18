FROM python:3.11
WORKDIR /app
COPY . /app/

# Installing dependencies:
RUN pip install --no-cache-dir -r requirements.txt

CMD ["python", "WeatherData.py"]