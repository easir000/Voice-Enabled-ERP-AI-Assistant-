<p>Voice-Based Money Request System<br />Project Overview<br />This project implements an AI-powered voice command system for handling money requests, such as budget approvals for projects. The system takes spoken input from users, extracts key details like project numbers, amounts, and purposes, and confirms the request before saving it to a database.</p>
<p>The solution uses speech recognition, OpenAI&rsquo;s GPT model for understanding commands, and Whisper for speech-to-text transcription. It also integrates a simple validation flow to ensure that all necessary information is provided by the user before submitting a request.</p>
<p>Features<br />Voice and Text Interaction: Users can interact using voice commands or text inputs.<br />Field Validation: Ensures required fields like project number and amount are provided.<br />Confirmation Flow: Asks for user confirmation before submitting a request.<br />Database Storage: Successfully processed requests are stored in an SQLite database.<br />Extensible Design: Can be expanded to support additional workflows.<br />Technology Stack<br />Python: Core language for building the application.<br />Whisper: Speech-to-text transcription.<br />OpenAI GPT: Command processing and natural language understanding.<br />SpeechRecognition: Captures audio input from users.<br />Pyttsx3: Text-to-speech for responses.</p>
<p><br />Getting Started</p>
<p>Prerequisites<br />Before running the project, ensure you have the following installed:</p>
<p>Python 3.8 or higher<br />OpenAI API key (create an account at OpenAI)<br />Required Python packages (see below)<br />Installation<br />Clone the Repository</p>
<p>&nbsp;</p>
<p>git clone [https://github.com/your-username/voice-money-request.git](https://github.com/easir000/voice-money-request.git)<br />cd voice-money-request<br />Install Dependencies Make sure you have pip installed. Then, run:</p>
<p>&nbsp;</p>
<p>pip install -r requirements.txt<br />Set Up Environment Variables</p>
<p>&nbsp;</p>
<p>OPENAI_API_KEY=your-openai-api-key<br />Replace your-openai-api-key with your actual API key.<br />Running the Application<br />To start the system, run the following command:</p>
<p>&nbsp;</p>
<p>python main.py</p>
<p>How to Use</p>
<p>The system will start listening for voice input.</p>
<p>Speak your command, for example:</p>
<p>"I need to request money for project 223 to buy tools, the amount is 500 riyals."<br />The system will confirm the details:<br />"You are requesting money for project 223, amount: 500 riyals, for buying tools. Do you want to proceed?"<br />Say "Yes" to confirm, and the request will be submitted to the database.<br />Example Interactions<br />Scenario 1: Complete Information Provided<br />User: "I need to request money for project 101, amount 300 riyals, for new equipment."<br />AI Agent: "You are requesting money for project 101, amount: 300 riyals, for new equipment. Do you want to proceed?"<br />User: "Yes."<br />AI Agent: "Request submitted successfully."<br />Scenario 2: Missing Information<br />User: "I need to request money for buying tools."<br />AI Agent: "Can you provide the project number?"<br />User: "Project 105."<br />AI Agent: "And the amount?"<br />User: "200 riyals."<br />AI Agent: "You are requesting money for project 105, amount: 200 riyals, for buying tools. Do you want to proceed?"<br />User: "Yes."<br />AI Agent: "Request submitted successfully."</p>
<p>Deployment<br />Option 1: Deploy on Hugging Face Spaces<br />Create an account on Hugging Face.<br />Upload your code and set up a new Gradio space for your app.<br />Once deployed, share the live demo link.</p>
<p>Option 2: Deploy on Google Colab<br />Upload the project to a Google Colab notebook.<br />Install dependencies and run the code in the Colab environment.<br />Share the notebook link for others to interact with the system.</p>
<p>Database Structure<br />The application uses an SQLite database to store money request details. The database schema is as follows:</p>
<p>Field Type Description<br />id INTEGER Primary Key<br />project_id TEXT Project number<br />amount REAL Requested amount<br />reason TEXT Purpose of the request<br />status TEXT Request status (e.g., "Approved")<br />timestamp TEXT Time of the request<br />Future Enhancements<br />Support for multiple languages for voice recognition and responses.<br />Integration with other project management tools for automated approvals.<br />Deployment on cloud platforms like AWS or Azure for scalability.</p>
<p>Troubleshooting<br />Common Issues<br />Error: No API Key Provided</p>
<p><br />Speech Recognition Not Working<br />Check if your microphone is properly configured and accessible by the application.</p>
<p>&nbsp;</p>
<p>Contributing<br />We welcome contributions! Feel free to open issues or submit pull requests to improve the project.</p>
<p>Fork the repository.<br />Create a new branch:</p>
<p><br />git checkout -b feature-branch<br />Make your changes and commit:</p>
<p><br />git commit -m "Add new feature"<br />Push to your branch:</p>
<p><br />git push origin feature-branch<br />Open a pull request on GitHub.<br />License<br />This project is licensed under the MIT License. See the LICENSE file for details.</p>
<p>Contact<br />For questions, feedback, or collaboration, reach out to:</p>
<p>Name: Easir Maruf<br />Email: easir956@gmail.com<br />LinkedIn: Easir Maruf</p>
