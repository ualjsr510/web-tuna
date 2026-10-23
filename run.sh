#!/usr/bin/env bash
# Script de arranque del Servidor Web Seguro de la Tuna de Derecho de Almería

cd "$(dirname "$0")"

PORT="${1:-8080}"

echo "=========================================================="
echo "  Iniciando Portal Web - Tuna de Derecho de Almería"
echo "  Base de datos: database/tuna.db"
echo "  Puerto: $PORT"
echo "=========================================================="

# Liberar el puerto si ya está en uso por una instancia previa
if command -v fuser >/dev/null 2>&1; then
    PIDS_OCUPADOS=$(fuser "$PORT"/tcp 2>/dev/null)
    if [ -n "$PIDS_OCUPADOS" ]; then
        echo "[!] Puerto $PORT ocupado por proceso(s): $PIDS_OCUPADOS. Liberando..."
        fuser -k -TERM "$PORT"/tcp 2>/dev/null
        sleep 1
        PIDS_RESTANTES=$(fuser "$PORT"/tcp 2>/dev/null)
        if [ -n "$PIDS_RESTANTES" ]; then
            fuser -k -9 "$PORT"/tcp 2>/dev/null
            sleep 0.5
        fi
        echo "[+] Puerto $PORT liberado correctamente."
    fi
fi

# Inicializar base de datos si no existe
if [ ! -f "database/tuna.db" ]; then
    echo "[*] Base de datos no encontrada. Inicializando..."
    python3 database/init_db.py
fi

# Iniciar servidor seguro reemplazando el proceso bash
exec python3 server.py "$PORT"
