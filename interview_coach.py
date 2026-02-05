import streamlit as st
import speech_recognition as sr
from openai import OpenAI

# --- CONFIGURATION ---
st.set_page_config(page_title="INDG Architect Prep v2", page_icon="🏗️", layout="wide")

# --- CONTEXT & PROMPTS ---
JOB_CONTEXT = """
COMPANY: INDG (Industrial/Defense Digital Group)
ROLE: Web Application Architect 3
STACK: AWS (Serverless focus), Event-Driven Architecture (EDA), Microservices, Micro-frontends.
LEVEL: Senior/Principal IC.
"""

# The "Bar Raiser" System Prompt
SYSTEM_PROMPT = f"""
You are a Principal Software Architect and "Bar Raiser" interviewer at a top-tier tech firm. 
You are interviewing a candidate for a 'Web Application Architect 3' role.
CONTEXT: {JOB_CONTEXT}

YOUR GOAL:
Do not just "correct" the user. You must teach them the *mental model* behind the answer.
Architect interviews are about **TRADE-OFFS**, not just definitions.

INSTRUCTIONS:
Analyze the candidate's answer and output feedback in this specific Markdown structure:

### 🎯 Scorecard
* **Technical Accuracy:** (1-5 Stars)
* **Communication Clarity:** (Did they start high-level then go deep? Or did they ramble?)
* **Seniority Signal:** (Did they sound like a Junior Dev or a System Architect?)

### ⚖️ The Trade-Off Analysis (Crucial)
(Explain the "Why". If they chose Solution A, explain why Solution B might have been better or worse.
*Example:* "You suggested SNS for messaging, but for this specific order-preservation use case, Kinesis would be safer due to shard ordering.")

### 🧠 Mental Model Check
(Identify which architectural pattern applies here: e.g., CAP Theorem, Saga Pattern, CQRS, Strangler Fig.
Explain if they applied it correctly.)

### 🚀 The "Level-Up" Rephrase
(Rewrite their core argument in the voice of a Principal Architect. Use precise terminology like 'idempotency', 'eventual consistency', 'coupling', 'cohesion'.)
"""

# --- QUESTION BANKS (TIERED) ---

QUESTIONS_BEHAVIORAL = {
    "🟢 Foundational": [
        "Tell me about yourself and your history with AWS.",
        "Why do you want to leave your current role for INDG?",
        "Describe a time you had a conflict with a developer."
    ],
    "🟡 Intermediate": [
        "Tell me about a time you had to mentor a mid-level engineer. How did you measure their growth?",
        "Describe a time you missed a deadline. How did you communicate it to stakeholders?",
        "How do you handle 'Analysis Paralysis' in your team when choosing a tech stack?"
    ],
    "🔴 Deep Dive (Influence)": [
        "Tell me about a time you strongly disagreed with Management/Product about a feature that would introduce massive technical debt. Did you block it? Why or why not?",
        "You need to convince a team to move from a Monolith to Micro-frontends, but they are resistant to change. Roleplay your opening pitch.",
        "Describe a failure that was entirely your fault. How did it impact the business, and what systemic change did you implement to prevent recurrence?"
    ]
}

QUESTIONS_SYSTEM_DESIGN = {
    "🟢 Foundational": [
        "What is the difference between Horizontal and Vertical scaling?",
        "Explain the concept of 'Cold Starts' in AWS Lambda and one simple way to mitigate them.",
        "What is a Microservice? How does it differ from a Monolith?",
        "Explain 'Infrastructure as Code' to a non-technical Project Manager."
    ],
    "🟡 Intermediate": [
        "We need to decouple our Order Service from our Inventory Service. Explain how you would use AWS SNS and SQS to achieve this.",
        "Design a simple CI/CD pipeline for a serverless application. What stages are critical?",
        "What are the pros and cons of using a Shared Database pattern vs. Database-per-Service?",
        "Explain the 'Strangler Fig' pattern for legacy migration."
    ],
    "🔴 Deep Dive (Architectural)": [
        "Design a highly available Event-Driven Architecture for a logistics platform processing 10k events/second. Discuss 'At-least-once' vs 'Exactly-once' delivery guarantees in your design.",
        "We are seeing data inconsistencies between our Read database and Write database in a CQRS setup. How do you troubleshoot and resolve this lag?",
        "Micro-frontends introduce complexity in shared state and styling. When would you argue *AGAINST* using Micro-frontends?",
        "How do you design for 'Idempotency' in a payment processing system where the network might time out after the request is sent?"
    ]
}

