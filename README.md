# Twilio API Rain Alert App

This project is a rain alert application that uses the Twilio API to send SMS alerts about rain forecasts to your phone. By leveraging weather data, the app proactively notifies you to bring an umbrella if rain is predicted in your area, ensuring you're prepared for the day's weather.

## Features

- Uses OpenWeatherMap API to fetch weather forecasts.
- Sends SMS alerts through Twilio API if rain is predicted.
- Can be customized to monitor specific locations.

## Prerequisites

Before you begin, ensure you have the following:

- Python 3.x installed on your system.
- A Twilio account and a Twilio phone number capable of sending SMS messages.
- An OpenWeatherMap API key.

## Installation

1. **Clone the Repository**

   Start by cloning the repository to your local machine:

   ```bash
   git clone https://github.com/matusoff/Twilio_API_rain_alert_app.git
   cd Twilio_API_rain_alert_app

## Set Up a Virtual Environment (Optional)
```bash
  python -m venv venv
  source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
```

## Configuration
Before running the app, you need to configure a few settings:

## Environment Variables

Set up the following environment variables in your system or define them in a .env file in the project root:

- TWILIO_ACCOUNT_SID: Your Twilio Account SID.
- TWILIO_AUTH_TOKEN: Your Twilio Auth Token.
- TWILIO_PHONE_NUMBER: The Twilio phone number that will send the alerts.
- MY_PHONE_NUMBER: The phone number that will receive the alerts.
- OPENWEATHER_API_KEY: Your OpenWeatherMap API key.
-LATITUDE  and LONGITUDE: The coordinates of the location you want to monitor.

## Usage
To run the rain alert app, execute the main.py script:

```bash
python main.py
```

## Credits
This project makes use of the following APIs:

- Twilio API for sending SMS messages. Special thanks to Twilio for providing a robust and easy-to-use API for communications.
- OpenWeatherMap API for weather data and forecasts.

## Contributing
Contributions to the Twilio API Rain Alert App are welcome! Feel free to fork the repository, make your changes, and submit a pull request.
