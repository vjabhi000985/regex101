from flask import Flask, render_template, request, session, redirect, url_for
import re

app = Flask(__name__)
app.secret_key = 'hSJ1GbYwHqmB-HkxLyzc8l37A5FlXTCU-WM8mGZSPsA'

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/test_regex', methods=['POST'])
def test_regex():
    try:
        regex_exp = request.form['regex_exp']
        test_string = request.form['test_string']

        lines = test_string.splitlines()
        matched_results = []

        for line in lines:
            matches = re.findall(regex_exp, line)
            if matches:
                joined_matches = ', '.join(matches)
                matched_results.append(joined_matches)

        session['regex_results'] = matched_results
        return render_template('regex_result.html', session=session)
    except re.error as e:
        session['regex_error'] = str(e)
        return render_template('index.html')


@app.route('/validate_email', methods=['POST'])
def validate_email():
    email_id = request.form['email_id']
    email_regex = r"^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$"

    if re.match(email_regex, email_id):
        session['email_valid'] = True
    else:
        session['email_valid'] = False

    print(session)    
    
    return render_template('email_result.html')

@app.route('/regex_result')
def regex_result():
    if 'regex_results' in session:
        matches = session.pop('regex_results')
        return render_template('regex_result.html', matches=matches)
    elif 'regex_error' in session:
        error_message = session.pop('regex_error')
        return render_template('regex_result.html', error=error_message)
    else:
        return redirect(url_for('index'))

@app.route('/email_result')
def email_result():
    if 'email_valid' in session:
        email_valid = session.pop('email_valid')
        return render_template('email_result.html', email_valid=email_valid)
    else:
        return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True)