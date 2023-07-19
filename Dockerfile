FROM python:3.10

WORKDIR /code

COPY ./requirements.txt /code/requirements.txt

# Creating a destination folder for uploaded files
RUN mkdir /code/uploads

RUN pip install --no-cache-dir --upgrade -r /code/requirements.txt

COPY ./app /code/app

CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]