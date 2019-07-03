FROM python:2.7
COPY . /app
WORKDIR /app
RUN pip install flask
RUN pip install flask_restful
ENTRYPOINT ["python"]
CMD ["app.py"]
