from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

@app.route('/')
def home():
    return redirect(url_for('signup'))

@app.route('/signup', methods=['GET', 'POST'])
def signup():
    if request.method == 'POST':
        username = request.form['username']
        email = request.form['email']
        password = request.form['password']
        # Here you would typically save the user data to a database
        return redirect(url_for('data'))  # Redirect to a data page after sign up
    return render_template('signup.html')

@app.route('/data')
def data():
    # Placeholder for user data
    users = []  # Replace with actual user data retrieval
    return render_template('data.html', users=users)

if __name__ == '__main__':
    app.run(debug=True)
