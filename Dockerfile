FROM python:3.7

# Create a virtual environment
RUN python -m venv /venv
ENV PATH="/venv/bin:$PATH"

COPY . /app
WORKDIR /app

# Install the requirements inside the virtual environment
RUN pip install -r requirements.txt

EXPOSE 8080
CMD gunicorn --workers=4 --bind 0.0.0.0:8080 app:app