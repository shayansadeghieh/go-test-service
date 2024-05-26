package main

import (
	"fmt"
	"io"
	"log"
	"net/http"
)

func main() {
	// server.StartServer()

	serverUrl := "http://localhost:3333/"
	resp, err := http.Get(serverUrl)
	if err != nil {
		log.Fatal(err)
	}

	defer resp.Body.Close()

	body, err := io.ReadAll(resp.Body)
	if err != nil {
		log.Fatal(err)
	}
	fmt.Println(string(body))
}
