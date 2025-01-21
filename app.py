from flask import Flask, request, render_template, redirect, url_for

app = Flask(__name__)

# In-memory storage
data_store = {}

# Route for the form
@app.route('/')
def index():
    return render_template('form.html')

# Route to handle form submission
@app.route('/submit', methods=['POST'])
def submit_form():
    name = request.form.get('name')
    email = request.form.get('email')

    # Save to the in-memory storage
    data_store[email] = {'name': name, 'email': email}

    return redirect(url_for('show_data'))

# Route to display the stored data
@app.route('/data')
def show_data():
    return render_template('data.html', data=data_store)

if __name__ == '__main__':
    app.run(debug=True)