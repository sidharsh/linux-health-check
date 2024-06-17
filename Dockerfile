FROM python:3.9-slim

WORKDIR /app

# Install pyATS and required dependencies
RUN pip install pyats[full]

# Copy your PyATS script and the configuration file into the container
COPY linux_health_check_job.py /app/
COPY config.yaml /app/

# Command to run your PyATS script with the YAML file path
CMD ["pyats", "run", "job", "linux_health_check_job.py"]
