FROM python:latest
RUN mkdir -p /app
WORKDIR /app

COPY require.txt require.txt
RUN pip3 install -r require.txt

COPY . .

CMD [ "python", "main.py"]
