# # Use the official Python image from the Docker Hub with the specified version
# FROM python:3.12.1

# # Set the working directory in the container
# WORKDIR /app

# # Copy the requirements.txt file into the container
# COPY requirements.txt .

# # Install the dependencies specified in the requirements.txt
# RUN pip install --no-cache-dir -r requirements.txt

# # Download the SpaCy language model
# RUN python -m spacy download en_core_web_sm

# # Copy the rest of the application code into the container
# COPY . .

# # Expose the port that Streamlit uses
# EXPOSE 8501

# # Run the Streamlit app
# CMD ["streamlit", "run", "app1.py"]

# Use the official Python image from the Docker Hub with the specified version
FROM python:3.12.1

# Set the working directory in the container
WORKDIR /app

# Install dependencies for Python virtual environment (optional, but recommended)
RUN apt-get update && apt-get install -y \
    python3-venv \
    && rm -rf /var/lib/apt/lists/*

# Create a virtual environment in the container
RUN python -m venv /app/venv

# Activate the virtual environment and install the dependencies specified in the requirements.txt
COPY requirements.txt .
RUN /app/venv/bin/pip install --no-cache-dir -r requirements.txt

# Download the SpaCy language model inside the virtual environment
RUN /app/venv/bin/python -m spacy download en_core_web_sm

# Copy the rest of the application code into the container
COPY . .

# Expose the port that Streamlit uses
EXPOSE 8501

# Run the Streamlit app using the virtual environment's Python
CMD ["/app/venv/bin/streamlit", "run", "app1.py"]
