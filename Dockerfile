FROM python:3.10.4-alpine3.15
WORKDIR /app
COPY . .
RUN pip3 install -r requirements.txt
CMD [ "uvicorn", "main:app", "--host", "0.0.0.0", "--port", "42069"]
