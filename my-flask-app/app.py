from flask import Flask, render_template, request

app = Flask(__name__)

# Home route
@app.route('/')
def home():
    return render_template('index.html')

# Greet route
@app.route('/greet', methods=['POST'])
def greet():
    name = request.form.get('name')
    if name:
        return f'<h1>Hello, {name}!</h1>'
    else:
        return '<h1>Please enter your name!</h1>'

if __name__ == '__main__':
    app.run(debug=True)
