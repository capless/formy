FROM capless/capless-docker:jupyter
COPY . /code
RUN poetry run pip install --upgrade pip
RUN poetry install
