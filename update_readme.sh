#!/bin/bash
# Script para atualização automática do README
# Adicione este script ao seu cron job ou GitHub Actions

cd "$(dirname "$0")"
python update_readme.py

# Se estiver usando Git, commit das mudanças
if git diff --quiet README.md; then
    echo "README.md não foi modificado"
else
    git add README.md
    git commit -m "docs: atualização automática do README"
    echo "README.md atualizado e commitado"
fi
