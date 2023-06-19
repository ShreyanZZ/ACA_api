# ACA_api

| Endpoint                                  | Method | Description                                           |
|-------------------------------------------|--------|-------------------------------------------------------|
| /api/users/                               | GET    | Retrieve all registered users                         |
| /api/users/{username}/                     | GET    | Retrieve a registered user by primary key (username)  |
| /api/users/                               | POST   | Register a new user                                   |
| /api/users/                               | DELETE | Delete all users                                      |
| /api/users/{username}/                     | DELETE | Delete a user by primary key (username)               |
| /api/users/{username}/                     | PUT    | Update user details for a given user                  |
| /api/transactions/                        | GET    | Retrieve all transactions                             |
| /api/transactions/{transaction_id}/         | GET    | Retrieve a particular transaction by transaction ID    |
| /api/transactions/                        | POST   | Create a new transaction                              |
