import streamlit as st
import json
import os
from rapidfuzz import process, fuzz

# --- 1. SETUP & INITIALIZATION ---
DB_FILE = "brain.json"

def load_brain():
    if os.path.exists(DB_FILE):
        with open(DB_FILE, "r") as f:
            return json.load(f)
    else:
        return {"who are you": "I am an AI made by Anmol."}

def save_brain(data):
    with open(DB_FILE, "w") as f:
        json.dump(data, f, indent=4)

# NEW: This function turns complex datasets into simple Q&A pairs
def flatten_data(raw_data):
    flattened = {}
    # Check if this is an "intents" style file
    if isinstance(raw_data, dict) and "intents" in raw_data:
        for intent in raw_data["intents"]:
            for pattern in intent.get("patterns", []):
                # We store the first response for each pattern
                if intent.get("responses"):
                    flattened[pattern.lower().strip()] = intent["responses"][0]
        return flattened
    # If it's already a simple { "q": "a" } file, just return it
    return raw_data

knowledge_base = load_brain()

# --- 2. SIDEBAR ---
st.sidebar.title("Data Management")

uploaded_file = st.sidebar.file_uploader("Upload any .json dataset", type="json")
if uploaded_file is not None:
    try:
        raw_upload = json.load(uploaded_file)
        # Use our smart flattener
        new_knowledge = flatten_data(raw_upload)
        
        # Merge into the brain
        knowledge_base.update(new_knowledge)
        save_brain(knowledge_base)
        st.sidebar.success(f"Learned {len(new_knowledge)} new things!")
    except Exception as e:
        st.sidebar.error(f"Error reading file: {e}")

# Download button
json_string = json.dumps(knowledge_base, indent=4)
st.sidebar.download_button(label="Download Trained Brain", data=json_string, file_name="brain.json")

# --- 3. MAIN CHAT ---
st.title("Anmol's Learning AI")
user_query = st.text_input("User:", placeholder="Type here...").lower().strip()

if user_query:
    questions = list(knowledge_base.keys())
    
    # We "think hard" here by checking similarity
    match_result = process.extractOne(user_query, questions, scorer=fuzz.WRatio)
    
    if match_result:
        best_match, score, _ = match_result
        # If match is better than 75%, answer from memory
        if score > 95:
            st.info(f"**AI:** {knowledge_base[best_match]}")
        else:
            # Not a good enough match
            st.warning("I don't know that yet.")
            new_answer = st.text_input("What's the answer?")
            if st.button("Teach Me"):
                knowledge_base[user_query] = new_answer
                save_brain(knowledge_base)
                st.success("Learned!")
                st.rerun()