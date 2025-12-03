# --- Build Stage ---------------------------------------------------------
FROM node:20-alpine AS builder
WORKDIR /app
ARG VITE_API_BASE_URL
ENV VITE_API_BASE_URL=${VITE_API_BASE_URL}
COPY package*.json ./
RUN npm install --production=false
COPY . .
RUN npm run build-only


# --- Final Stage (Caddy) -------------------------------------------------
FROM caddy:2.10.2
WORKDIR /srv
COPY --from=builder /app/dist/ ./
COPY <<EOF /etc/caddy/Caddyfile
:3000 {
    encode gzip zstd

    handle {
        root * /srv
        try_files {path} /index.html
        file_server
    }
}
EOF
