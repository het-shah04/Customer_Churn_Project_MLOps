FROM python:3.11-slim

WORKDIR /app

COPY requirements.txt .

RUN pip install --upgrade pip \
    && pip install -r requirements.txt \
    && apt-get clean && rm -rf /var/lib/apt/lists/*

COPY . .

# Explicitly copy model (in case .dockerignore excluded mlruns)
# NOTE: destination changed to /app/src/serving/model to match inference.py's path
COPY src/serving/model /app/src/serving/model

# Copy MLflow run (artifacts + metadata) to the flat /app/model convenience path
COPY src/serving/model/777697818682899649/models/m-e6469dbbfaf748c38ce4af1fb78f25e6/artifacts /app/model
COPY src/serving/model/777697818682899649/7fbee769856c4c24a3bda807be0f7a41/artifacts/feature_columns.txt /app/model/
COPY src/serving/model/777697818682899649/7fbee769856c4c24a3bda807be0f7a41/artifacts/preprocessing.pkl /app/model/

# make "serving" and "app" importable without the "src." prefix
# ensures logs are shown in real-time (no buffering).
# lets you import modules using from app... instead of from src.app....
ENV PYTHONUNBUFFERED=1 \
    PYTHONPATH=/app/src

CMD ["uvicorn", "src.app.main:app", "--host", "0.0.0.0", "--port", "8000"]

EXPOSE 8000