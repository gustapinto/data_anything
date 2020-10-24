FROM python:3.8.6

WORKDIR /jupyter

COPY requirements.txt .

RUN pip install -r requirements.txt

COPY . .

EXPOSE 8888

ENTRYPOINT ["jupyter", "lab","--ip=0.0.0.0","--allow-root"]
