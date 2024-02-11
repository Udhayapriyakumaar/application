FROM python:3.9.5-slim-buster

RUN apt-get update && \
    apt-get install -y libsm6 libxext6 libxrender-dev libgl1-mesa-glx libglib2.0-0

ADD . /app

WORKDIR /app

RUN pip3 install -r requirements.txt

RUN pip3 install -U tensorflow

# Copy your model file
COPY model.h5 /app

# EXPOSE 5000

CMD ["python", "app.py"]
