#!/bin/bash

alembic upgrade head

cd app

uvicorn app.main:app --host 127.0.0.1 --port 8000 --reload