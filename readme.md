# API SII - Ricardo Vaca

## Run the project

1. make install
2. make up

### Run the tests

1. make test

## Information

### Description

This is a Web API that uses web scraping to find the Development Unit (Unidad de Fomento (UF)) from https://www.sii.cl/

### Technologies

- Python
- FastAPI (web server)
- BeautifulSoup (web scraping)

### Folder structure

This projects was built within a Clean Architecture.

![Clean Architecture](https://miro.medium.com/v2/resize:fit:800/1*0R0r00uF1RyRFxkxo3HVDg.png)

### Tests

This is the list of the tests that are completed:

- `unit/cases`
- `unit/endpoints`

This is the list of the tests that can be added:

- `unit/implementations`
- `contract`
- `integration`

## Endpoints

1. Get development unit by date

```
GET /development-unit/{date with dd-mm-YYYY format}
Example /development-unit/01-05-2023
```
