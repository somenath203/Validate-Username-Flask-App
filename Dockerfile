FROM python:3.11.2

COPY ./requirements.txt /main/requirements.txt 

WORKDIR /main

RUN pip install -r requirements.txt

COPY . /main

ENTRYPOINT [ "python" ]

CMD [ "app.py" ]