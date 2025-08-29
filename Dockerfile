FROM apache/airflow:2.7.2-python3.11

COPY requirements.txt /opt/airflow/

USER root
RUN apt-get update && apt-get install -y \
    gcc \
    python3-dev \
    unzip \
    curl \
    && rm -rf /var/lib/apt/lists/* \
    && curl "https://awscli.amazonaws.com/awscli-exe-linux-x86_64.zip" -o "awscliv2.zip" \
    && unzip awscliv2.zip \
    && ./aws/install \
    && rm -rf awscliv2.zip aws/

USER airflow
RUN pip install --no-cache-dir -r /opt/airflow/requirements.txt
