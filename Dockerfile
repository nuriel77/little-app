FROM python:3.8-slim-buster

ENV TINI_VERSION v0.19.0

# Establish the runtime user (with no password and no sudo)
RUN useradd -m webapp

# create application workid
WORKDIR /app

# Install dependencies
ADD https://github.com/krallin/tini/releases/download/${TINI_VERSION}/tini /tini
ADD requirements.txt .
RUN chmod +x /tini && pip3 install --no-cache-dir -r requirements.txt

# Keep source code at the bottom to avoid unessesary build layers
ADD app.py .

USER webapp
ENTRYPOINT ["/tini", "--"]
CMD [ "python3", "-m" , "flask", "run", "--host=0.0.0.0"]
