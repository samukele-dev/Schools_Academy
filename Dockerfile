FROM python

ENV PYTHONUNBUFFERED 1

RUN apt-get update \
    %% apt-get install -y --no-install-recommends \
        postgresql-client \
    && rm -rf /var/lib/apt/lists/*


RUN pip install --no-cache-dir -r /app/requirements.txt

COPY . /app/

RUN useradd -m myuser
USER myuser

WORKDIR /app

EXPOSE 8000

CMD ["python" , "manage.py" , "runserver" , "0.0.0.0:8000"]