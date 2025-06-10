
![Logo](/logos.png)


[![MIT License](https://img.shields.io/badge/License-MIT-green.svg)](https://choosealicense.com/licenses/mit/)


# TacleAPI

🕵️TacleAPI - this is a software interface that helps to remotely manage a device. TacleAPI - his is a set of software functions and procedures. In simple terms, it is a program that allows you to remotely control a device.

## API Reference

#### Send own command

```http
  GET /command/{command}
```

| Parameter | Type     | Description                |
| :-------- | :------- | :------------------------- |
| `command` | `string` | **Required**. Your command |

#### Template commands

```http
  GET /shutdown
```

| Parameter | Type     | Description                       |
| :-------- | :------- | :-------------------------------- |
| `shutdown`      | `string` | **Required**. Shutdown host |
| `reboot`      | `string` | **Required**. Reboot host |
| `sleep`      | `string` | **Required**. Sleep host |




## Installation

Install my-project with git, change allow ip pool before start.

```bash
  git clone https://github.com/TheDmitryY/tacle-api
  cd tacle-api/app
  fastapi run app.py
```
    
## Features

- Fast commands
- Full confidence
- Cross platform


## Authors

- [@TheDmitryY](https://www.github.com/TheDmitryY)

## Feedback

If you have any feedback, please reach out to us at telegram: [trusres](https://t.me/trusres)

