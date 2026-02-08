FROM node:20-alpine AS build
WORKDIR /frontend
COPY frontend/package.json ./ 
COPY frontend/package-lock.json ./   # jetzt vorhanden
RUN npm install
COPY frontend/ ./
RUN npm run build

FROM ghcr.io/home-assistant/amd64-base:latest
WORKDIR /app
COPY app /app/app
COPY run.sh /app/run.sh
COPY --from=build /frontend/build /app/frontend

RUN apk add --no-cache python3 py3-pip
RUN pip3 install --no-cache-dir -r /app/app/requirements.txt
RUN chmod +x /app/run.sh

CMD ["/app/run.sh"]
