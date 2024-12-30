# Use an x86_64-compatible base image
FROM --platform=linux/amd64 ubuntu:22.04

# Install dependencies
RUN apt-get update && \
    apt-get install -y python3 python3-pip libc6 wget gcc && \
    pip3 install streamlit && \
    wget https://bellard.org/ts_sms/ts_sms-2024-12-26.tar.gz && \
    tar -xzf ts_sms-2024-12-26.tar.gz

# Copy app files
WORKDIR /app
COPY app /app
COPY ts_sms-2024-12-26 /app/ts_sms-2024-12-26

# Expose Streamlit default port
EXPOSE 8501

# Run Streamlit app
CMD ["streamlit", "run", "streamlit_app.py", "--server.port=8501", "--server.address=0.0.0.0"]