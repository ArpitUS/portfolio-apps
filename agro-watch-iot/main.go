package main

import (
	"fmt"
	"net/http"

	_ "github.com/gorilla/mux" // temporary dummy import to trigger go.sum
)

func healthHandler(w http.ResponseWriter, r *http.Request) {
	w.Header().Set("Content-Type", "application/json")
	w.WriteHeader(http.StatusOK)
	fmt.Fprint(w, `{"status":"ok","service":"agro-watch-iot"}`)
}

func main() {
	http.HandleFunc("/health", healthHandler)
	fmt.Println("agro-watch-iot running on :8080")
	_ = http.ListenAndServe(":8080", nil)
}
