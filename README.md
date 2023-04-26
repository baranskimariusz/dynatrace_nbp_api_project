# NBP API Project

This project focuses on providing endpoints to query data from the NBP's public APIs and return relevant information from them.

## Getting Started

These instructions will guide you on how to set up the project and run it on your local machine.

### Installation

1. Clone the repository:

```
git clone https://github.com/baranskimariusz/dynatrace_nbp_api_project.git
```

2. Change the directory to the project folder:

```
cd dynatrace_nbp_api_project
```

3. (Optional) Create and activate a virtual environment:

- Create a virtual environment:

```
python -m venv venv
```

- Activate the virtual environment:

  - On macOS and Linux:

  ```
  source venv/bin/activate
  ```


4. Install the required Python packages:

```
pip install Flask requests pytest
```

### Running the Application

1. Start the Flask application:

```
python main.py
```

2. Test the application using a web browser, Postman, or `curl`:

- Average exchange rate for a currency on a specific date:

```
http://127.0.0.1:5000/average_exchange_rate/usd/2022-01-10
```

- Min and max average values for a currency in the last x days:

```
http://127.0.0.1:5000/min_max_average/usd/10
```

- Major difference between the buy and ask rate for a currency in the last x days:

```
http://127.0.0.1:5000/major_difference/usd/10
```

### Running the Tests

To run the tests using `pytest` (assuming you actually have a test file named `test_nbp_service.py`):

```
pytest test_nbp_service.py
```

### Deactivating the Virtual Environment

To deactivate the virtual environment (if you used one):

```
deactivate
```

## Built With

- Flask - The web framework used
- Requests - HTTP library for Python
- Brainpower