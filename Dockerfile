FROM python:3-alpine

RUN pip install envparse

ADD main.py /
ADD utils.py /

USER 1001
CMD [ "python3", "/main.py" ]
