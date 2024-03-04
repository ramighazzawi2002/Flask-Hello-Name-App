# Hello Name Flask Application

This is a simple Flask application that takes a user's name as input and returns a greeting with the name.

## Files

- `flask.py`: This is the main Flask application file. It defines a single route `/test` that accepts POST requests. The route handler reads the 'Name' field from the form data, passes it to a function from `main.py`, and returns the result.

- `main.py`: This file contains a function `add_hello_before_name(name)` that takes a name as input and returns a string "Hello " followed by the name.

- `index.html`: This is the HTML file for the front-end of the application. It contains a form that sends a POST request to the `/test` route on the Flask application.

## Running the Application

1. Ensure you have Python and Flask installed on your system.
2. Run the Flask application with the command `python flask.py`.
3. Open a web browser and navigate to `http://127.0.0.1:5000/test` to see the application in action.

## Contributing

Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

## License

MIT
