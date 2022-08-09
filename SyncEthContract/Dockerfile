FROM python:3.6
WORKDIR /docker_test
COPY flask_test .
RUN pip install flask
EXPOSE 5000
CMD ["python3","./app.py"]