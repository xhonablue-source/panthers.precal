# panther_vision.py

import streamlit as st
import matplotlib.pyplot as plt
import numpy as np

# Page Setup
st.set_page_config(page_title="Panther Vision: See the Function", page_icon="🐆")

# Title and Intro
st.title("🐆 Panther Vision: See the Function")
st.markdown("""
### *Temet Nosce* — Know Thyself  
**Panthers know themselves, and they know a function when they see one.**  
Pre-Calculus is about recognizing patterns and relationships — especially functions — so that they can be modeled, predicted, and **commanded**.

---

### 🎯 Purpose:
This lesson helps you:
- **Recognize** real-world functions
- **Understand** their structure and meaning
- **Command** them using mathematical models
""")

# Standards Dropdowns
with st.expander("📘 Illinois Pre-Calculus Standards"):
    st.markdown("""
- **MA.F-IF.A.1**: Understand that a function is a rule that assigns to each input exactly one output.
- **MA.F-IF.B.4**: For a function that models a relationship, interpret key features of graphs and tables.
- **MA.F-IF.C.7**: Graph functions expressed symbolically and show key features.
- **MA.F-BF.A.1**: Write a function that describes a relationship.
""")

with st.expander("📚 Common Core Math Practices"):
    st.markdown("""
- **MP.1**: Make sense of problems and persevere in solving them  
- **MP.2**: Reason abstractly and quantitatively  
- **MP.4**: Model with mathematics  
- **MP.7**: Look for and make use of structure
""")

# Classic Explanation
st.markdown("""
---

### 📘 Classic Explanation (McGraw-Hill Style):
A **function** is a rule that connects every input to exactly one output.  
Think of it like a vending machine: press a button (input), get a snack (output).  
You wouldn’t press one button and get random snacks — that’s not a function.

---
""")

# Student Info
name = st.text_input("Enter your name:")
avatar = st.selectbox("Choose your Chicago-based avatar:", [
    "🎧 Drill Data Star", "📈 Trend Analyst", "🏙️ South Side Coder", "🚇 CTA Function Rider"
])
if name:
    st.success(f"Welcome, {name} aka {avatar}! Let’s explore Panther Vision.")

# Real-Life Function Examples
st.header("🔟 Mapped Function Examples")

examples = [
    {
        "label": "Hourly Pay",
        "rule": lambda x: 15 * x,
        "expr": "f(x) = 15x",
        "unit": "(USD)",
        "desc": "💵 Earn 15 per hour at a part-time job."
    },
    {
        "label": "Spotify Streams",
        "rule": lambda x: 100 * (1.5 ** x),
        "expr": "f(x) = 100 × 1.5^x",
        "unit": "",
        "desc": "🎧 Get 100 → viral streams over days."
    },
    {
        "label": "Uber Fare",
        "rule": lambda x: 2.5 * x + 3,
        "expr": "f(x) = 2.5x + 3",
        "unit": "",
        "desc": "🚗 3 base + 2.5 per mile for a ride."
    },
    {
        "label": "Phone Battery",
        "rule": lambda x: 100 - 10 * x,
        "expr": "f(x) = 100 - 10x",
        "unit": "(%)",
        "desc": "🔋 Lose 10% battery/hour."
    },
    {
        "label": "Basketball Arc",
        "rule": lambda x: -1 * (x - 5)**2 + 25,
        "expr": "f(x) = -1(x - 5)^2 + 25",
        "unit": "(feet)",
        "desc": "🏀 Parabolic jump shot arc."
    },
    {
        "label": "YouTube Subs",
        "rule": lambda x: 2000 + 50 * x,
        "expr": "f(x) = 2000 + 50x",
        "unit": "(subs)",
        "desc": "📺 Gain 50 subs/week from a fanbase."
    },
    {
        "label": "Gym Progress",
        "rule": lambda x: 100 * np.log(x + 1),
        "expr": "f(x) = 100 × log(x + 1)",
        "unit": "(lbs)",
        "desc": "🏋🏽 Build strength — slows over time."
    },
    {
        "label": "Bus Time",
        "rule": lambda x: 10 * x + 5,
        "expr": "f(x) = 10x + 5",
        "unit": "(minutes)",
        "desc": "🚌 Each stop adds 10 mins + 5 min base."
    },
    {
        "label": "Temperature Drop",
        "rule": lambda x: 70 - 2 * x,
        "expr": "f(x) = 70 - 2x",
        "unit": "(°F)",
        "desc": "🌡️ Decrease of 2°F/hour."
    },
    {
        "label": "Water Bill",
        "rule": lambda x: 25 + 1.75 * x,
        "expr": "f(x) = 25 + 1.75x",
        "unit": "",
        "desc": "🚿 Pay 25 base + 1.75 per gallon."
    },
]

selected = st.selectbox("Choose a real-life function to explore:", [ex["label"] for ex in examples])
for ex in examples:
    if selected == ex["label"]:
        x_vals = np.linspace(0, 10, 100)
        y_vals = ex["rule"](x_vals)
        fig, ax = plt.subplots()
        ax.plot(x_vals, y_vals)
        ax.set_title(f"{ex['label']} — {ex['expr']} {ex['unit']}")
        ax.set_xlabel("x")
        ax.set_ylabel("f(x)")
        st.pyplot(fig)
        st.info(ex["desc"])

# Exit Reflection
st.header("🧾 Reflection")
reflection = st.text_area("What is one real-world situation you could model with a function?")
if st.button("Submit"):
    st.success("✅ Great work thinking like a mathematician!")

st.balloons()
