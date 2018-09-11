# Store Reviews Service

This project is a Restfull Application built using Django which contains data related to Stores, their Reviews, Product details and their availability in the Stores.

## DB Design

### Table Name: Store

| Field          | Type         | Null     | Key         | Default | Extra |
|----------------|--------------|----------|-------------|---------|-------|
| store_id       | integer      | NOT NULL | Primary Key |         |       |
| store_name     | varchar(200) | NOT NULL |             |         |       |
| store_owner    | varchar(200) |          |             |         |       |
| location       | text         |          |             |         |       |
| established_on | Date Time    | NULL     |             |         |       |
| gst_in         | varchar(200) |          |             |         |       |


###Table Name: Reviews

| Field      | Type    | Null     | Key                | Default | Extra |
|------------|---------|----------|--------------------|---------|-------|
| review_id  | integer | NOT NULL | Primary Key        |         |       |
| store_id   | integer | NOT NULL | Foreign Key(Store) |         |       |
| review     | text    |          |                    |         |       |
| stars      | integer |          |                    |         |       |
| created_at |         |          |                    | NOW     |       |
| updated_at |         |          |                    | NOW     |       |

### Table Name: Entities

| Field       | Type         | Null     | Key         | Default | Extra |
|-------------|--------------|----------|-------------|---------|-------|
| entity_id   | integer      | NOT NULL | Primary Key |         |       |
| entity_name | varchar(200) |          |             |         |       |
| price       | Float        |          |             |         |       |
| created_at  |              |          |             | NOW     |       |
| updated_at  |              |          |             | NOW     |       |

### Table Name: Inventories

| Field        | Type    | Null     | Key                   | Default | Extra |
|--------------|---------|----------|-----------------------|---------|-------|
| inventory_id | integer | NOT NULL | Primary Key           |         |       |
| store_id     | integer | NOT NULL | Foreign Key(Store)    |         |       |
| entity_id    | integer | NOT NULL | Foreign Key(Entities) |         |       |
| count        | integer |          |                       |         |       |
| created_at   |         |          |                       | NOW     |       |
| updated_at   |         |          |                       | NOW     |       |

## Instructions to Build and Run

### Requirements:-
- Python 3+
- pip

### Instructions:-
1. git clone http://gitlab.networthcorp.net/prince0909/store-django-project.git
2. cd  store-django-project
3. pip install -r 
4. python manage.py migrate
5. python manage.py runserver

This starts the application on port `8000`.

You can go to `http://localhost:8000` on your browser to see the home page. 

## API Documentation:-

you can refer to [Postman Collection here](https://www.getpostman.com/collections/2c6e7f6268f2c62b6ea4).
