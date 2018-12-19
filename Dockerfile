FROM python:2.7
COPY app.py /opt/fakestagram-app/app.py
COPY static /opt/fakestagram-app/static 
COPY templates /opt/fakestagram-app/templates
RUN pip install flask
ENTRYPOINT ["/opt/fakestagram-app/app.py"]
