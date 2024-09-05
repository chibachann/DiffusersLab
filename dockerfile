FROM nvcr.io/nvidia/cuda:12.4.1-devel-ubuntu22.04

# 環境変数の設定
ENV DEBIAN_FRONTEND=noninteractive
ENV TZ=UTC

# 必要なパッケージのインストール
RUN apt-get update && apt-get install -y \
    nano \
    git \
    wget \
    curl \
    build-essential \
    cmake \
    libsm6 \
    libxext6 \
    libxrender-dev \
    libgl1-mesa-glx \
    libglib2.0-0 \
    python3.11 \
    python3.11-dev \
    python3.11-distutils \
    python3-pip \
    && rm -rf /var/lib/apt/lists/*

# Python 3.11をデフォルトに設定
RUN update-alternatives --install /usr/bin/python3 python3 /usr/bin/python3.11 1
RUN update-alternatives --set python3 /usr/bin/python3.11

# pipのアップグレードと必要なパッケージのインストール
RUN python3 -m pip install --upgrade pip setuptools wheel

RUN pip3 install torch torchvision torchaudio --index-url https://download.pytorch.org/whl/cu124

# 必要なライブラリをインストール
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# pythonコマンドをpython3にリンク
RUN ln -sf /usr/bin/python3 /usr/bin/python

# 環境変数の設定
ENV PATH="/usr/local/bin:${PATH}"

# エイリアスの設定
RUN echo "alias python=python3" >> ~/.bashrc
RUN echo "alias pip=pip3" >> ~/.bashrc
