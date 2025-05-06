# URL Shortener

A simple URL shortener built using Python 3 and Flask. This app allows users to shorten long URLs and redirect to them using short URLs.

## Features

- Shorten a long URL into a short and unique URL.
- Redirect from a short URL to the original long URL.
- Flask-based web application.

## Installation

### Prerequisites

Ensure that you have the following installed on your system:

- Python 3.x
- pip3 (Python package manager)

### Steps to Install

1. Clone this repository:

   ```bash
   git clone https://github.com/your-username/url-shortener.git
   cd url-shortener
   ```

2. Create a virtual environment:

   ```bash
   python3 -m venv venv
   ```

3. Activate the virtual environment:

   - On Windows:
     ```bash
     .\venv\Scripts\activate
     ```
   - On macOS/Linux:
     ```bash
     source venv/bin/activate
     ```

4. Install the required dependencies:

   ```bash
   pip3 install -r requirements.txt
   ```

5. Run the Flask application:

   ```bash
   python3 app.py
   ```

6. Open your web browser and go to `http://127.0.0.1:5000/` to use the URL shortener.

## Usage

1. Visit the homepage at `http://127.0.0.1:5000/`.
2. Enter a long URL in the input field.
3. Click on the "Shorten URL" button to get a shortened version of the URL.
4. Use the generated short URL to redirect to the original long URL.

## How It Works

1. User enters a long URL.
2. The backend generates a unique short URL (hash/ID) for the provided long URL.
3. The short URL is saved and returned to the user.
4. When a user visits the short URL, the backend looks up the original long URL and redirects the user.

## Technologies Used

- Python 3.x
- Flask
- HTML, CSS for frontend

## Contributing

Feel free to fork this repository and submit a pull request if you'd like to contribute improvements!

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
