#!/usr/bin/env bash
# Script de arranque del Servidor Web Seguro de la Tuna de Derecho de Almería

cd "$(dirname "$0")"

PORT="${1:-8080}"

echo "=========================================================="
echo "  Iniciando Portal Web - Tuna de Derecho de Almería"
echo "  Base de datos: database/tuna.db"
echo "  Puerto: $PORT"
echo "=========================================================="

# Inicializar base de datos si no existe
if [ ! -f "database/tuna.db" ]; then
    echo "[*] Base de datos no encontrada. Inicializando..."
    python3 database/init_db.py
fi

# Iniciar servidor seguro
python3 server.py "$PORT"
