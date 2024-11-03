from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/github-webhook', methods=['POST'])
def github_webhook():
    # Get the JSON data from the request
    event_data = request.json
    
    # Log the event data
    print("Received GitHub webhook event:")
    print(event_data)

    # Respond to GitHub
    return jsonify({'status': 'success'}), 200

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)

