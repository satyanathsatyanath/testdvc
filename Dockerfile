FROM python:3.10-slim

WORKDIR /app

RUN apt-get update && apt-get install -y git

COPY . .

RUN pip install -r requirements.txt

# ✅ Initialize Git and DVC for full versioning
RUN git init && dvc init

CMD ["bash"]
