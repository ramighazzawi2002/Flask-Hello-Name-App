from flask import Flask, request
from main import add_hello_before_name
app = Flask(__name__)

@app.route('/test', methods=['POST'])
def test():
    user_input = request.form.get('Name')
    return add_hello_before_name(user_input)

if __name__ == '__main__':
    app.run(port=5000)
    