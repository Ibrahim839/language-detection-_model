FROM python:3.11


WORKDIR /src/usr/api

COPY ./api .

EXPOSE 5000


RUN pip install -r requirements.txt

CMD ["flask", "--app=./api", "run", "--host=0.0.0.0", "--port=5000"]