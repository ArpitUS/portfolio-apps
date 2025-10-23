# ==========================
# Stage 1: Build frontend
# ==========================
FROM node:20-alpine AS build

WORKDIR /app

# Add system packages for npm builds
RUN apk add --no-cache python3 make g++

# Copy package files
COPY package*.json ./

# Use legacy-peer-deps for compatibility & ensure deterministic install
RUN npm ci --legacy-peer-deps || npm install --legacy-peer-deps

# Copy the rest of your code
COPY . .

# Prevent memory-related crashes
ENV NODE_OPTIONS=--max-old-space-size=2048

# Build the project
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
