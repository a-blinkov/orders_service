# main part
FROM python:3.11

# Installing of Python packages
ADD ./* $HOME/code/
WORKDIR /code/openapi_server

ENV PYTHONPATH=/code/src:/code
ENV PYTHONUNBUFFERED=1
ENV PATH /home/${USERNAME}/.local/bin:${PATH}

RUN python -m pip install --upgrade pip
RUN python3.11 -m venv /venv
COPY requirements.txt .
RUN python -m pip install -r requirements.txt