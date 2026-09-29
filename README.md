# 🧠 RecallCare AI

### Customer Support AI Agent with Persistent Memory

RecallCare AI is an intelligent customer-support agent that remembers previous customer interactions and uses that knowledge to provide more personalized support.

Instead of making customers repeat their problem every time, RecallCare remembers:

* Previous support issues
* Customer environment
* Troubleshooting steps
* Solutions that worked
* Solutions that failed
* Customer-specific context

## 🎯 Problem

Traditional AI support agents often treat every conversation as a new conversation.

This creates a frustrating experience because customers may need to repeatedly explain:

* What device they use
* Which operating system they have
* What problem occurred
* Which troubleshooting steps they already tried
* Which solution previously worked

## 💡 Solution

RecallCare AI adds persistent memory using **Hindsight**.

The agent follows this workflow:

```text
Customer Message
       ↓
Hindsight Recall
       ↓
Relevant Customer History
       ↓
Groq LLM
       ↓
Personalized Support Response
       ↓
Hindsight Retain
       ↓
Memory for Future Conversations
```

## 🧠 How Hindsight Is Used

Each customer receives an isolated memory bank.

Example:

```text
customer-CUST-101
```

The agent recalls relevant information from that customer's previous conversations before generating a response.

After responding, the interaction is stored back into Hindsight so future conversations can use it.

This creates a continuous learning loop:

```text
Recall → Understand → Respond → Remember → Improve
```

## 🧪 Demonstration

### Interaction 1

Customer:

> My CloudDesk application crashes whenever I upload files larger than 50 MB. I'm using Windows 11 on an HP laptop.

The agent receives and stores the customer's problem and environment.

### Interaction 2

Customer:

> Clearing the cache fixed the problem. Please remember that this worked for me.

The successful troubleshooting solution is stored in memory.

### Interaction 3

Customer:

> The same upload problem is happening again. What should I try first?

RecallCare retrieves the previous memory and recommends clearing the cache first.

### Customer Isolation Test

When another customer such as:

```text
CUST-102
```

asks:

> What laptop am I using?

The agent does not retrieve CUST-101's HP laptop information.

This demonstrates customer-specific memory isolation.

## 🛠️ Technology Stack

* Python
* Streamlit
* Groq
* Hindsight
* Hindsight Client SDK

## 🚀 Installation

Clone the repository:

```bash
git clone YOUR_GITHUB_REPOSITORY_URL
cd customer-support-ai
```

Create a virtual environment:

```bash
python -m venv venv
```

Activate it on Windows:

```powershell
venv\Scripts\Activate.ps1
```

Install dependencies:

```bash
pip install -r requirements.txt
```

Create a `.env` file:

```text
GROQ_API_KEY=your_groq_api_key
HINDSIGHT_API_KEY=your_hindsight_api_key
```

Never commit `.env` to GitHub.

Run:

```bash
streamlit run app.py
```

## 🏗️ Architecture

```text
                ┌───────────────────┐
                │     Customer      │
                └─────────┬─────────┘
                          ↓
                ┌───────────────────┐
                │    Streamlit UI   │
                └─────────┬─────────┘
                          ↓
                ┌───────────────────┐
                │ Hindsight Recall  │
                └─────────┬─────────┘
                          ↓
                ┌───────────────────┐
                │     Groq LLM      │
                └─────────┬─────────┘
                          ↓
                ┌───────────────────┐
                │ Personalized      │
                │ Support Response  │
                └─────────┬─────────┘
                          ↓
                ┌───────────────────┐
                │ Hindsight Retain  │
                └───────────────────┘
```

## 🌟 Key Value

RecallCare AI turns a generic support chatbot into a customer-aware support agent by giving it persistent memory.

The key difference is not only answering the current question, but remembering what happened before and using that experience in future support interactions.

## 📌 Hackathon

Built for **Hack With Hyderabad 3.0 — AI Agents That Learn Using Hindsight**.

The project uses Hindsight as the persistent memory layer required by the hackathon.
