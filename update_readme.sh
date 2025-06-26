#!/bin/bash
# Script para atualiza��o autom�tica do README
# Adicione este script ao seu cron job ou GitHub Actions

cd "$(dirname "$0")"
python update_readme.py

# Se estiver usando Git, commit das mudan�as
if git diff --quiet README.md; then
    echo "README.md n�o foi modificado"
else
    git add README.md
    git commit -m "docs: atualiza��o autom�tica do README"
    echo "README.md atualizado e commitado"
fi
