FROM alpine:3.18

RUN apk add --no-cahe python3-dev \
   && pip3 install --upgrade pip 

WORKDIR /app

COPY . /app

RUN pip3 --no-cache-dir install -r requirements.txt

CMD ["python3", "src/mi_pokeapi_app.py"]


