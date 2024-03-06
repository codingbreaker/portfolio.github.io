
1. Run the Flask application:

2. Open a web browser and go to `http://127.0.0.1:5000/` to access the home page.

3. Navigate through different pages using the navigation links provided.

4. To submit a form, go to the "Contact" page and fill out the form. Upon submission, the data will be written to a CSV file named `db.csv`.

## Project Structure

- `app.py`: This file contains the main Flask application code, including route definitions and form submission logic.
- `templates/`: This directory contains HTML templates for different pages served by the application, which are rendered using Jinja2.
- `static/`: This directory contains static assets such as CSS and JavaScript files used for styling and client-side interactions.
- `db.csv`: This is the CSV file where form data is stored.

## Routes

- `/`: Home page
- `/about`: About page
- `/education`: Education page
- `/skill`: Skill page
- `/contact`: Contact page

## Front-end Technologies Used

- HTML: HyperText Markup Language is used for structuring web pages.
- CSS: Cascading Style Sheets are used for styling the HTML elements and defining their appearance.
- JavaScript: Used for client-side interactions and form validation.
- Jinja2: A templating engine for Python, used to dynamically render HTML templates with data from the server.

## Dependencies

- Flask: A micro web framework for Python.

## Credits

This application was developed by Pawan.
