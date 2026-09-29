import os
from groq import Groq
from dotenv import load_dotenv

from memory import recall_memory, remember

load_dotenv()

groq_client = Groq(
    api_key=os.getenv("GROQ_API_KEY")
)


SYSTEM_PROMPT = """
You are RecallCare AI, an intelligent customer support agent.

Your job is to help customers solve technical problems.

You should:
1. Use relevant previous customer history.
2. Avoid asking for information that is already remembered.
3. Remember previous troubleshooting steps.
4. Consider whether previous solutions worked or failed.
5. Be polite and professional.
6. Ask focused questions when more information is needed.
7. Never invent customer history.
"""


def chat_with_agent(customer_id, user_message):

    # Get relevant memories
    memories = recall_memory(
        customer_id,
        user_message
    )

    if memories:
        memory_context = "\n".join(
            f"- {memory}" for memory in memories
        )
    else:
        memory_context = "No relevant previous customer history."

    prompt = f"""
CUSTOMER MEMORY:

{memory_context}

CURRENT CUSTOMER MESSAGE:

{user_message}

Answer the customer as a helpful support agent.
Use the customer memory when relevant.
"""
    # Ask Groq
    response = groq_client.chat.completions.create(

        model="openai/gpt-oss-120b",

        messages=[
            {
                "role": "system",
                "content": SYSTEM_PROMPT
            },
            {
                "role": "user",
                "content": prompt
            }
        ],

        temperature=0.3
    )
    answer = response.choices[0].message.content
    # Store this interaction in Hindsight
    memory_record = f"""
Customer said:
{user_message}

Support agent replied:
{answer}
"""

    remember(
        customer_id,
        memory_record
    )
    return answer, memories