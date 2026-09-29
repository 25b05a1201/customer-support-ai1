import os
from dotenv import load_dotenv
from hindsight_client import Hindsight

load_dotenv()

HINDSIGHT_API_URL = os.getenv(
    "HINDSIGHT_API_URL",
    "https://api.hindsight.vectorize.io"
)

HINDSIGHT_API_KEY = os.getenv("HINDSIGHT_API_KEY")

client = Hindsight(
    base_url=HINDSIGHT_API_URL,
    api_key=HINDSIGHT_API_KEY
)


def get_bank_id(customer_id):
    return f"customer-{customer_id}"


def ensure_bank(customer_id):
    bank_id = get_bank_id(customer_id)

    try:
        client.create_bank(
            bank_id=bank_id
        )
        print(f"Memory bank created: {bank_id}")

    except Exception as e:
        # If the bank already exists, continue normally.
        print(f"Bank already exists or could not be created: {e}")


def remember(customer_id, content):

    bank_id = get_bank_id(customer_id)

    try:
        ensure_bank(customer_id)

        client.retain(
            bank_id=bank_id,
            content=content
        )

        print("Memory saved successfully.")
        return True

    except Exception as e:
        print("Memory retain error:", e)
        return False


def recall_memory(customer_id, query):

    bank_id = get_bank_id(customer_id)

    try:
        ensure_bank(customer_id)

        result = client.recall(
            bank_id=bank_id,
            query=query
        )

        memories = []

        for item in result.results:
            if hasattr(item, "text"):
                memories.append(item.text)

        print(f"Memories found: {len(memories)}")

        return memories

    except Exception as e:
        print("Memory recall error:", e)
        return []