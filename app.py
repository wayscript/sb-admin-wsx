import os

from flask import Flask, render_template, request

# App Logic
app = Flask(__name__)

# DATABASE OPTIONS GO HERE
# this list supplies the options that are generated in the home page selector
# to add or remove entries from home page selector, put them in the list SELECTOR_OPTIONS below

SELECTOR_OPTIONS = ['database_1', 'database_2', 'database_3']

@app.route('/')
def index():
    return render_template('index.html', selector_options = SELECTOR_OPTIONS )

@app.route('/404')
def not_found():
    return render_template('404.html')

@app.route('/charts')
def charts():
    return render_template('charts.html')

@app.route('/tables')
def tables():
    return render_template('tables.html')

@app.route('/submit_form', methods=['GET', 'POST'])
def submit_form():
    database_name = request.form.get('database_selection')
    # HERE YOUR ACTION CAN BE DONE TO YOUR DATABASE
    # we can access the database name from our form by database_name variable
    # We can connect to our database via python library, example:
    # connection = mysql.connector.connect(
    #        host=host_name,
    #        user=user_name,
    #        passwd=user_password,
    #        database=database_name
    #    )
    # select_users = "SELECT * from users"
    # connection.autocommit = True
    # cursor = connection.cursor()
    # try:
    #    cursor.execute(query)
    #    result = 'Success!'
    # except OperationalError as e:
    #    result = 'Operation Failure'
    result = 'Success!'
    return render_template('submit_form.html', selected_database = database_name, result = result)

@app.route('/example')
def example_sb_admin_home():
    return render_template('example.html')

if __name__ == '__main__':
    app.run()
