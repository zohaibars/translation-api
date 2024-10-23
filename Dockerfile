FROM tiangolo/uvicorn-gunicorn-fastapi:python3.11

# Set Work Directory
WORKDIR /app

# Copy dependencies
COPY requirements.txt /app

# Install dependencies
RUN pip install -r requirements.txt

# Install git and git-lfs
RUN apt-get update && apt-get install -y git && \
    curl -s https://packagecloud.io/install/repositories/github/git-lfs/script.deb.sh | bash && \
    apt-get install -y git-lfs && \
    git lfs install

# Copy setup script for IndicTransTokenizer
COPY setup.sh /app/setup.sh

# Make setup script executable
RUN chmod +x /app/setup.sh

# Run setup script
RUN /app/setup.sh

# Add IndicTransTokenizer to PYTHONPATH
ENV PYTHONPATH "${PYTHONPATH}:/app/IndicTransTokenizer"

# Copy model
# COPY indictrans2-en-indic-1B app/

# Copy main application
COPY app.py /app

# Expose port
EXPOSE 8091

# Command to run the application
CMD ["python3", "app.py"]
