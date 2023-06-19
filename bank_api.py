from flask import Flask, jsonify, request

app = Flask(__name__)


users = []
transactions = []


@app.route('/api/users/', methods=['GET'])
def get_all_users():
    return jsonify(users)


@app.route('/api/users/<username>/', methods=['GET'])
def get_user(username):
    for user in users:
        if user['username'] == username:
            return jsonify(user)
    return jsonify({'message': 'User not found'})


@app.route('/api/users/', methods=['POST'])
def create_user():
    data = request.get_json()
    username = data['username']
    password = data['password']
    email = data['email']
    balance = data['balance']

    
    for user in users:
        if user['username'] == username:
            return jsonify({'message': 'Username already exists'})

    user = {
        'username': username,
        'password': password,
        'email': email,
        'balance': balance
    }
    users.append(user)
    return jsonify({'message': 'User created successfully'})


@app.route('/api/users/', methods=['DELETE'])
def delete_all_users():
    users.clear()
    return jsonify({'message': 'All users deleted successfully'})


@app.route('/api/users/<username>/', methods=['DELETE'])
def delete_user(username):
    for user in users:
        if user['username'] == username:
            users.remove(user)
            return jsonify({'message': 'User deleted successfully'})
    return jsonify({'message': 'User not found'})


@app.route('/api/users/<username>/', methods=['PUT'])
def update_user(username):
    for user in users:
        if user['username'] == username:
            data = request.get_json()
            user['password'] = data['password']
            user['email'] = data['email']
            user['balance'] = data['balance']
            return jsonify({'message': 'User updated successfully'})
    return jsonify({'message': 'User not found'})


@app.route('/api/transactions/', methods=['GET'])
def get_all_transactions():
    return jsonify(transactions)


@app.route('/api/transactions/<transaction_id>/', methods=['GET'])
def get_transaction(transaction_id):
    for transaction in transactions:
        if transaction['transaction_id'] == transaction_id:
            return jsonify(transaction)
    return jsonify({'message': 'Transaction not found'})


@app.route('/api/transactions/', methods=['POST'])
def create_transaction():
    data = request.get_json()
    from_username = data['from_username']
    to_username = data['to_username']
    amount = data['amount']

    
    from_user = None
    to_user = None
    for user in users:
        if user['username'] == from_username:
            from_user = user
        elif user['username'] == to_username:
            to_user = user
    if from_user is None or to_user is None:
        return jsonify({'message': 'Invalid users'})

    
    if from_user['balance'] < amount:
        return jsonify({'message': 'Insufficient balance'})

    
    from_user['balance'] -= amount
    to_user['balance'] += amount

    transaction = {
        'from_username': from_username,
        'to_username': to_username,
        'transaction_id': len(transactions) + 1,
        'amount': amount
    }
    transactions.append(transaction)
    return jsonify({'message': 'Transaction created successfully'})

if __name__ == '__main__':
    app.run(debug=True)


