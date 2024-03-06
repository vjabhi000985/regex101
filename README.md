# Regex101Clone.com

## Description: 
A web application that facilitates experimenting with regular expressions and matching them against text input. Also, it has the feature to validate the entered email.

## Features
- Accepts regular expression patterns and test strings from users.
- Evaluates matches and displays results.
- Takes an email address and validates whether it is a genuine email id or not.
- (Planned) Handles multiple input strings separated by spaces or newlines.

## Installation
### 1. Clone the repository
```bash
git clone https://github.com/vjabhi000985/regex101.git
```
### 2. Install the required packages
```bash
pip install -r requirements.txt
```
### 3. Run the flask app
```bash
python app.py
```
### 4. Access the application in your web browser, typically at
```http://127.0.0.1:5000/```

## Known Issues:
`Bug`: The test_regex function currently evaluates only one string at a time. A fix is underway to enable handling multiple input strings.

## Contributing:
- Fork this repository.
- Create a branch for your modifications.
- Ensure adherence to PEP 8 style guidelines.
- Include comprehensive tests for new features or bug fixes.
- Submit a pull request describing your changes.

## Credits
Developed by *Pandey Abhishek Nath Roy [me]*
