FROM rman:1.0
USER root
RUN yum install  -y python3 epel-release python-pip nc
USER oracle
COPY ./requirements.txt /app/requirements.txt
WORKDIR /app
RUN pip3 install -r requirements.txt  --user
COPY . /app
CMD [ "python3", "./app.py" ]
EXPOSE 8080
