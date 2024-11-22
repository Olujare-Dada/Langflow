# AI-Powered Profile Assistant
This project demonstrates an AI-powered assistant using LangFlow and AstraDB to answer user questions based on profiles and other indexed data.

![image](https://github.com/user-attachments/assets/7a2e1ff7-c428-45e8-89c3-dbed8cb00a6c)
> Image of the Langflow architecture
<br>

## Features
- AI Agent with LangFlow: Built an AI agent using LangFlow to process and respond to user queries.
- AstraDB Integration: Uses AstraDB for indexing and storing data (e.g., profile notes).
- Customizable Inputs: Supports user-provided profiles and dynamic queries via a Python script.

## Setup and Installation
### Prerequisites
- Python 3.8 or higher
- LangFlow installed
- AstraDB account and database
- `.env` file with necessary environment variables (e.g., database credentials)

## Steps
Clone the repository:
```
git clone https://github.com/Olujare-Dada/Langflow.git
cd Langflow
```

Install dependencies:
```
pip install -r requirements.txt

```

Create a `.env` file in the root directory and add your environment variables:
```
ASTRA_DB_ID=your_db_id
ASTRA_DB_REGION=your_db_region
ASTRA_DB_KEYSPACE=your_keyspace
ASTRA_DB_CLIENT_ID=your_client_id
ASTRA_DB_CLIENT_SECRET=your_client_secret

```

# How It Works
Input Parameters:

**Profile**: A user-specific profile or context.
**Question**: A query for the AI agent.
**Processing**:
The Python script customizes inputs using TWEAKS.
The `run_flow_from_json` function runs the LangFlow workflow.

**Output**:
The AI agent responds based on the profile and data retrieved from AstraDB.
