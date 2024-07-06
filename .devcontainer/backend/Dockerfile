FROM ubuntu:20.04

# 必要なパッケージをインストール
RUN apt-get update && \
    apt-get install -y git python3 python3-pip && \
    apt-get clean

# ワークスペースを作成
WORKDIR /workspace/backend
COPY backend/requirements.txt /workspace/backend/

RUN pip3 install -r requirements.txt