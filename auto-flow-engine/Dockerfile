FROM golang:1.23.4-alpine3.19 AS builder
WORKDIR /app
COPY go.mod go.sum ./
RUN go mod download
COPY . .
# Build a static binary to allow using a minimal final image (scratch)
RUN CGO_ENABLED=0 GOOS=linux GOARCH=amd64 go build -ldflags="-s -w" -o /app/main .

FROM scratch
# Copy the statically linked binary from the builder stage
COPY --from=builder /app/main /main
# Use a simple entrypoint for the minimal final image
CMD ["/main"]
