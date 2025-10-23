# builder stage: compile a static Go binary
FROM golang:1.23.4-alpine3.19 AS builder
WORKDIR /app

# download dependencies first for better caching
COPY go.mod go.sum ./
RUN go mod download

# copy the rest of the source and build a static binary
COPY . .
RUN CGO_ENABLED=0 GOOS=linux GOARCH=amd64 go build -ldflags="-s -w" -o /main .

# final stage: minimal image with only the binary and CA certs
FROM scratch
# copy CA certs from the builder so TLS works (if needed)
COPY --from=builder /etc/ssl/certs/ca-certificates.crt /etc/ssl/certs/ca-certificates.crt
COPY --from=builder /main /main

# run as non-root if your binary supports it (optional)
# USER 1000

ENTRYPOINT ["/main"]
