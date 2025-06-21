# Stage 1: Build
FROM node:20-alpine as builder

WORKDIR /app
COPY . .
RUN npm install && npm run build

# Stage 2: Serve
FROM nginx:alpine

COPY --from=builder /app/dist /usr/share/nginx/html
EXPOSE 80
