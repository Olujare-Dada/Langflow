from langflow.load import run_flow_from_json
from dotenv import load_dotenv



load_dotenv()


def ask_ai(profile, question):

    TWEAKS = {
    "TextInput-rbz9E": {
        "input_value": question
    },
    "TextInput-x4ECF": {
        "input_value": profile
    }
    }

    result = run_flow_from_json(flow="Ask_AI.json",
                                input_value="message",
                                session_id="", # provide a session id if you want to use session state
                                fallback_to_env_vars=True, # False by default
                                tweaks=TWEAKS)

    return result[0].outputs[0].results["text"].data["text"]