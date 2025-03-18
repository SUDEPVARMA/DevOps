from flask import Flask, request, render_template

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def home():
    print('Home page accessed')
    return "Welcome to the Home Page!"  # Added return statement

@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        name = request.form.get('name', '')
        email = request.form.get('email', '')
        password = request.form.get('password', '')


        return render_template('success.html', name=name)
    
    return render_template('register.html')

if __name__ == '__main__':
    print("Starting Flask application...")  # Added print statement for clarity
    app.run(debug=True)
