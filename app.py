# panther_vision.py

import streamlit as st
import matplotlib.pyplot as plt
import numpy as np

# Page Setup
st.set_page_config(page_title="Panther Vision: See the Function", page_icon="👁️")

# Title and Intro
st.title("👁️ Panther Vision: See the Function")
st.markdown("""
Welcome, **Englewood STEM Panthers**!  
This MathCraft lesson helps you **see, understand, and recognize** real-life functions — and what they mean for your world.

---

### 📘 Classic Explanation (McGraw-Hill Style):
A **function** is a rule that connects every input to exactly one output.  
Think of it like a vending machine: press a button (input), get a snack (output).  
You wouldn’t press one button and get random snacks — that’s not a function.

---

### 🎯 Objective:
By the end of this lesson, you'll be able to:
- Define and identify functions
- Distinguish between function types
- Match real-life examples to function models
- Interpret graphs and expressions
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
