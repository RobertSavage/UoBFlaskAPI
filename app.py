from flask import Flask, request, jsonify
from functools import wraps

app = Flask(__name__)

def require_token(func):
    @wraps(func)
    def decorated(*args, **kwargs):
        token = None
        
        if 'Authorization' in request.headers:
            header = request.headers['Authorization']
            token = header.split(" ")[1]
        
        if not token:
            return jsonify({'message': 'Token is missing.'}), 401
        
        if token != 'eyJhbGciOiJIUzUxMiJ9.eyJSb2xlIjoiQWRtaW4iLCJJc3N1ZXIiOiJJc3N1ZXIiLCJVc2VybmFtZSI6IkphdmFJblVzZSIsImV4cCI6MTY3OTY5NTI2NiwiaWF0IjoxNjc5Njk1MjY2fQ.IBtlGd762-BC38xjLM4WjlBcJUolOmBVikDlmqSw2r6wWFzojy43X_RN51AMJKshUVa9koELbi0qVmAPT3Ch2g':  # replace with your actual token validation code
            return jsonify({'message': 'Invalid token.'}), 401
        
        return func(*args, **kwargs)

    return decorated

@app.route('/api/my-endpoint', methods=['GET'])
@require_token
def my_endpoint():
    return jsonify({'message': 'This endpoint requires a bearer token.'})

if __name__ == '__main__':
    app.run(debug=True)