# --- FUNCTIONS ---

def transcribe_audio(audio_file):
    r = sr.Recognizer()
    try:
        with sr.AudioFile(audio_file) as source:
            audio_data = r.record(source)
            text = r.recognize_google(audio_data)
            return text
    except sr.UnknownValueError:
        return "Error: Could not understand audio."
    except Exception as e:
        return f"Error processing audio: {e}"

def get_ai_feedback(api_key, stage, question, answer):
    if not api_key:
        return "⚠️ Please enter your OpenRouter API Key in the sidebar."
    
    client = OpenAI(base_url="https://openrouter.ai/api/v1", api_key=api_key)
    
    try:
        completion = client.chat.completions.create(
            model="google/gemini-2.0-flash-001",
            messages=[
                {"role": "system", "content": SYSTEM_PROMPT},
                {"role": "user", "content": f"STAGE: {stage}\nQUESTION: {question}\nCANDIDATE ANSWER: {answer}"}
            ]
        )
        return completion.choices[0].message.content
    except Exception as e:
        return f"Error connecting to AI: {e}"

# --- SIDEBAR ---
with st.sidebar:
    st.header("⚙️ Coach Settings")
    api_key = st.text_input("OpenRouter API Key", type="password")
    
    st.markdown("### 🗺️ Difficulty Guide")
    st.info("🟢 **Foundational:** Definitions & Basic Concepts.\n\n🟡 **Intermediate:** Implementation & Standard Patterns.\n\n🔴 **Deep Dive:** Edge cases, Trade-offs, & Failure Modes.")
    
    st.markdown("---")
    st.write("Current Focus: **Web App Architect 3**")

# --- MAIN APP ---
st.title("🏗️ INDG Architect Prep (Deep Dive Mode)")
st.markdown("Use the tabs below to switch between Behavioral fit and Technical System Design. **Pay attention to the difficulty tiers.**")

tab1, tab2 = st.tabs(["👔 Behavioral & Leadership", "☁️ System Design & Architecture"])

# === TAB 1: BEHAVIORAL ===
with tab1:
    st.subheader("Leadership & Soft Skills")
    
    # Tier Selection
    tier_b = st.selectbox("Select Difficulty:", list(QUESTIONS_BEHAVIORAL.keys()), key="tier_b")
    
    # Question Selection based on Tier
    q_b = st.selectbox("Select Question:", QUESTIONS_BEHAVIORAL[tier_b], key="q_b")
    
    st.markdown(f"### ❓ {q_b}")
    
    ans_b = st.text_area("Your Response:", height=150, key="ans_b")
    audio_b = st.audio_input("Record Answer:", key="audio_b")
    
    final_ans_b = ans_b
    if audio_b:
        txt = transcribe_audio(audio_b)
        if "Error" not in txt:
            st.success(f"Transcribed: {txt}")
            final_ans_b = txt

    if st.button("Analyze Leadership", key="btn_b"):
        if final_ans_b:
            with st.spinner("Analyzing influence & seniority..."):
                st.markdown(get_ai_feedback(api_key, "Behavioral", q_b, final_ans_b))

# === TAB 2: SYSTEM DESIGN ===
with tab2:
    st.subheader("Technical Architecture")
    
    # Tier Selection
    tier_t = st.selectbox("Select Difficulty:", list(QUESTIONS_SYSTEM_DESIGN.keys()), key="tier_t")
    
    # Question Selection based on Tier
    q_t = st.selectbox("Select Question:", QUESTIONS_SYSTEM_DESIGN[tier_t], key="q_t")
    
    st.markdown(f"### ❓ {q_t}")
    st.caption("Tip: For Deep Dive questions, assume high scale (100k+ users) and focus on failure scenarios.")
    
    ans_t = st.text_area("Your Response (Describe your diagram/logic):", height=250, key="ans_t")
    audio_t = st.audio_input("Record Answer:", key="audio_t")
    
    final_ans_t = ans_t
    if audio_t:
        txt = transcribe_audio(audio_t)
        if "Error" not in txt:
            st.success(f"Transcribed: {txt}")
            final_ans_t = txt

    if st.button("Analyze Architecture", key="btn_t"):
        if final_ans_t:
            with st.spinner("Analyzing trade-offs & patterns..."):
                st.markdown(get_ai_feedback(api_key, "System Design", q_t, final_ans_t))

# --- FOOTER ---
st.markdown("---")
st.caption("System Design Interview Coach | Version 2.0")