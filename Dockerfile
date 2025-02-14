# Use a base image with Python
FROM python:3.12

# Set the working directory inside the container
WORKDIR /usr/src/app

# Copy requirements file to install dependencies
COPY requirements.txt .

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy the rest of the application files
COPY . .

# Expose the port the app will run on
EXPOSE 5000

# Set the default command to run your Flask app
CMD ["python", "app.py"]
