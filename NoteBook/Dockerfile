FROM jupyter/base-notebook:latest


WORKDIR /src/usr/notebook

COPY ./NoteBook .

EXPOSE 80


RUN pip install -r requirements.txt

CMD ["jupyter", "notebook", "--ip=0.0.0.0", "--port=80"]