# イメージ
FROM node:21-alpine

# パッケージ最新化とインストール
RUN apk update && apk add git curl

# package.jsonとpackage-lock.jsonをコピー (キャッシュ効率化のため)
COPY ./frontend/package*.json ./

# 依存関係をインストール
RUN npm install

WORKDIR /workspace

CMD ["npm", "start"]