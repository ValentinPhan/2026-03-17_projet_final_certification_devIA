@echo off
cd /d "%~dp0"
echo [1/4] Arret de l'ancienne stack...
docker compose down --remove-orphans

echo [2/4] Liberation des conteneurs occupant les ports 8000/8001/8501/9090/3000...
for %%P in (8000 8001 8501 9090 3000) do (
  for /f %%i in ('docker ps -q --filter "publish=%%P"') do docker rm -f %%i
)

echo [3/4] Suppression d'eventuels conteneurs nommes...
docker rm -f prometheus grafana 2>nul

echo [4/4] (Re)construction et demarrage...
docker compose up --build
