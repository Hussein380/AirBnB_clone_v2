# AirBnB Clone with Flask

This project is an implementation of an AirBnB clone using Flask, a Python web framework. It aims to replicate some of the functionalities of the AirBnB platform, such as listing properties, searching for accommodations, and user interactions.

## Table of Contents

- [Introduction](#introduction)
- [Features](#features)
- [Installation](#installation)
- [Usage](#usage)
- [Project Structure](#project-structure)
- [Contributing](#contributing)
- [License](#license)

## Introduction

AirBnB Clone with Flask is a web application built with Python and Flask framework. It provides a platform for users to list their properties for rent and for others to search and book accommodations. The application implements various routes and functionalities to achieve this, such as displaying listings, handling user authentication, and managing property bookings.

## Features

- **User Authentication**: Users can create accounts, log in, and log out.
- **Property Listings**: Users can list their properties with details such as description, price, and location.
- **Search and Filter**: Users can search for properties based on location, price range, and other criteria.
- **Booking Management**: Users can book properties and manage their bookings.
- **Admin Panel**: Admins have access to an admin panel to manage users, properties, and bookings.

## Installation

To run the AirBnB Clone with Flask locally, follow these steps:

1. Clone the repository:

    ```bash
    git clone https://github.com/your_username/AirBnB_clone_v2.git
    ```

2. Navigate to the project directory:

    ```bash
    cd AirBnB_clone_v2
    ```

3. Install the required dependencies:

    ```bash
    pip install -r requirements.txt
    ```

4. Set up the Flask environment variables:

    ```bash
    export FLASK_APP=web_flask/__init__.py
    export FLASK_ENV=development
    ```

5. Run the Flask application:

    ```bash
    flask run
    ```

The application should now be running locally at `http://127.0.0.1:5000`.

## Usage

Once the application is running, you can access it through a web browser. Here are some of the available routes:

- `/`: Home page with a welcome message.
- `/hbnb`: Displays "HBNB".
- `/c/<text>`: Displays "C <text>".
- `/python/<text>`: Displays "Python <text>".
- `/number_template/<n>`: Displays an HTML page with "Number: n".
- `/number_odd_or_even/<n>`: Displays an HTML page with "Number: n is even|odd".

## Project Structure

The project follows a standard Flask application structure:

- `web_flask/`: Contains the Flask application code.
- `models/`: Includes the data models and storage classes.
- `templates/`: Contains HTML templates for rendering pages.
- `static/`: Includes static files such as CSS and JavaScript.
- `tests/`: Includes unit tests for the application.

## Contributing

Contributions to the AirBnB Clone with Flask project are welcome! If you find any bugs or have suggestions for improvements, please open an issue or submit a pull request.


