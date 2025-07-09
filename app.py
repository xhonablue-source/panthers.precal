import streamlit as st
import matplotlib.pyplot as plt
import numpy as np

# --- Page Setup ---
st.set_page_config(page_title="Panther Vision: See the Function", page_icon="👁️")

# --- Title and Intro ---
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

# --- Common Core Strand Selection ---
strand = st.selectbox("📚 Choose a Common Core Math Strand:", [
    "HSA-CED.A.1 – Create equations",
    "HSF-IF.B.4 – Interpret key features of functions",
    "HSF-IF.C.7 – Graph functions expressed symbolically",
    "HSF-BF.A.1 – Build a function that models a relationship"
])

# --- Student Info (Moved Up) ---
name = st.text_input("Enter your name:")
avatar = st.selectbox("Choose your multidimensional shape avatar:", [
    "🔺 Tetrahedron", "🚘 Dodecahedron", "🪒 Cube", "🌀 Torus"
])

if name:
    st.success(f"Welcome, {name} the {avatar}! Let's begin Panther Vision.")

# --- Role or Identity Selection (Previously 'Drill Data Star') ---
role_options = [
    "🌟 Skill Mastery Star",
    "🚀 Growth Mode",
    "🎮 Level-Up Leader",
    "🎯 Focus Champ",
    "📊 Data Boss",
    "🧠 Brain Builder",
    "🎓 Panther Scholar",
    "📈 Goal Getter",
    "🛠️ Problem Solver",
    "💡 Idea Generator"
]

role = st.selectbox("Pick your learning mode or style:", role_options)

# --- Continue with rest of the interactive lesson below this ---
# Example placeholder:
st.markdown("## 🔍 Let's explore what a function looks like in real life...")

# You can insert function visualizations, modeling examples, toggles, etc. here...
