FROM chibachann/cuda-pytorch:12.1-2.2.2-py3.11

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
