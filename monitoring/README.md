# Monitoring — Prometheus + Grafana

Stack d'observabilité pour les APIs FastAPI du projet (api_data, api_ia).

## Architecture

- **APIs FastAPI** : exposent leurs métriques sur `/metrics`
  (via `prometheus-fastapi-instrumentator`).
- **Prometheus** (port `9090`) : scrape `/metrics` toutes les 15 s.
- **Grafana** (port `3000`) : visualise les métriques, datasource et
  dashboard provisionnés automatiquement.

## Lancement

```bash
docker compose up --build
```

## Accès

| Service     | URL                          | Identifiants     |
|-------------|------------------------------|------------------|
| API Data    | http://localhost:8001/docs   | —                |
| API IA      | http://localhost:8000/docs   | —                |
| Métriques   | http://localhost:8001/metrics<br>http://localhost:8000/metrics | — |
| Prometheus  | http://localhost:9090         | —                |
| Grafana     | http://localhost:3000         | admin / admin    |

Dans Grafana, le dashboard **« DevIA — Monitoring APIs Ferroviaires »**
est déjà chargé (datasource Prometheus configurée automatiquement).

## Fichiers

```
monitoring/
├── prometheus.yml                       # config de scrape
├── grafana/
│   ├── provisioning/
│   │   ├── datasources/datasource.yml   # datasource Prometheus auto
│   │   └── dashboards/dashboard.yml     # provider de dashboards
│   └── dashboards/devia_dashboard.json  # le dashboard
├── grafana_dashboard_mockup.png         # visuel (soutenance)
└── grafana_dashboard_mockup.svg
```

## Métriques principales

- `http_requests_total` — nombre de requêtes (labels : handler, method, status)
- `http_request_duration_seconds_bucket` — histogramme de latence (p50/p95/p99)
- `up` — disponibilité des cibles scrappées
