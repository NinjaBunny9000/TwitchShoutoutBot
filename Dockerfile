FROM python:3.6.9-alpine

RUN python -m pip install pipenv

WORKDIR /usr/app

COPY ./Pipfile ./Pipfile.lock ./
RUN pipenv install

COPY . .

CMD ["python", "--version"]
