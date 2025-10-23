# syntax=docker/dockerfile:1

# builder stage
FROM golang:1.23.4-alpine3.19 AS builder
WORKDIR /app

# copy module files and download dependencies
COPY go.mod go.sum ./
RUN go mod download

# copy source code and build static binary
COPY . .
RUN CGO_ENABLED=0 GOOS=linux GOARCH=amd64 go build -ldflags="-s -w" -o /main .

# final minimal stage
FROM scratch
COPY --from=builder /main /main

ENTRYPOINT ["/main"]
