from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__, template_folder='templates')  # Specify the template folder

# List to store user data
users = []

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/signup', methods=['GET', 'POST'])
def signup():
    if request.method == 'POST':
        username = request.form.get('username')
        email = request.form.get('email')
        password = request.form.get('password')
        
        if username is None or email is None or password is None:
            return 'Missing form data', 400
        
        # Save user data to the list
        users.append({'username': username, 'email': email})
        return redirect(url_for('data'))  # Redirect to a data page after sign up
    else:
        return render_template('signup.html')

@app.route('/data')
def data():
    return render_template('data.html', users=users)

if __name__ == '__main__':
    app.run(debug=True)