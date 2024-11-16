
import openai
import re

import openai

# Set your OpenAI API key
openai.api_key = "API key"

def process_voice_command(command):
    """Processes the voice command and determines the action."""
    try:
        # Step 1: Analyze the intent and extract details using OpenAI GPT
        intent, details = analyze_command_with_openai(command)

        if intent == "money_request":
            project = details.get("project")
            amount = details.get("amount")
            reason = details.get("reason")
            
            if not project or not amount or not reason:
                return "Incomplete details. Please specify the project, amount, and reason.", None

            confirmation_text = (
                f"You are requesting {amount} Riyals for project {project} to {reason}. "
                "Do you want to proceed?"
            )
            return confirmation_text, details
        else:
            return "Sorry, I didn't understand that command.", None

    except Exception as e:
        print(f"Error processing command: {e}")
        return "An error occurred while processing your request.", None

def analyze_command_with_openai(command):
    """Uses OpenAI to extract intent and entities from the command."""
    prompt = (
        f"Extract the intent and relevant details from this command:\n"
        f"Command: '{command}'\n\n"
        "Return the intent as 'money_request' if it's about requesting money. "
        "Extract the following details if available:\n"
        "- project: Project number\n"
        "- amount: Amount of money\n"
        "- reason: Purpose for the request\n"
        "Respond in JSON format."
    )

    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[{"role": "user", "content": prompt}],
        max_tokens=100,
        temperature=0.5
    )

    # Parse the OpenAI response to get intent and details
    message = response['choices'][0]['message']['content']
    print(f"OpenAI Response: {message}")
    
    try:
        # Convert the response to a dictionary
        result = eval(message)
        return result.get("intent"), result.get("details", {})
    except:
        return None, {}

