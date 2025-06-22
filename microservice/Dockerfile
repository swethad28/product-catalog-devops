# --------------------
# Stage 1: Builder
# --------------------
    FROM python:3.11-slim AS builder

    WORKDIR /app
    
    # Install dependencies early for cache
    COPY requirements.txt .
    RUN pip install --upgrade pip && \
        pip install --user -r requirements.txt
    
    # Copy app source code
    COPY app/ ./app
    COPY .env.example .env
    
    # --------------------
    # Stage 2: Runtime
    # --------------------
    FROM python:3.11-slim
    
    WORKDIR /app
    
    # Copy dependencies and code from builder stage
    COPY --from=builder /root/.local /root/.local
    COPY --from=builder /app /app
    
    ENV PATH=/root/.local/bin:$PATH
    
    # Expose the port
    EXPOSE 8000
    
    # Healthcheck
    HEALTHCHECK CMD curl --fail http://localhost:8000/health || exit 1
    
    # Run the app
    CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]
    