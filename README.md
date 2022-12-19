
# Technical test - Wonder Travel ✈️🌊🌴

The solution of the Technical test made with 💚 by [Anfercode
](https://github.com/Anfercode)


![Logo](https://wondertravel.co/wp-content/uploads/2021/11/logo-main.png)



# Dependencies.

- Docker version 20.10.17 🐋
- make :computer: (optional: there is a section to execute the project without make)

## Run Locally

Clone the project

```bash
  git clone https://github.com/Anfercode/wonder-technical-test
```

Go to the project directory

```bash
  cd wonder-technical-test
```

Start the server

```bash
  make start
```

Start the server (without make)

```bash
  docker-compose up -d --build
```

## Retrive all commands from make

```bash
  make help
```

## Running Tests

To run tests, run the following command

```bash
  make test
```

To run tests, run the following command (Without make)

```bash
  docker-compose exec web pytest .
```

## Enter the service shell

To enter the shell, run the following command
```bash
  make shell
```

To enter the shell, run the following command (Without make)
```bash
  docker-compose exec web sh
```

## Restart the server
To restart the server, run the following command

```bash
  make restart
```

To restart the server, run the following command (Without make)

```bash
  docker-compose restart
```

## API Reference

The base url will be running in http://localhost:8000

### API Endpoints
| HTTP Verbs | Endpoints | Action |
| --- | --- | --- |
| GET | /health_check | the health check of the service|
| POST | /location | The post of the all antenna information |
| POST | /location_by_parts/{name} | The post of the antenna information |
| GET | /location_by_parts/{name} | To retrieve the antenna information |
| GET | /get_user_location | To retrieve the coordinates and the message of the user |

To run the endpoints service the swagger service is in the following link `http://localhost:8000/docs`

