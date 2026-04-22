# Social-to-Lead Agentic Workflow (AutoStream)

## Project Overview

This project implements a conversational AI agent for a fictional SaaS product called AutoStream, which provides automated video editing for content creators.

The agent is designed to:

* Understand user intent
* Answer product-related queries using a knowledge base (RAG)
* Identify high-intent users
* Capture leads through a structured conversational workflow
  
## How to Run the Project Locally

1. Clone the repository:

```
git clone (https://github.com/deepoo07/autostream-agent)
cd autostream-agent
```

2. Ensure Python 3.9 or above is installed.

3. Run the application:

```
python app.py
```

4. Interact with the chatbot in the terminal.

## Architecture Explanation

This project follows a simple agentic workflow implemented using Python.

Instead of using LangGraph or AutoGen, a rule-based approach was used to clearly demonstrate the logic behind intent detection, knowledge retrieval, and action execution.

The system consists of the following components:

* Intent Detection: Classifies user input into greeting, pricing inquiry, or high-intent using keyword-based logic.
* RAG (Retrieval-Augmented Generation): Retrieves relevant information from a local JSON knowledge base containing pricing, features, and policies.
* Agent Logic: Controls the conversation flow and decision-making process.
* Tool Execution: Calls a mock lead capture function only after collecting all required user details.

State is managed using Python dictionaries (`conversation_state` and `lead_data`), which retain context across multiple conversation turns. This allows the agent to handle multi-step interactions such as collecting user information step-by-step.

## WhatsApp Deployment Using Webhooks

This agent can be integrated with WhatsApp using a service such as Twilio.

The workflow would be as follows:

1. A user sends a message on WhatsApp.
2. The message is forwarded to a backend server using a webhook.
3. The backend processes the message using the agent function.
4. The agent generates a response.
5. The response is sent back to the user via the WhatsApp API.

This setup enables real-time interaction between users and the conversational agent.

## Features

* Intent detection (greeting, pricing, high-intent)
* RAG-based responses using a local knowledge base
* Lead capture workflow (name, email, platform)
* Email validation
* Platform validation
* Multi-turn conversation handling
* Controlled conversation termination

## Video explanation

https://drive.google.com/file/d/1krAaE8LSBtOWs4PZUJCarPPbLnAT77JF/view?usp=sharing


## Tech Stack

* Python 3.9+
* JSON (for knowledge base)
