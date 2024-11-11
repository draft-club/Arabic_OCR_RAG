# Base image with Python
FROM python:3.9-slim

# Set environment variables
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

# Set the working directory inside the container
WORKDIR /app

# Copying all project files to container
COPY . .

# Install dependencies
RUN apt update \
    && xargs -a linux_packages.txt apt install -y \
    #Cleaning ----------------------
    && apt clean \
    && rm -rf /var/lib/apt/lists/* \
    #-------------------------------
    && pip install --upgrade pip \
    && pip install --no-cache-dir -r requirements.txt

# Expose the port Streamlit will run on
EXPOSE 8501

# Run the Streamlit app
CMD ["streamlit", "run", "/app/streamlit_app/app.py", "--server.port=8501"]
