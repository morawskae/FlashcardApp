# Flashcard API

A REST API for a flashcard application built with Django REST Framework. Users can create decks, add flashcards, track learning progress, and review flashcards using a spaced-repetition system.

## Built With

* Python
* Django
* Django REST Framework
* SQLite
* Token Authentication

## Getting Started

### Prerequisites

Make sure you have:

* Python 3.10+
* Git
* pip

### Installation

1. Clone the repository:

```bash
git clone https://github.com/morawskae/FlashcardApp
cd <project-directory\backend>
```

2. Create a virtual environment:

```bash
python -m venv venv
```

3. Activate the virtual environment.

**Windows:**

```bash
venv\Scripts\activate
```

**macOS/Linux:**

```bash
source venv/bin/activate
```

4. Install the dependencies:

```bash
pip install -r requirements.txt
```

5. Apply database migrations:

```bash
python manage.py migrate
```

6. Start the development server:

```bash
python manage.py runserver
```

The API will be available at:

```text
http://127.0.0.1:8000/api/
```

## Usage

The API uses token authentication.

After registering or logging in, include the returned token in requests to protected endpoints:

```text
Authorization: Token <your-token>
```

For example:

```http
GET /api/decks/
Authorization: Token your-token
```

You can use Postman or another API client to interact with the API.

## Roadmap

Planned features include:

* [ ] Public/shared decks
* [ ] User-specific learning progress
* [ ] Deck statistics and learning analytics
* [ ] Tags and deck search/filtering
* [ ] Favorite/bookmarked decks
* [ ] Review history
* [ ] API tests and improved documentation

## API Description

### Authentication

| Method | Endpoint              | Description                                |
| ------ | --------------------- | ------------------------------------------ |
| `POST` | `/api/auth/register/` | Register a new user                        |
| `POST` | `/api/auth/login/`    | Log in and receive an authentication token |
| `POST` | `/api/auth/logout/`   | Log out and invalidate the current token   |

### Decks

| Method   | Endpoint           | Description                      |
| -------- | ------------------ | -------------------------------- |
| `GET`    | `/api/decks/`      | List the user's accessible decks |
| `POST`   | `/api/decks/`      | Create a new deck                |
| `GET`    | `/api/decks/<id>/` | Retrieve a deck                  |
| `PUT`    | `/api/decks/<id>/` | Update a deck                    |
| `PATCH`  | `/api/decks/<id>/` | Partially update a deck          |
| `DELETE` | `/api/decks/<id>/` | Delete a deck                    |

### Flashcards

| Method   | Endpoint                      | Description                  |
| -------- | ----------------------------- | ---------------------------- |
| `GET`    | `/api/decks/<id>/flashcards/` | List flashcards in a deck    |
| `POST`   | `/api/decks/<id>/flashcards/` | Create a flashcard in a deck |
| `GET`    | `/api/flashcards/<id>/`       | Retrieve a flashcard         |
| `PUT`    | `/api/flashcards/<id>/`       | Update a flashcard           |
| `PATCH`  | `/api/flashcards/<id>/`       | Partially update a flashcard |
| `DELETE` | `/api/flashcards/<id>/`       | Delete a flashcard           |

### Learning Progress

| Method | Endpoint                         | Description                            |
| ------ | -------------------------------- | -------------------------------------- |
| `GET`  | `/api/decks/<id>/flashcards/due` | Get flashcards that are due for review |
| `GET`  | `/api/flashcards/<id>/progress/` | Get progress for a flashcard           |

### Reviews

| Method | Endpoint                       | Description                            |
| ------ | ------------------------------ | -------------------------------------- |
| `POST` | `/api/flashcards/<id>/review/` | Submit a review/rating for a flashcard |
| `GET`  | `/api/flashcards/<id>/review/` | Get review history for a flashcard     |

Most endpoints require authentication using a DRF token.

## Project Structure

```text
backend/
├── flashcard_api/
├── FlashcardProject/
├── manage.py
├── requirements.txt
├── .gitignore
└── README.md
```
