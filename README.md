Sure, here is a `README.md` file for your `json_input_formatter` Django REST app:

### `README.md`

```markdown
# JSON Input Formatter

JSON Input Formatter is a Django REST application that formats JSON data to a specific string format suitable for use in Postman. The app receives a JSON object via a POST request and returns it formatted as required.

## Features

- Accepts JSON input via POST request
- Formats JSON to a specific string format
- Returns the formatted string

## Requirements

- Python 3.x
- Django 3.x or 4.x
- Django REST framework

## Installation

1. Clone the repository:

   ```bash
   git clone https://github.com/your-username/json_input_formatter.git
   cd json_input_formatter
   ```

2. Create and activate a virtual environment:

   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`
   ```

3. Install the dependencies:

   ```bash
   pip install -r requirements.txt
   ```

4. Apply migrations:

   ```bash
   python manage.py migrate
   ```

5. Run the development server:

   ```bash
   python manage.py runserver
   ```

## Usage

1. Open Postman or any other API testing tool.

2. Send a POST request to `http://127.0.0.1:8000/api/format-json/` with the JSON body you want to format.

   Example:

   ```json
   {
    "data":{
        "sample":"HII"
      }
    }
   ```

3. The response will be the formatted JSON string:

   ```json
   {
    "formatted_data": "{\r\n    \"sample\": \"HII\"\r\n}"
   }
   ```

## Development

### Setting Up the Development Environment

1. Clone the repository:

   ```bash
   git clone https://github.com/your-username/json_input_formatter.git
   cd json_input_formatter
   ```

2. Create and activate a virtual environment:

   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`
   ```

3. Install the dependencies:

   ```bash
   pip install -r requirements.txt
   ```

### Running Tests

To run tests, use the following command:

```bash
python manage.py test
```

## Contributing

1. Fork the repository.
2. Create a new branch: `git checkout -b feature-name`.
3. Make your changes and commit them: `git commit -m 'Add some feature'`.
4. Push to the branch: `git push origin feature-name`.
5. Submit a pull request.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

```

This `README.md` provides an overview of the project, installation instructions, usage examples, and guidelines for development and contribution. Make sure to replace placeholders like `your-username` with your actual GitHub username or the relevant information.