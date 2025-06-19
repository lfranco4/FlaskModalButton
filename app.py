from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/submit', methods=['POST'])
def submit():
    user_input = request.form.get('user_input')
    print(f"Received: {user_input}")  # Handle as needed
    return "Input received", 200

if __name__ == '__main__':
    app.run(debug=True)
