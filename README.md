# MyDiary

MyDiary is an online journal where users can pen down their thoughts and feelings.

## Getting Started

These instructions will get you a copy of the project up and running on your local machine for development and testing purposes. See deployment for notes on how to deploy the project on a live system.

### Prerequisites

* Git
* Python 3.6.4
* Virtualenv

### Quick Start

1. Clone the repository

```
$ git clone https://github.com/Peteromuya/My_Diary
$ cd into the created folder
```
  
2. Initialize and activate a virtualenv

```
$ virtualenv --no-site-packages env
$ source env/bin/activate
```

3. Install the dependencies

```
$ pip install -r requirements.txt
```

4. Run the development server

```
$ python app.py
```

5. Navigate to [http://localhost:5000](http://localhost:5000)

At the / endpoint you should see 'Welcome to MyDiary' API displayed in your browser.

## Endpoints

Here is a list of all endpoints in MyDiary API

Endpoint | Functionality 
------------ | -------------
POST   /api/v1/auth/signup | Register a user
POST   /api/v1/auth/login | Log in user
POST   /api/v1/users | Register a user
GET    /api/v1/users | Get all users
GET   /api/v1/users/id | Get a single user
PUT  /api/v1/users/id | Update a single user
DELETE   /api/v1/users/id | Delete a single user
POST   /api/v1/entries | Create new entry 
GET   /api/v1/entries | Get all entries
GET   /api/v1/entries/id | Get a single entry
PUT   /api/v1/entries/id | Update a single entry
DELETE   /api/v1/entries/id | Delete a single entry

## Running the tests

To run the automated tests simply run

```
coverage run -m unittest

pytest

```

## And coding style tests

Coding styles tests are tests that ensure conformity to coding style guides. In our case, they test conformity to
PEP 8 style guides

```
pylint app.py
```

## Deployment

Ensure you use Productionconfig settings which have DEBUG set to False

## Built With

* Python 3.6.4
* Flask - The web framework used

## GitHub pages

https://github.com/Peteromuya/Peteromuya.github.io

## Versioning

Most recent version is version 1

## Author

Peter Omuya

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details

## Acknowledgements

* Hat tip to anyone who's code was used
* Inspiration and encouragement
* etc
