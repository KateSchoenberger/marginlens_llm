# Overview
Katelyn Schoenberger is a former VP/Quantitative Analyst on the Quantitative Risk Services team at Bank of America. Frequently overwhelmed with the influx of requests related to SIMM from traders, Kate noticed that the harmony between front-office and middle-office functions was asynchronous, meaning traders are under extreme pressure to receive the insights on their data in a quick fashion; contrary to the front-office speed, quants in middle-office facing roles are not usually operating under the same pace or mentality.
Instead, MarginLens allows for traders and other front-office professionals who are non-technical to input their own questions without having to wait for answers to their questions from the busy risk quants. 
As a quant, Kate noticed that her fellow teammates, while highly intelligent, were generating very generic insights on the reports without going into greater analysis on the financial implications or math behind the SIMM calculations, which is very quantitatively involved, time-consuming, and manually processed behind the scenes through the UI system. The reports were also very bulky and lengthy – something many traders don’t have time to skim and account for in great length. Even incorporating pivot tables, charts, and other visual aids was excessive. Traders just want quick answers, so now, with MarginLens, they can directly ask whatever question they desire on their own time. 

# Features

Real-time SIMM Data Analysis: Quickly processes and interprets SIMM data to provide immediate insights.
Enhanced Communication: Facilitates better understanding between front-office and middle-office teams.
Scalable Architecture: Built to handle large datasets efficiently.

# Installation

To set up MarginLens LLM on your local machine:

Clone the repository:

git clone https://github.com/KateSchoenberger/marginlens_llm.git
cd marginlens_llm


Install the required dependencies:

pip install -r requirements.txt


Set up environment variables:

cp .env.example .env
# Edit .env to include your API keys and other configurations


Run the application:

python app/main.py

# Usage

Once the application is running, you can interact with it via the command line or integrate it into your existing systems to analyze SIMM data and receive insights.

# Testing

To run the test suite:

pytest tests/


Ensure all tests pass before deploying to production.

# Contributing

Contributions are welcome! Please fork the repository, create a new branch, and submit a pull request with your proposed changes.

# License

This project is licensed under the MIT License - see the LICENSE file for details.
