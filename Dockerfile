FROM python:3.9-alpine

WORKDIR /app

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt && \
    rm -rf /root/.cache/pip

COPY create_envs_and_secrets.py .

CMD ["python", "create_envs_and_secrets.py"]