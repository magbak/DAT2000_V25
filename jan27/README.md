## DAT 2000 Øving 26. Januar 2025

### Postgres

Starte postgres med Docker:

```shell
docker run -p 5432:5432 --name some-postgres -e POSTGRES_PASSWORD=mysecretpassword -d postgres
```

### Noen nyttige kommandoer:

List kjørende kontainere

```shell
docker ps
```

Stopp en kjørende kontainer

```shell
docker stop some-postgres
```

List også stoppede kontainere

```shell
docker ps -a
```

Start en stoppet kontainer

```shell
docker start some-postgres
```

Slett kontaineren, husk å slette volum med -v, hvis ikke kan det bli mye liggende

```shell
docker rm -v some-postgres
```