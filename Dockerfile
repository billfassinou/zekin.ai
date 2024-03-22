# utiliser la commande 'docker search python' pour connaitre l'image de base Python à utiliser
FROM python

COPY . /app

WORKDIR /app


# utiliser pip ou pip3, selon la version que vous avez installé
RUN pip3 install --break-system-packages -r requirements.txt

EXPOSE 8000

CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]
