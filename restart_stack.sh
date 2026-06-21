#!/usr/bin/env bash
set -e
cd "$(dirname "$0")"
echo "[1/4] Arret de l'ancienne stack..."
docker compose down --remove-orphans || true

echo "[2/4] Liberation des conteneurs occupant les ports..."
for P in 8000 8001 8501 9090 3000; do
  ids=$(docker ps -q --filter "publish=$P")
  [ -n "$ids" ] && docker rm -f $ids || true
done

echo "[3/4] Suppression d'eventuels conteneurs nommes..."
docker rm -f prometheus grafana 2>/dev/null || true

echo "[4/4] (Re)construction et demarrage..."
docker compose up --build
