# Flashcard API
A REST API for a flashcard application built with Django REST Framework. Users can create and manage flashcard decks, add flashcards, track individual learning progress, review cards using a spaced-repetition system, and analyze their learning activity.

The API also supports public/shared decks, bookmarks, tags, deck search and filtering, and deck-level learning statistics. Learning progress is user-specific, allowing each user to maintain their own review history and spaced-repetition schedule for flashcards.

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
## Current Features
* User registration and login
* Token-based authentication
* User-owned flashcard decks
* Create, read, update, and delete decks
* Create and manage flashcards within decks
* Access control for decks and flashcards
* Staff users can access all decks and flashcards
* Public/shared flashcard decks
* User-specific learning progress
* Track flashcard learning progress and review history
* Review flashcards using ratings
* Spaced-repetition scheduling using the SM-2 algorithm
* Retrieve flashcards that are due for review
* Retrieve review history for flashcards
* Deck statistics and learning analytics
* Statistics for total, started, new, and due flashcards
* Statistics for reviews and cards reviewed today
* Average ease-factor and last-review information
* Tags for organizing decks
* Create, update, delete, and manage tags
* Add tags to decks
* Search public decks by title
* Filter public decks by one or multiple tags
* Combine deck title search with multiple tag filters
* Case-insensitive deck searching
* Bookmark public decks
* Retrieve a user's bookmarked decks
* Add and remove deck bookmarks
* API endpoints for authentication, decks, flashcards, learning progress, reviews, bookmarks, statistics, tags, search, and filtering

## Roadmap

Planned features include:

* [X] Public/shared decks
* [X] User-specific learning progress
* [X] Deck statistics and learning analytics
* [X] Tags and deck search/filtering
* [X] Bookmarked decks
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
| `GET`    | `/api/decks/`      | List the user's  decks |
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


### Bookmarks 

| Method | Endpoint                       | Description                            |
| ------ | ------------------------------ | -------------------------------------- |
| `GET` | `/api/decks/bookmarked/` | Get a list of bookmarked decks |
| `POST`  | `/api/decks/<id>/bookmarked/` | Bookmark a deck    |
| `DELETE`  | `/api/flashcards/<id>/review/` | Remove a deck from bookmarked   |

### Statistics
| Method | Endpoint                       | Description                            |
| ------ | ------------------------------ | -------------------------------------- |
| `GET` | `/api/decks/<id>/stats/` | Returns learning statistics for the current user within the specified deck|

Statistic include:
* total, started, new and due flashcards
* total reviews
* reviews and cards reviewed today
* average ease factor
* last review time.

### Tags

| Method  | Endpoint                  | Description                     |
| ------- | ------------------------- | ------------------------------- |
| `GET`   | `/api/tags/`              | List of available tags           |
| `POST`  | `/api/tags/`              | Create a tag                     |
| `GET`   | `/api/tags/<id>/`          | Retrieve an available tag        |
| `PUT`   | `/api/tags/<id>/`          | Update a tag                     |
| `PATCH` | `/api/tags/<id>/`          | Partially update a tag           |
| `DELETE`| `/api/tags/<id>/`          | Delete a tag                     |
| `GET`    | `/api/decks/<id>/tags/`      | List tags in a deck |
| `POST`    | `/api/decks/<deck_id>/tags/<tag_id>`      | Add available tag to a deck |
| `GET`    | `/api/decks/<deck_id>/tags/<tag_id>`      | Remove tag from a deck |

### Deck search and filtering

The public decks endpoint supports searching by deck title and filtering by multiple tags.

| Method | Endpoint | Description |
| ------ | -------- | ----------- |
| GET | `/api/decks/public/` | List all public decks |
| GET | `/api/decks/public/?search=python` | Search decks by title |
| GET | `/api/decks/public/?tag=programming` | Filter decks by tag |
| GET | `/api/decks/public/?tag=programming&tag=python` | Filter decks by multiple tags |
| GET | `/api/decks/public/?search=python&tag=programming&tag=backend` | Search by title and filter by multiple tags |

Multiple tags are combined using **AND** logic. A deck must contain all requested tags to be included in the results.

Search is case-insensitive and matches any part of the deck title.

Example:

`GET /api/decks/public/?search=django&tag=programming&tag=backend`

Returns public decks whose title contains `django` and which have both `Programming` and `Backend` tags.


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
