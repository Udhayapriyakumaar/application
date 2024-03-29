FROM python:3.9.5-slim-buster

# Install required dependencies
RUN apt-get update && \
    apt-get install -y libsm6 libxext6 libxrender-dev libgl1-mesa-glx libglib2.0-0

# Add your application code
ADD . /app

WORKDIR /app

# Install Python dependencies
RUN pip3 install -r requirements.txt

# Install AVX2 and FMA-enabled TensorFlow
RUN pip3 uninstall -y tensorflow
RUN pip3 install -U tensorflow

# Copy your model file
COPY model.h5 /app

# EXPOSE 5000

CMD ["python", "app.py"]