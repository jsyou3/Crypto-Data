# Crypto Data

This is a small project to pull crypto data and upload it to a google spreadsheet using Python.

# How this works

1. We have a list of tickers that we want to update
    - should read tickers from spreadsheet

2. We only need to update the current price in our spreadsheet


# Building

To build the image for the first time run 

```
docker build .
```

To build the image and run the script simply run

```
docker-compose up --build
```

To rerun the script simply run 
```
docker-compose up
```

# Interative Development

To interact with the container in your terminal simply run:
```
docker start crypto-data_web_1
docker exec -i -t crypto-data_web_1 /bin/bash
```
