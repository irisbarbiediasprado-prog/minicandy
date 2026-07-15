#!/data/data/com.termux/files/usr/bin/bash

set -e

echo "🍬 MiniCandy Bootstrap"
echo

echo "[1/5] Atualizando pacotes..."
pkg update -y
pkg upgrade -y

echo
echo "[2/5] Instalando dependências..."
pkg install -y \
    git \
    python \
    curl \
    wget \
    nano \
    tree \
    zip \
    unzip \
    openssh \
    ripgrep \
    jq

echo
echo "[3/5] Configurando armazenamento..."
termux-setup-storage || true

echo
echo "[4/5] Configurando Git..."
git config --global init.defaultBranch main
git config --global pull.rebase false
git config --global core.editor nano
git config --global color.ui auto

echo
echo "[5/5] Verificando ambiente..."
git --version
python3 --version

echo
echo "✅ Bootstrap concluído!"
echo
echo "Próximo passo:"
echo "python3 -m cli doctor"
