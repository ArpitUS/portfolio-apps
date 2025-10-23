# =======================================
# Stage 1: Build the Vite app
# =======================================
FROM node:20-alpine AS build

WORKDIR /app

# Add lightweight build tools only when needed
RUN apk add --no-cache python3 make g++ 

# Copy dependency files
COPY package*.json ./

# Install dependencies safely (prevent OOM errors)
RUN npm ci --legacy-peer-deps --no-audit --no-fund || npm install --legacy-peer-deps --no-audit --no-fund

# Copy rest of the source
COPY . .

# Increase memory for Node during build
ENV NODE_OPTIONS=--max-old-space-size=2048

# Build production app
RUN npm run build

# =======================================
# Stage 2: Serve with Nginx
# =======================================
FROM nginx:alpine

# Copy the build output to Nginx’s HTML folder
COPY --from=build /app/dist /usr/share/nginx/html

# Expose port 80 for Render
EXPOSE 80

CMD ["nginx", "-g", "daemon off;"]
