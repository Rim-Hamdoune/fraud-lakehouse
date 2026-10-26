# Lakehouse de détection de fraude bancaire

Projet big data : plateforme data de détection de fraude sur ~6,3 millions de transactions
(jeu de données PaySim), en architecture médaillon (bronze / silver / gold).

**Stack prévue :** PySpark, Delta Lake, MinIO, Airflow, MLflow, LightGBM, SHAP, PostgreSQL,
Power BI, Docker Compose, GitHub Actions, Azure.

> 🚧 Projet en cours de construction.

## Structure du dépôt

| Dossier | Contenu |
|---|---|
| `src/fraud_lakehouse/` | Code de production (ingestion, transformations, features, qualité, ML) |
| `dags/` | DAGs Airflow |
| `notebooks/` | Exploration uniquement, pas de logique de production |
| `tests/` | Tests pytest |
| `powerbi/` | Dashboard Power BI et captures |
| `docs/` | Architecture et décisions techniques |
| `data/` | Données locales, non versionnées |
