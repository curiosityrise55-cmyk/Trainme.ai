🧠 Learning AI
A community-driven, self-evolving Knowledge Base AI.

This project is a lightweight, "retrieval-based" AI model built to run efficiently on entry-level hardware (like an Intel Core i3 with 10GB RAM). Unlike traditional AIs that require massive GPUs, this model uses Fuzzy Logic to match user queries against a dynamically expanding JSON "brain."

🚀 How It Works
The AI follows a "Check-Answer-Learn" logic flow:

Check: When a user asks a question, the AI scans its brain.json file.

Match: It uses the Rapidfuzz library to calculate the similarity between the user's input and known questions.

Answer: If the similarity score is above 75%, it provides the stored answer.

Learn: If the AI doesn't recognize the question, it asks the user to teach it. Once the user provides an answer, the AI saves it instantly to its memory for future use.

🛠️ Features
Dynamic Learning: Users can train the AI directly through the web interface.

Dataset Support: Supports bulk training by uploading .json datasets (including "Intents" format).

Fuzzy Search: Handles typos and variations in questioning (e.g., "Hi" vs "Hii").

Data Portability: Features a download button to export the trained brain.json at any time.

Zero-Cost Hosting: Designed to run on Streamlit Community Cloud for free.

📂 Project Structure
train.py: The main Python script containing the Streamlit UI and matching logic.

brain.json: The "Memory" of the AI, stored as key-value pairs.

requirements.txt: List of dependencies needed for the cloud environment.

intents.json: An example dataset used for initial training.

💻 Technical Specifications
This project was optimized to run on a Sony VAIO with the following specs:

CPU: Intel Core i3-3217U @ 1.80GHz

RAM: 10 GB

Storage: 320 GB HDD (Toshiba)

OS: Windows 10

📥 Installation (For Local Development)
To run this project on your own computer:

Clone the repository:

Bash
git clone https://github.com/YOUR_USERNAME/YOUR_REPO_NAME.git
Install dependencies:

Bash
pip install streamlit rapidfuzz
Run the app:

Bash
streamlit run train.py
🎯 Future Goals
Scaling to Math: Implementing datasets covering algebra, calculus, and physics.

Database Integration: Moving from a JSON file to a SQL database for handling millions of data points.

Natural Language Processing: Adding sentiment analysis to understand user emotions.

👨‍💻 Developed By
Anmol - Aspiring AI Engineer
