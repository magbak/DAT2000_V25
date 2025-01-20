# DAT2000_V25

## Nyttige kommandoer


Installere avhengighetene til appen
```shell
cd jan20
cd app
pip install -r requirements.txt
```


Starte appen (antar at du er i jan20/app)
```shell
fastapi dev app.py
```

Bygge docker (antar at du er i app..)
```shell
docker build . -t myapp
```

Kjøre docker 
```shell
docker run myapp
```

