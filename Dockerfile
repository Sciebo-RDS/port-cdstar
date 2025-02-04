FROM zivgitlab.uni-muenster.de/sciebo-rds/dependency_proxy/containers/python:3.8
EXPOSE 8080

# set the base installation, requirements are not changed often
RUN pip install --upgrade pip setuptools wheel

WORKDIR /app
ADD ./requirements.txt ./cdstar.png ./
RUN pip install -r requirements.txt

ENV OPENAPI_MULTIPLE_FILES      "interface_port_metadata.yml"

ADD "https://raw.githubusercontent.com/Sciebo-RDS/Sciebo-RDS/master/RDS/circle2_use_cases/interface_port_metadata.yml" ./

# now add everything else, which changes often
ADD src ./

ENTRYPOINT [ "python", "server.py" ]