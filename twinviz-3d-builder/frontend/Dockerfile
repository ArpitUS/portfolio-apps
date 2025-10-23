# ==========================
# Stage 1: Build frontend
# ==========================
FROM node:20-alpine AS build

WORKDIR /app

# Install build dependencies for native modules
RUN apk add --no-cache python3 make g++

# Copy package files first
COPY package*.json ./

# Use npm ci for reproducible builds and retry on failure
RUN npm ci --legacy-peer-deps --no-audit --no-fund || npm install --legacy-peer-deps --no-audit --no-fund

# Copy all other files
COPY . .

# Increase memory limit to prevent Render OOM
ENV NODE_OPTIONS=--max-old-space-size=2048

# Build the production app
RUN npm run build

# ==========================
# Stage 2: Serve via NGINX
# ==========================
FROM nginx:alpine

# Copy built app
COPY --from=build /app/dist /usr/share/nginx/html

# Expose HTTP port
EXPOSE 80

CMD ["nginx", "-g", "daemon off;"]
