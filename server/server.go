package server

import (
	"log"
	"net/http"
)

func StartServer() {
	http.HandleFunc("/", printHello)

	err := http.ListenAndServe(":3333", nil)
	if err != nil {
		log.Fatalf("Failed to listen and serve: %v", err)
	}

}

func printHello(w http.ResponseWriter, r *http.Request) {
	fmt.Printf("got / request\n")
	io.WriteString(w, "This is my website!\n")
}
