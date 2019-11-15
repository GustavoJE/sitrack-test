# sitrack-test

An API for creating alphabet soups written in Python

---

## Summary

An API that creates a word soup with a random generated horizontal word (left to right) and a random generated vertical word (top to botton).
The API also returns said word soup and the list of words to find

## Requirements

The following packages are required by sitrack-test

| Package Name | URL                                                           | Minimum required version |
|--------------|---------------------------------------------------------------|--------------------------|
| Python       | https://www.python.org/downloads/                             | `3.7`                    |
| git          | https://git-scm.com/book/en/v2/Getting-Started-Installing-Git | `latest`                 |
| pip          | https://pip.pypa.io/en/stable/installing/                     | `19.2.3`                 |
| mongodb      | https://docs.mongodb.com/manual/installation/                 | `3.9.0  `                |

## Directory structure

```bash
$ tree
├── config
├── helpers
├── app.py
└── README.md
```

| Dirname | Description                                                         |
|---------|---------------------------------------------------------------------|
| config  | This directory contains `application` and `database` configurations |
| helpers | This directory contains helpers function for creating the word soup |


## Installation

1. Checkout the repo
```bash
$ git clone git@github.com:GustavoJE/sitrack-test.git
```

2. Install the dependencies
```bash
$ pip install -r requirements.txt
```

3. Run the application
```bash
$ python app.py
```

### Available environment configuration variables

| Name             | Description                         | Default Value                            | Required |
|------------------|-------------------------------------|------------------------------------------|----------|
| **Database**     |                                     |                                          |          |
| MONGO_HOST       | The hostname of the mongodb         | `mongodb://admin:admin@localhost:27017/` | **yes**  |
| MONGO_DATABASE   | The name of the mongo's database    | `sitrack`                                | no       |
| MONGO_COLLECTION | The name of the mongo's collection  | `sitrackexam`                            | no       |
| **Application**  |                                     |                                          |          | 
| APP_PORT         | The port of the application         | `8000`                                   | no       |
| APP_DEBUG        | Enables hot reloading for debugging | `False`                                  | no       |


## Documentation

For documenting the API, I used Swagger functionality that comes built in `flask_restplus` framework. In order to create and present the `swagger.json` file, please Run the API and visit the endpoint `http://HOST:{PORT}/`. You should see the documentation of the API's endpoints

## Known issues

https://github.com/vaibhavsingh97/random-word/issues/16
