from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

# List to store user data
users = []

@app.route('/')
def home():
    return redirect(url_for('signup'))

@app.route('/signup', methods=['GET', 'POST'])
def signup():
    if request.method == 'POST':
        username = request.form['username']
        email = request.form['email']
        password = request.form['password']
        # Save user data to the list
        users.append({'username': username, 'email': email})
        return redirect(url_for('data'))  # Redirect to a data page after sign up
    return render_template('signup.html')

@app.route('/data')
def data():
    return render_template('data.html', users=users)

if __name__ == '__main__':
    app.run(debug=True)
