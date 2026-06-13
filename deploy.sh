#!/bin/bash
echo "🧹 Limpiando caché anterior (.web)..."
rm -rf .web

echo "🚀 Iniciando despliegue de Reflex..."
reflex deploy

echo "✅ Proceso completado."
