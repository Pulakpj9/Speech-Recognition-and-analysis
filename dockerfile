# Use the official Python image from the Docker Hub with the specified version
FROM python:3.12.1

# Set the working directory in the container
WORKDIR /app

# Copy the requirements.txt file into the container
COPY requirements.txt .

# Install the dependencies specified in the requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Download the SpaCy language model
RUN python -m spacy download en_core_web_sm

# Copy the rest of the application code into the container
COPY . .

# Expose the port that Streamlit uses
EXPOSE 8501

# Run the Streamlit app
CMD ["streamlit", "run", "app1.py"]