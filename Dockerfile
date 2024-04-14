# Install base Python image
FROM python:3.11-slim-buster

# Install libgl1-mesa-glx
RUN apt-get update && apt-get install -y libgl1-mesa-glx

# Copy files to the container
COPY *.py /app/
COPY requirements.txt /app/

# Set working directory to previously added app directory
WORKDIR /app/

# Install dependencies
RUN pip install --upgrade pip
RUN pip install -r requirements.txt
RUN python main.py


# Expose the port uvicorn is running on
EXPOSE 80

# Run uvicorn server
CMD ["uvicorn", "main:app", "--reload", "--host", "0.0.0.0", "--port", "80"]