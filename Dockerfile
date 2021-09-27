FROM python:3-alpine

LABEL description="Dockerfile for Python Exquiste Corpse"

COPY exquisite.py /app/
COPY exquisiteOM.py /app/
COPY vocabulary1.py /app/

CMD python3 /app/exquisite.py