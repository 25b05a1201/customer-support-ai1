import streamlit as st
from agent import chat_with_agent
st.set_page_config(
    page_title="RecallCare AI",
    page_icon="🧠",
    layout="wide"
)
st.title("🧠 RecallCare AI")
st.caption(
    "Customer Support Agent that remembers every customer interaction"
)
# -----------------------------
# Sidebar
# -----------------------------
with st.sidebar:
    st.header("Customer")

    customer_id = st.text_input(
        "Customer ID",
        value="CUST-101"
    )

    st.divider()

    st.subheader("Why RecallCare?")

    st.write("""
    Traditional chatbots forget customers.

    RecallCare remembers:

    • Previous problems  
    • Customer environment  
    • Troubleshooting attempted  
    • Failed fixes  
    • Successful fixes  
    • Customer preferences
    """)


# -----------------------------
# Session chat
# -----------------------------

if "messages" not in st.session_state:

    st.session_state.messages = []


for message in st.session_state.messages:

    with st.chat_message(message["role"]):

        st.markdown(message["content"])
user_input = st.chat_input(
    "Describe your problem..."
)
if user_input:
    st.session_state.messages.append(
        {
            "role": "user",
            "content": user_input
        }
    )
    with st.chat_message("user"):
        st.markdown(user_input)
    with st.chat_message("assistant"):

        with st.spinner(
            "Checking customer history..."
        ):

            response, memories = chat_with_agent(
                customer_id,
                user_input
            )
        if memories:

            with st.expander(
                "🧠 Memories used by the AI"
            ):

                for memory in memories:

                    st.write("•", memory)
        st.markdown(response)
    st.session_state.messages.append(
        {
            "role": "assistant",
            "content": response
        }
    )