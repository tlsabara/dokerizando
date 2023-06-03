FROM python:3.10
LABEL authors="tlsabara"

ENV ROOT_DIR=/code
ENV FLASK_APP=app.py
ENV FLASK_ENV=development
ENV FLASK_DEBUG=0

WORKDIR $ROOT_DIR

COPY ./ $ROOT_DIR

RUN pip install --upgrade pip
RUN pip install -r requirements.txt

EXPOSE 5000

CMD python -m flask run
