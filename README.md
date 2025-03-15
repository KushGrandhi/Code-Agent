# Coding AI Agent

## Overview
This project implements an AI-powered agent system designed to assist with various tasks, including:
- Running terminal commands
- Browsing the internet
- Generating and managing code
- Searching LinkedIn profiles for relevant data

The agents are built using `agno` and leverage various models like Groq and Gemini to provide intelligent automation and assistance.

## How to Run
To get started with this agent system, follow these steps:

1. **Clone the Repository**
   ```sh
   git clone <repository-url>
   cd <repository-folder>
   ```
2. **Install Dependencies**
   Ensure you have `python-dotenv` installed and properly set up environment variables in a `.env` file:
   ```sh
   pip install -r requirements.txt
   ```
3. **Set Up API Keys**
   Create a `.env` file and add your API keys:
   ```sh
   GROQ_API_KEY=your_groq_api_key
   AGNO_API_KEY=your_agno_api_key
   GOOGLE_API_KEY=your_google_api_key
   ```
4. **Run the Agent**
   ```sh
   python main.py
   ```
   This will start an interactive session where you can chat with the agent.

## What Are Agents?
Agents in this system are AI-powered assistants designed to specialize in different tasks. Each agent has a unique role, and they work together to achieve complex objectives.

### Available Agents
- **Terminal Agent**: Executes terminal commands to navigate and modify the system.
- **Browser Agent**: Searches the web for relevant information.
- **Code Generator Agent**: Writes and refines code based on user requests.
- **Software Development Engineer (SDE) Agent**: Oversees code development and manages the project structure.

## Capabilities
- **Internet Access**: The browser agent can fetch information from the web to answer queries accurately.
- **Conversational AI**: Users can interact naturally with the system, making it feel like an intelligent assistant.
- **Code Generation and Project Management**: The coding agent can write code, create files, and manage project structures automatically.
- **Terminal Interaction**: The system can navigate directories, execute commands, and manipulate files using shell commands.

## Example Usage
### Running a Terminal Command
```sh
You: List files in the current directory
Agent: Running `ls`
...
```
### Searching the Web
```sh
You: Find the latest research papers on AI
Agent: Searching Google...
...
```
### Generating Code
```sh
You: Create a Python script to scrape a website
Agent: Writing the script...
...
```
### Managing a Project
```sh
You: Create a new folder for the project and initialize it with a README
Agent: Done. You can now start working on your project!
```

## Future Enhancements
- Integration with more APIs for extended functionality.
- More intelligent decision-making capabilities.
- Improved interaction with cloud-based storage and services.



