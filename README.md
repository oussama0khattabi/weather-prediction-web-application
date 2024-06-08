# Weather Prediction Web Application

This repository contains the code and resources for a weather prediction web application. The model is trained on the Rabat weather dataset to predict rain and temperature. The application is built with Flask and containerized using Docker.

## Features

- **Weather Prediction**: Predicts rain and temperature based on historical weather data from Rabat.
- **Web Interface**: User-friendly interface built with Flask.
- **Dockerized**: Containerized application for easy deployment.

## Technologies Used

- **Flask**: Web framework for building the web application.
- **Docker**: Containerization platform for packaging the application.
- **Machine Learning**: Model trained on Rabat weather dataset for prediction.

## Prerequisites

Before running the application, ensure you have the following installed:

- Python 3.8+
- Docker

## Installation

1. **Clone the Repository**:

    ```bash
    git clone https://github.com/oussama0khattabi/weather-prediction-web-application.git
    cd weather-prediction-web-application
    ```

2. **Build and Run with Docker**:

    - Build the Docker image:

        ```bash
        docker compose up --build .
        ```


3. **Access the Application**:

    Open your web browser and navigate to `http://localhost:5000` to access the weather prediction application.

## Project Structure

- `app.py`: Main Flask application file.
- `rain classification.ipynb`: Script for loading and using the rain prediction model.
- `temp regression.ipynb`: Script for loading and using the temperature prediction model.
- `Dockerfile`: Docker configuration file.
- `requirements.txt`: List of Python dependencies.


