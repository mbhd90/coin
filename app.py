from flask import Flask, jsonify
from block import Blockchain

app = Flask(__name__)
blockchain = Blockchain()

# Create new Block and return new block in json format

@app.route('/mine', methods=['POST'])
def mine_block():
    previous_block = blockchain.print_previous_block()
    previous_proof = previous_block['proof']
    proof = blockchain.proof_of_work(previous_proof)
    previous_hash = blockchain.hash(previous_block)
    block = blockchain.create_block(proof, previous_hash)

    response = {'message': 'A block is MINED',
                'index': block['index'],
                'timestamp': block['timestamp'],
                'proof': block['proof'],
                'previous_hash': block['previous_hash']}

    return jsonify(response), 200

# Display blockchain in json format


@app.route('/get', methods=['GET'])
def display_chain():
    response = {'chain': blockchain.chain,
                'length': len(blockchain.chain)}
    return jsonify(response), 200

# Check validity of blockchain

@app.route('/valid', methods=['GET'])
def valid():
    valid = blockchain.chain_valid(blockchain.chain)

    if valid:
        response = {'message': 'The Blockchain is valid.'}
        return jsonify(response), 200
    else:
        response = {'message': 'The Blockchain is not valid.'}
        return jsonify(response), 422

app.run(host='127.0.0.1', port=5000)