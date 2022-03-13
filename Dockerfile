FROM python:3.10.2

# The enviroment variable ensures that the python output is set straight
# to the terminal with out buffering it first
ENV PYTHONUNBUFFERED 1

# create root directory for our project in the container
RUN mkdir /apirest
# Set the working directory to /nazmiblog
WORKDIR /restapi
# Copy the current directory contents into the container at /nazmiblog
ADD . /restapi/
# Install any needed packages specified in requirements.txt
RUN pip install -r requirements.txt
#tell containers to listen on port 8080 during runtime..tpi x tahu kena specify tcp or udp protocol ke idok
EXPOSE 8080
#tell container to execute this after starting ni dalam json format host 0.0.0.0
ENV DBHOST lin-1040-1128-mysql-primary.servers.linodedb.net
ENV DBNAME world
ENV DBUSER linroot
ENV DBPASSWORD xdzA,e2ERRHKtEuA
CMD ["python", "manage.py", "runserver", "0.0.0.0:8080"]