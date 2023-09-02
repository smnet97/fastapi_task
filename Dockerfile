FROM python:3.11.5-slim

WORKDIR /fastapi_task

COPY . /fastapi_task

RUN pip install -r requirements.txt

CMD ["uvicorn", "src.main:app", "--host", "127.0.0.1", "--port", "8000"]