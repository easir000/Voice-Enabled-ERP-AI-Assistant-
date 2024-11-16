Voice-Based Money Request System
Project Overview
This project implements an AI-powered voice command system for handling money requests, such as budget approvals for projects. The system takes spoken input from users, extracts key details like project numbers, amounts, and purposes, and confirms the request before saving it to a database.

The solution uses speech recognition, OpenAI’s GPT model for understanding commands, and Whisper for speech-to-text transcription. It also integrates a simple validation flow to ensure that all necessary information is provided by the user before submitting a request.

Features
Voice and Text Interaction: Users can interact using voice commands or text inputs.
Field Validation: Ensures required fields like project number and amount are provided.
Confirmation Flow: Asks for user confirmation before submitting a request.
Database Storage: Successfully processed requests are stored in an SQLite database.
Extensible Design: Can be expanded to support additional workflows.
Technology Stack
Python: Core language for building the application.
Whisper: Speech-to-text transcription.
OpenAI GPT: Command processing and natural language understanding.
SpeechRecognition: Captures audio input from users.
Pyttsx3: Text-to-speech for responses.


Getting Started

Prerequisites
Before running the project, ensure you have the following installed:

Python 3.8 or higher
OpenAI API key (create an account at OpenAI)
Required Python packages (see below)
Installation
Clone the Repository



git clone https://github.com/your-username/voice-money-request.git
cd voice-money-request
Install Dependencies Make sure you have pip installed. Then, run:



pip install -r requirements.txt
Set Up Environment Variables



OPENAI_API_KEY=your-openai-api-key
Replace your-openai-api-key with your actual API key.
Running the Application
To start the system, run the following command:



python main.py

How to Use

The system will start listening for voice input.

Speak your command, for example:

"I need to request money for project 223 to buy tools, the amount is 500 riyals."
The system will confirm the details:
"You are requesting money for project 223, amount: 500 riyals, for buying tools. Do you want to proceed?"
Say "Yes" to confirm, and the request will be submitted to the database.
Example Interactions
Scenario 1: Complete Information Provided
User: "I need to request money for project 101, amount 300 riyals, for new equipment."
AI Agent: "You are requesting money for project 101, amount: 300 riyals, for new equipment. Do you want to proceed?"
User: "Yes."
AI Agent: "Request submitted successfully."
Scenario 2: Missing Information
User: "I need to request money for buying tools."
AI Agent: "Can you provide the project number?"
User: "Project 105."
AI Agent: "And the amount?"
User: "200 riyals."
AI Agent: "You are requesting money for project 105, amount: 200 riyals, for buying tools. Do you want to proceed?"
User: "Yes."
AI Agent: "Request submitted successfully."

Deployment
Option 1: Deploy on Hugging Face Spaces
Create an account on Hugging Face.
Upload your code and set up a new Gradio space for your app.
Once deployed, share the live demo link.

Option 2: Deploy on Google Colab
Upload the project to a Google Colab notebook.
Install dependencies and run the code in the Colab environment.
Share the notebook link for others to interact with the system.

Database Structure
The application uses an SQLite database to store money request details. The database schema is as follows:

Field	Type	Description
id	INTEGER	Primary Key
project_id	TEXT	Project number
amount	REAL	Requested amount
reason	TEXT	Purpose of the request
status	TEXT	Request status (e.g., "Approved")
timestamp	TEXT	Time of the request
Future Enhancements
Support for multiple languages for voice recognition and responses.
Integration with other project management tools for automated approvals.
Deployment on cloud platforms like AWS or Azure for scalability.

Troubleshooting
Common Issues
Error: No API Key Provided


Speech Recognition Not Working
Check if your microphone is properly configured and accessible by the application.



Contributing
We welcome contributions! Feel free to open issues or submit pull requests to improve the project.

Fork the repository.
Create a new branch:


git checkout -b feature-branch
Make your changes and commit:


git commit -m "Add new feature"
Push to your branch:


git push origin feature-branch
Open a pull request on GitHub.
License
This project is licensed under the MIT License. See the LICENSE file for details.

Contact
For questions, feedback, or collaboration, reach out to:

Name: Easir Maruf
Email: easir956@gmail.com
LinkedIn: Easir Maruf
