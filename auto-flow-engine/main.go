package main

import (
	"encoding/json"
	"fmt"
	"log"
	"net/http"
	"os"
	"time"

	"github.com/gorilla/mux"
)

// HealthResponse defines the JSON structure for /health
type HealthResponse struct {
	Status  string `json:"status"`
	Service string `json:"service"`
	Time    string `json:"time"`
}

// TriggerResponse defines the JSON structure for /trigger
type TriggerResponse struct {
	Status     string `json:"status"`
	WorkflowID string `json:"workflow_id"`
	Message    string `json:"message"`
	Time       string `json:"time"`
}

// handleHealth responds to GET /health
func handleHealth(w http.ResponseWriter, r *http.Request) {
	response := HealthResponse{
		Status:  "ok",
		Service: "auto-flow-engine",
		Time:    time.Now().Format(time.RFC3339),
	}
	w.Header().Set("Content-Type", "application/json")
	json.NewEncoder(w).Encode(response)
}

// handleTrigger simulates a workflow trigger endpoint
func handleTrigger(w http.ResponseWriter, r *http.Request) {
	type RequestBody struct {
		WorkflowID string `json:"workflow_id"`
	}

	var req RequestBody
	if err := json.NewDecoder(r.Body).Decode(&req); err != nil {
		http.Error(w, "Invalid JSON payload", http.StatusBadRequest)
		return
	}

	response := TriggerResponse{
		Status:     "success",
		WorkflowID: req.WorkflowID,
		Message:    fmt.Sprintf("Workflow %s triggered successfully", req.WorkflowID),
		Time:       time.Now().Format(time.RFC3339),
	}

	w.Header().Set("Content-Type", "application/json")
	json.NewEncoder(w).Encode(response)
}

func main() {
	r := mux.NewRouter()

	// Register routes
	r.HandleFunc("/health", handleHealth).Methods("GET")
	r.HandleFunc("/trigger", handleTrigger).Methods("POST")

	// Get port from environment or default
	port := os.Getenv("PORT")
	if port == "" {
		port = "8080"
	}

	log.Printf("🚀 Auto-Flow Engine service running on port %s", port)
	log.Fatal(http.ListenAndServe(":"+port, r))
}
