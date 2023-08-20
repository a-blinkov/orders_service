# main part
FROM python:3.11

# Installing of Python packages
COPY ./ $HOME/code/

WORKDIR /code

ENV PYTHONPATH=/code
ENV PYTHONUNBUFFERED=1
ENV PATH /home/${USERNAME}/.local/bin:${PATH}
ENV PATH="$PATH:/bin"


RUN python -m pip install --upgrade pip
RUN python3.11 -m venv /venv
COPY requirements.txt .
RUN python -m pip install  -r requirements.txt
