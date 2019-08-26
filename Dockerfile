FROM python:3.7
COPY ./requirements.txt /usr/src/app/requirements.txt
WORKDIR /usr/src/app
RUN pip3 install --upgrade pip
RUN pip install -r requirements.txt
COPY . /usr/src/app
EXPOSE 5000
