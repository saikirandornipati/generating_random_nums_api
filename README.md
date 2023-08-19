

# Generating_random_nums_api**


Brief description of your application.

## Table of Contents
- [Getting Started](#getting-started)
  - [Prerequisites](#prerequisites)
  - [Installation](#installation)
- [Running the App](#running-the-app)
  - [FastAPI](#fastapi)
  - [Flask](#flask)
- [API Endpoint](#api-endpoint)
- [Testing](#testing)

## Getting Started

### Prerequisites

List the prerequisites that users need to have installed on their system before they can run your app. For example:

- Python 3.x
- pip3

To install pip:
python3 get-pip.py


Include instructions or links to installation guides for these prerequisites.

### Installation

Provide step-by-step instructions on how to install your application. This might include:

1. Cloning the repository:
   ```bash
   git clone https://github.com/saikirandornipati/generating_random_nums_api.git
   ```

2. Navigating to the project directory:
   ```bash
   cd generating_random_nums_api
   ```

3. Installing dependencies:
   ```bash
   pip install -r requirements.txt
   ```

## Running the App

Explain how to run your application using both FastAPI and Flask. Include separate sections for each framework.

### FastAPI

1. Navigate to the `app` directory:
   ```bash
   cd fastapi_api_app_random_numbers
   ```

2. Run the FastAPI app using Uvicorn:
   ```bash
   python3 -m uvicorn main:app --host 0.0.0.0 --port 8000
   ```

The app should now be running at `http://127.0.0.1:8000`.

### Flask

1. Navigate to the `app` directory:
   ```bash
   cd app
   ```

2. Run the Flask app:
   ```bash
   flask run
   ```

The app should now be running at `http://127.0.0.1:5000`.

## API Endpoint

Explain the API endpoint that your app provides and how users can interact with it. Include sample request and response data.

## Testing

Explain how to run the tests for your app. Include instructions for running test files using `pytest` or any other testing framework.


---

By providing detailed instructions and explanations in your README.md file, you can make it easier for users to set up and run your FastAPI or Flask app and ensure a smoother onboarding experience for them.
