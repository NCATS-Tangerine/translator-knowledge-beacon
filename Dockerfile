FROM python:3.6

RUN mkdir -p /usr/src/app
WORKDIR /usr/src/app

COPY beacon_controller /usr/src/app/beacon_controller
COPY config /usr/src/app/config
COPY beacon /usr/src/app/beacon

COPY MANIFEST.in /usr/src/app/MANIFEST.in
COPY setup.py /usr/src/app/setup.py

RUN python setup.py install

WORKDIR /usr/src/app/beacon

EXPOSE 8080

ENTRYPOINT ["python3"]

CMD ["-m", "swagger_server"]
