import streamlit as st

# --- Page Config ---
st.set_page_config(page_title="Developer Portfolio", page_icon="💻", layout="wide")

# --- Sidebar ---
with st.sidebar:
    st.image("https://avatars.githubusercontent.com/u/9919?s=200&v=4", width=150)  # Placeholder logo
    st.title("M.Bilal")
    st.markdown("🚀 Beginner Python Developer ")
    st.markdown("📍 Karachi, PAKISTAN")
    st.markdown("📧 bilalseo@gmail.com")
    st.markdown("🌐 [GitHub](https://github.com/MBilalSIddiqi)")
    st.markdown("🔗 [LinkedIn](https://www.linkedin.com/in/umme-bilal-11299229a/`)")

# --- Title ---
st.title("💼 Portfolio")

# --- About Section ---
st.header("About Me")
st.write("""
HI, I am Bilal 
a student at PIAIC and an aspiring Python developer, currently seeking opportunities to gain hands-on experience and grow my skills in a real-world environment."
""")

# --- Skills Section ---
st.header("🛠️ Skills")
cols = st.columns(3)
cols[0].markdown("- Python")
cols[1].markdown("- Strreamlit")
cols[2].markdown("- Chainlit")

# --- Projects Section ---
st.header("📂 Projects")

with st.expander("🌐 Project 1:  Console-Based Hangman Game"):
    st.write("""
    - Built a  simple text-based Hangman game in Python.
    - Tech:Python, Random module, String manipulation
    - [Source Code](https://github.com/MBilalSIddiqi/Beginner-Projects/blob/main/HANGMAN.py)
    """)

with st.expander("📱 Project 2: Console-Based Math Quiz Game"):
    st.write("""
    - Created an interactive math quiz game in Python that generates random arithmetic problems using basic operators.
    - Tech: Python, random, operator modules
    - [Source Code](tps://github.com/MBilalSIddiqi/Beginner-Projects/blob/main/Math_quiz.py)
    """)

with st.expander("🎮 Project 3: Mini Ludo Game (2-Player Console Edition)"):
    st.write("""
    - Developed a two-player console-based Ludo game where players roll dice in turns to race to position 30.
    - Tech: Python, File Handling, Random module
    - [GitHub](https://github.com/MBilalSIddiqi/Beginner-Projects/blob/main/Ludo_game.py)
    """)
with st.expander("🔐 Project 4: Console-Based User Authentication System"):
    st.write("""
    - Built a simple authentication system in Python with login/logout functionality, profile viewing, and access control using decorators.
    - Tech: Python, Dictionaries, Decorators, Control Flow
    - [GitHub](https://github.com/MBilalSIddiqi/Beginner-Projects/blob/main/simple_login_program.py)
    """)
with st.expander("🌡️Project 6: Weather Checker using OpenWeatherMap API ☁️"):
    st.write("""
    - Developed a Python script that fetches and displays real-time weather data using the OpenWeatherMap API.
    - Tech: Python, requests module, OpenWeatherMap API
    - [GitHub](https://github.com/MBilalSIddiqi/Beginner-Projects/blob/main/Weather_checker.py)
    """)

# --- Footer ---
st.markdown("---")
st.write("© 2025 bilal  | Made with Streamlit")

