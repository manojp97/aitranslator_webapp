FROM python:3.9

WORKDIR /code

# Copy requirements first
COPY requirements.txt .

# Install Python libraries
RUN pip install --no-cache-dir -r requirements.txt

# Copy project files
COPY . .

# Run the Flask app
CMD ["python", "app.py"]