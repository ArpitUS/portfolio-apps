# ===============================
# Stage 1: Build the Vite frontend
# ===============================
FROM node:20-alpine AS build

# Set working directory
WORKDIR /app

# Add system dependencies for native npm modules
RUN apk add --no-cache python3 make g++

# Copy package files first for caching
COPY package*.json ./

# Install dependencies safely (avoid peer issues)
RUN npm install --legacy-peer-deps

# Copy the remaining project files
COPY . .

# Build production version
RUN npm run build

# ===============================
# Stage 2: Serve static files with NGINX
# ===============================
FROM nginx:alpine

# Copy built files from build stage
COPY --from=build /app/dist /usr/share/nginx/html

# Expose port 80
EXPOSE 80

# Start NGINX
CMD ["nginx", "-g", "daemon off;"]
