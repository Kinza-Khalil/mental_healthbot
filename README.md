Project: Mental Healthbot
==========================

The Mental Health Chatbot is a conversational AI application designed to provide information, resources, and support related to mental health issues. The chatbot is built using Rasa and ChatGPT by OpenAI.


Code Implementation
=====================
Rasa project setup: The initial Rasa project was set up using the rasa init command.
Domain configuration: The domain.yml file was configured with intents, entities, slots, and responses.
Training data: Training data for the NLU model was added in the nlu.yml file, and stories for the conversation flow were added in the stories.yml file.
Custom actions: Custom actions were implemented using Python and the Rasa SDK in the actions.py file.
ChatGPT integration: The OpenAI API was integrated into the Rasa action server to generate responses using ChatGPT.
Configuration settings: The config.yml file was updated with pipeline and policy settings, as well as threshold values for intent classification.

APIs and Libraries
====================
Rasa: The main framework used for building the chatbot.
OpenAI API: Used to integrate ChatGPT into the custom actions.
Requests library: Used for making API calls to the OpenAI API.
dotenv: Used for managing API keys and other sensitive information.

Challenges and Learnings
=========================
Ensuring that the domain.yml file is correctly formatted and contains all necessary information.
Configuring the NLU pipeline and policy settings in the config.yml file for optimal performance.
Understanding how to effectively integrate the ChatGPT API into the Rasa action server.
Learning how to handle edge cases and fallback scenarios to provide a smooth user experience.


Getting Started
-----------------

Prerequisites
----------------
Python 3.8 or higher
Rasa 2.8.9 or higher
dotenv for Python
An API key for the integrated service

Installation
---------------
1- Clone the repository:
   git clone https://github.com/Kinza_Khalil/Healthnbot.git
   
2- Navigate to the project directory:
   cd Healthbot
   
3- Create a virtual environment: Open a terminal/command prompt and navigate to your Rasa project directory.Then, run the following commands
   python -m venv venv
   
4- Activate the virtual environment:
On Windows:
    .\venv\Scripts\activate
On macOS and Linux:
    source venv/bin/activate
    
5- Install the required packages:
    pip install -r requirements.txt
    
6- Train the Rasa model:
    rasa train

API Key Instructions
---------------------
To properly set up and use an API key in this project, follow these instructions:

1- Sign up or log in: Visit the API provider's website and create an account or log in to your existing account.

2- Request an API key: Once logged in, navigate to the API section and request an API key. The process may vary depending on the API provider. Make sure to read their documentation on how to obtain an API key.

3- Add the API key to the .env file: Open the .env file and add the API key as an environment variable. The format should be:
API_KEY=your_api_key_here

Replace your_api_key_here with the actual API key you obtained from the API provider.

4- Install required libraries: Make sure you have installed all the required libraries, including python-dotenv. You can install it using the following command:
pip install python-dotenv

5- Load the API key in your code: The provided Python code already includes the necessary lines to load the environment variables from the .env file. Ensure that your .env file is properly set up and contains the correct API key.
    
Usage
--------
1- To Start the Rasa server:
    rasa run
    
2- In a separate terminal, start the Rasa action server:
    rasa run actions
    
3- Run the Rasa server: In another terminal window, start the Rasa server using the following command:
    rasa run -m models --enable-api --cors "*"
    
4- Start the web app: Navigate to the webapp directory and start the web app using the following command:
    python app.py
    
5- Access the chatbot: After starting the web app, open your web browser and navigate to http://localhost:5000 or the link provided in the terminal window. You should see the chatbot interface, where you can start interacting with the Mental Health Chatbot.
Remember to keep all terminal windows (Rasa action server, Rasa server, and web app server) running while interacting with the chatbot.
    
How to Run and Interact with the Chatbot
To run the chatbot, follow the steps provided in the Usage section. To interact with the chatbot, use Rasa's built-in shell and type your messages as prompted. The chatbot will respond with relevant information, resources, or further questions to understand your query better.
