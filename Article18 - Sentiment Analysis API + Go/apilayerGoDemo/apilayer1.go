package main

import (
  "fmt"
  "strings"
  "net/http"
  "io/ioutil"
)

func main() {
  url := "https://api.apilayer.com/sentiment/analysis"

  payload := strings.NewReader("This restaurant has a lovely atmosphere and the staff is great!")

  client := &http.Client {}
  req, err := http.NewRequest("POST", url, payload)
  req.Header.Set("apikey", "YOUR_ACCESS_KEY")

  if err != nil {
    fmt.Println(err)
  }
  res, err := client.Do(req)
	if res.Body != nil {
    defer res.Body.Close()
  }
  body, err := ioutil.ReadAll(res.Body)

  fmt.Println(string(body))
}