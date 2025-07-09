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
You wouldn't press one button and get random snacks — that's not a function.

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

# --- Function Explorer Section ---
st.header("🔍 Let's explore what a function looks like in real life...")

# Real-Life Function Examples
st.header("🔟 Mapped Function Examples")

examples = [
    {
        "label": "Hourly Pay",
        "rule": lambda x: 15 * x,
        "expr": "f(x) = 15x",
        "unit": "(USD)",
        "desc": "💵 Earn $15 per hour at a part-time job.",
        "domain": "Hours worked (0-40)",
        "range": "Dollars earned ($0-$600)"
    },
    {
        "label": "Spotify Streams",
        "rule": lambda x: 100 * (1.5 ** x),
        "expr": "f(x) = 100 × 1.5^x",
        "unit": "(streams)",
        "desc": "🎧 Start with 100 streams, grow exponentially by 50% each day.",
        "domain": "Days (0-10)",
        "range": "Stream count (100-5,766)"
    },
    {
        "label": "Uber Fare",
        "rule": lambda x: 2.5 * x + 3,
        "expr": "f(x) = 2.5x + 3",
        "unit": "(USD)",
        "desc": "🚗 $3 base fare + $2.50 per mile for a ride.",
        "domain": "Miles traveled (0-20)",
        "range": "Total fare ($3-$53)"
    },
    {
        "label": "Phone Battery",
        "rule": lambda x: max(0, 100 - 10 * x),
        "expr": "f(x) = 100 - 10x",
        "unit": "(%)",
        "desc": "🔋 Lose 10% battery per hour of use.",
        "domain": "Hours of use (0-10)",
        "range": "Battery percentage (0-100%)"
    },
    {
        "label": "Basketball Arc",
        "rule": lambda x: np.maximum(0, -1 * (x - 5)**2 + 25),
        "expr": "f(x) = -1(x - 5)² + 25",
        "unit": "(feet)",
        "desc": "🏀 Parabolic jump shot arc - height vs horizontal distance.",
        "domain": "Horizontal distance (0-10 feet)",
        "range": "Height (0-25 feet)"
    },
    {
        "label": "YouTube Subscribers",
        "rule": lambda x: 2000 + 50 * x,
        "expr": "f(x) = 2000 + 50x",
        "unit": "(subs)",
        "desc": "📺 Start with 2000 subscribers, gain 50 per week.",
        "domain": "Weeks (0-52)",
        "range": "Subscriber count (2,000-4,600)"
    },
    {
        "label": "Gym Progress",
        "rule": lambda x: 100 * np.log(x + 1),
        "expr": "f(x) = 100 × log(x + 1)",
        "unit": "(lbs)",
        "desc": "🏋🏽 Build strength - rapid gains early, then slows over time.",
        "domain": "Weeks of training (0-52)",
        "range": "Strength gained (0-395 lbs)"
    },
    {
        "label": "Bus Route Time",
        "rule": lambda x: 10 * x + 5,
        "expr": "f(x) = 10x + 5",
        "unit": "(minutes)",
        "desc": "🚌 Each bus stop adds 10 minutes + 5 minute base time.",
        "domain": "Number of stops (0-15)",
        "range": "Total time (5-155 minutes)"
    },
    {
        "label": "Temperature Drop",
        "rule": lambda x: 70 - 2 * x,
        "expr": "f(x) = 70 - 2x",
        "unit": "(°F)",
        "desc": "🌡️ Temperature decreases 2°F per hour after sunset.",
        "domain": "Hours after sunset (0-20)",
        "range": "Temperature (30-70°F)"
    },
    {
        "label": "Water Bill",
        "rule": lambda x: 25 + 1.75 * x,
        "expr": "f(x) = 25 + 1.75x",
        "unit": "(USD)",
        "desc": "🚿 Pay $25 base fee + $1.75 per 100 gallons used.",
        "domain": "Hundreds of gallons (0-50)",
        "range": "Bill amount ($25-$112.50)"
    },
]

# Function Selection and Visualization
selected = st.selectbox("Choose a real-life function to explore:", [ex["label"] for ex in examples])

# Find the selected example
selected_ex = None
for ex in examples:
    if selected == ex["label"]:
        selected_ex = ex
        break

if selected_ex:
    # Create two columns for layout
    col1, col2 = st.columns([2, 1])
    
    with col1:
        # Generate appropriate x values based on the function
        if selected == "Basketball Arc":
            x_vals = np.linspace(0, 10, 100)
        elif selected == "Phone Battery":
            x_vals = np.linspace(0, 10, 100)
        elif selected == "Gym Progress":
            x_vals = np.linspace(0, 52, 100)
        elif selected == "YouTube Subscribers":
            x_vals = np.linspace(0, 52, 100)
        elif selected == "Water Bill":
            x_vals = np.linspace(0, 50, 100)
        elif selected == "Bus Route Time":
            x_vals = np.linspace(0, 15, 100)
        elif selected == "Temperature Drop":
            x_vals = np.linspace(0, 20, 100)
        else:
            x_vals = np.linspace(0, 10, 100)
        
        y_vals = selected_ex["rule"](x_vals)
        
        # Create the plot
        fig, ax = plt.subplots(figsize=(10, 6))
        ax.plot(x_vals, y_vals, linewidth=3, color='#1f77b4')
        ax.set_title(f"{selected_ex['label']} — {selected_ex['expr']} {selected_ex['unit']}", 
                    fontsize=14, fontweight='bold')
        ax.set_xlabel("Input (x)", fontsize=12)
        ax.set_ylabel(f"Output f(x) {selected_ex['unit']}", fontsize=12)
        ax.grid(True, alpha=0.3)
        ax.set_facecolor('#f8f9fa')
        
        st.pyplot(fig)
    
    with col2:
        st.info(f"**Description:** {selected_ex['desc']}")
        st.write(f"**Domain:** {selected_ex['domain']}")
        st.write(f"**Range:** {selected_ex['range']}")
        st.write(f"**Expression:** `{selected_ex['expr']}`")

# Interactive Input Testing
st.header("🧮 Test Your Function")
if selected_ex:
    st.write(f"Try different inputs for the **{selected}** function:")
    
    # Get appropriate input range
    if selected == "Hourly Pay":
        test_input = st.slider("Hours worked:", 0, 40, 8)
    elif selected == "Spotify Streams":
        test_input = st.slider("Days:", 0, 10, 3)
    elif selected == "Uber Fare":
        test_input = st.slider("Miles traveled:", 0, 20, 5)
    elif selected == "Phone Battery":
        test_input = st.slider("Hours of use:", 0, 10, 3)
    elif selected == "Basketball Arc":
        test_input = st.slider("Horizontal distance (feet):", 0, 10, 5)
    elif selected == "YouTube Subscribers":
        test_input = st.slider("Weeks:", 0, 52, 12)
    elif selected == "Gym Progress":
        test_input = st.slider("Weeks of training:", 0, 52, 12)
    elif selected == "Bus Route Time":
        test_input = st.slider("Number of stops:", 0, 15, 5)
    elif selected == "Temperature Drop":
        test_input = st.slider("Hours after sunset:", 0, 20, 6)
    else:  # Water Bill
        test_input = st.slider("Hundreds of gallons:", 0, 50, 10)
    
    # Calculate and display result
    result = selected_ex["rule"](test_input)
    st.success(f"When x = {test_input}, f(x) = {result:.2f} {selected_ex['unit']}")

# Function Types Classification
st.header("🎯 Function Types in Action")

function_types = {
    "Linear Functions": {
        "examples": ["Hourly Pay", "Uber Fare", "YouTube Subscribers", "Bus Route Time", "Temperature Drop", "Water Bill"],
        "form": "f(x) = mx + b",
        "description": "Constant rate of change - creates straight lines"
    },
    "Exponential Functions": {
        "examples": ["Spotify Streams"],
        "form": "f(x) = a × b^x",
        "description": "Rapid growth or decay - creates curved lines"
    },
    "Quadratic Functions": {
        "examples": ["Basketball Arc"],
        "form": "f(x) = ax² + bx + c",
        "description": "Parabolic shape - has maximum or minimum point"
    },
    "Logarithmic Functions": {
        "examples": ["Gym Progress"],
        "form": "f(x) = a × log(x + b)",
        "description": "Rapid change initially, then levels off"
    }
}

type_selected = st.selectbox("Explore function types:", list(function_types.keys()))
type_info = function_types[type_selected]

st.write(f"**Form:** {type_info['form']}")
st.write(f"**Description:** {type_info['description']}")
st.write(f"**Examples from our list:** {', '.join(type_info['examples'])}")

# Quick Quiz Section
st.header("🎲 Quick Understanding Check")

quiz_questions = [
    {
        "question": "Which situation represents a linear function?",
        "options": ["Earning $15 per hour", "Viral video growth", "Basketball shot arc", "Gym strength gains"],
        "correct": 0,
        "explanation": "Linear functions have a constant rate of change - $15 per hour is constant!"
    },
    {
        "question": "What makes something a function?",
        "options": ["It has an x and y", "Each input has exactly one output", "It creates a curve", "It uses numbers"],
        "correct": 1,
        "explanation": "Functions must pass the vertical line test - each input (x) gives exactly one output (y)!"
    },
    {
        "question": "Which function type would model a bouncing ball's height?",
        "options": ["Linear", "Exponential", "Quadratic", "Logarithmic"],
        "correct": 2,
        "explanation": "Quadratic functions create parabolic shapes, perfect for projectile motion!"
    }
]

for i, q in enumerate(quiz_questions):
    st.write(f"**Question {i+1}:** {q['question']}")
    answer = st.radio(f"Select your answer for Q{i+1}:", q['options'], key=f"q{i}")
    
    if st.button(f"Check Answer {i+1}", key=f"check{i}"):
        if q['options'].index(answer) == q['correct']:
            st.success(f"✅ Correct! {q['explanation']}")
        else:
            st.error(f"❌ Try again! {q['explanation']}")

# Exit Reflection
st.header("🧾 Reflection")
reflection = st.text_area("What is one real-world situation you could model with a function? Describe the input, output, and what type of function it might be.")

if st.button("Submit Reflection"):
    if reflection.strip():
        st.success("✅ Excellent mathematical thinking! You're seeing functions everywhere now!")
        st.balloons()
    else:
        st.warning("Please share your thoughts to complete the reflection.")

# Final Summary
st.header("🎓 What You've Learned")
st.markdown("""
**Congratulations!** You've explored:
- ✅ **10 real-life functions** from jobs to sports to technology
- ✅ **4 different function types** and their characteristics  
- ✅ **Interactive testing** to see how inputs affect outputs
- ✅ **Visual representations** that make math come alive

**Remember:** Functions are everywhere in your daily life - from your paycheck to your phone battery to your favorite apps. Math isn't just numbers on a page - it's the language that describes how our world works!

Keep your **Panther Vision** sharp and you'll see functions everywhere! 🐾
""")

# IXL Integration Section
st.header("📚 IXL Practice & Related Lessons")

# IXL lessons organized by grade level and topic
ixl_lessons = {
    "Algebra 1": {
        "Function Basics": [
            "A.1 - Identify functions",
            "A.2 - Evaluate functions",
            "A.3 - Domain and range of functions",
            "A.5 - Graph a function",
            "A.6 - Find the slope of a graph"
        ],
        "Linear Functions": [
            "B.1 - Identify linear functions",
            "B.2 - Find the slope of a linear function",
            "B.3 - Graph a linear function",
            "B.4 - Write linear functions: word problems",
            "B.5 - Interpret the graph of a linear function"
        ],
        "Exponential Functions": [
            "P.1 - Identify exponential functions",
            "P.2 - Evaluate exponential functions",
            "P.3 - Graph exponential functions",
            "P.4 - Exponential growth and decay: word problems"
        ],
        "Quadratic Functions": [
            "Q.1 - Identify quadratic functions",
            "Q.2 - Evaluate quadratic functions",
            "Q.3 - Graph quadratic functions",
            "Q.4 - Solve quadratic equations by graphing"
        ]
    },
    "Algebra 2": {
        "Advanced Functions": [
            "A.1 - Domain and range of functions",
            "A.2 - Identify functions: graphs",
            "A.3 - Evaluate functions",
            "A.4 - Function transformation rules",
            "A.5 - Transformations of functions"
        ],
        "Polynomial Functions": [
            "B.1 - Polynomial vocabulary",
            "B.2 - Evaluate polynomials",
            "B.3 - Add and subtract polynomials",
            "B.4 - Graph polynomial functions"
        ],
        "Logarithmic Functions": [
            "M.1 - Convert between exponential and logarithmic form",
            "M.2 - Evaluate logarithms",
            "M.3 - Graph logarithmic functions",
            "M.4 - Domain and range of logarithmic functions"
        ]
    },
    "Precalculus": {
        "Function Analysis": [
            "A.1 - Function composition",
            "A.2 - Inverse functions",
            "A.3 - Even and odd functions",
            "A.4 - Domain and range of functions"
        ],
        "Trigonometric Functions": [
            "C.1 - Graph sine and cosine functions",
            "C.2 - Graph tangent and cotangent functions",
            "C.3 - Amplitude, period, and phase shift",
            "C.4 - Write equations of sine and cosine functions"
        ]
    }
}

# Let user select grade level for IXL recommendations
grade_level = st.selectbox("Select your grade level for IXL recommendations:", list(ixl_lessons.keys()))
selected_ixl = ixl_lessons[grade_level]

# Display IXL lessons in expandable sections
for topic, lessons in selected_ixl.items():
    with st.expander(f"📖 {topic} - IXL Lessons"):
        for lesson in lessons:
            st.write(f"• {lesson}")
        st.markdown(f"**🎯 Practice Tip:** Complete these lessons on IXL to master {topic.lower()} concepts!")

# Outside Resources Section
st.header("🌐 Additional Learning Resources")

# Categorized external resources
resources = {
    "📺 Video Tutorials": [
        {
            "name": "Khan Academy - Intro to Functions",
            "url": "https://www.khanacademy.org/math/algebra/x2f8bb11595b61c86:functions",
            "description": "Comprehensive video series on function basics, domain, range, and graphing"
        },
        {
            "name": "Professor Leonard - Function Fundamentals",
            "url": "https://www.youtube.com/watch?v=kvGsIo1TmsM",
            "description": "Clear, detailed explanations of function concepts with worked examples"
        },
        {
            "name": "3Blue1Brown - Essence of Calculus",
            "url": "https://www.youtube.com/playlist?list=PLZHQObOWTQDMsr9K-rj53DwVRMYO3t5Yr",
            "description": "Visual and intuitive approach to understanding functions and their behavior"
        }
    ],
    "💻 Interactive Tools": [
        {
            "name": "Desmos Graphing Calculator",
            "url": "https://www.desmos.com/calculator",
            "description": "Free online graphing tool to visualize functions and explore their properties"
        },
        {
            "name": "GeoGebra Functions",
            "url": "https://www.geogebra.org/m/x39ys4d7",
            "description": "Interactive function explorer with sliders and dynamic visualization"
        },
        {
            "name": "Wolfram Alpha",
            "url": "https://www.wolframalpha.com/",
            "description": "Computational engine for function analysis, graphing, and problem solving"
        }
    ],
    "📚 Study Guides & Practice": [
        {
            "name": "Paul's Online Math Notes",
            "url": "https://tutorial.math.lamar.edu/Classes/Alg/Functions.aspx",
            "description": "Comprehensive notes on functions with examples and practice problems"
        },
        {
            "name": "Purplemath - Functions",
            "url": "https://www.purplemath.com/modules/fcns.htm",
            "description": "Step-by-step tutorials on function concepts and problem-solving strategies"
        },
        {
            "name": "Mathway Function Solver",
            "url": "https://www.mathway.com/",
            "description": "Online problem solver for function-related homework and practice"
        }
    ],
    "🎮 Educational Games": [
        {
            "name": "Function Machine - Math Playground",
            "url": "https://www.mathplayground.com/functionmachine.html",
            "description": "Interactive game to practice identifying function rules and patterns"
        },
        {
            "name": "Algebra Tiles - National Library of Virtual Manipulatives",
            "url": "https://www.glencoe.com/sites/common_assets/mathematics/ebook_assets/vmf/VMF-Interface.html",
            "description": "Visual tool for understanding algebraic concepts and function building"
        }
    ],
    "📖 Reference Materials": [
        {
            "name": "Common Core State Standards - Functions",
            "url": "http://www.corestandards.org/Math/Content/HSF/",
            "description": "Official standards document outlining function learning objectives"
        },
        {
            "name": "NCTM - Functions Resource",
            "url": "https://www.nctm.org/",
            "description": "National Council of Teachers of Mathematics resources for function instruction"
        }
    ]
}

# Display resources in organized tabs
resource_tabs = st.tabs(list(resources.keys()))

for i, (category, items) in enumerate(resources.items()):
    with resource_tabs[i]:
        for item in items:
            st.markdown(f"**[{item['name']}]({item['url']})**")
            st.write(f"📝 {item['description']}")
            st.write("---")

# Study Plan Generator
st.header("📅 Personalized Study Plan")

# Get student's current level and goals
current_level = st.selectbox("What's your current comfort level with functions?", [
    "Beginner - Just starting to learn about functions",
    "Intermediate - Understand basics, need more practice",
    "Advanced - Ready for complex function types",
    "Expert - Looking for challenge problems"
])

study_time = st.selectbox("How much time can you dedicate to studying functions per week?", [
    "1-2 hours",
    "3-4 hours", 
    "5-6 hours",
    "7+ hours"
])

# Generate personalized recommendations
if st.button("Generate My Study Plan"):
    st.success("🎯 Your Personalized Function Mastery Plan:")
    
    if "Beginner" in current_level:
        st.markdown("""
        **Week 1-2: Foundation Building**
        - Watch Khan Academy's "Intro to Functions" videos
        - Complete IXL lessons A.1-A.3 (Function Basics)
        - Practice with Desmos graphing calculator daily
        
        **Week 3-4: Linear Functions**
        - Focus on IXL lessons B.1-B.5 (Linear Functions)
        - Use Function Machine game for pattern recognition
        - Complete reflection exercises in this app
        """)
    
    elif "Intermediate" in current_level:
        st.markdown("""
        **Week 1: Review & Strengthen**
        - Complete remaining IXL function basics lessons
        - Practice with interactive tools (GeoGebra)
        - Work through Paul's Online Math Notes
        
        **Week 2-3: Expand to New Function Types**
        - Study exponential and quadratic functions
        - Use Wolfram Alpha for complex graphing
        - Create your own real-world function examples
        """)
    
    elif "Advanced" in current_level:
        st.markdown("""
        **Week 1: Master Advanced Concepts**
        - Complete Algebra 2 IXL lessons
        - Study function transformations and composition
        - Explore 3Blue1Brown's visual approach
        
        **Week 2: Real-World Applications**
        - Research functions in your field of interest
        - Create presentations on function modeling
        - Challenge yourself with competition problems
        """)
    
    else:  # Expert
        st.markdown("""
        **Ongoing Challenge Plan:**
        - Complete Precalculus IXL lessons
        - Study advanced function theory
        - Mentor other students learning functions
        - Explore mathematical research involving functions
        """)
    
    # Time-based recommendations
    if study_time == "1-2 hours":
        st.info("💡 **Tip:** Focus on one concept per week with daily 15-minute practice sessions.")
    elif study_time == "3-4 hours":
        st.info("💡 **Tip:** Balance video learning (60%) with hands-on practice (40%).")
    elif study_time == "5-6 hours":
        st.info("💡 **Tip:** Add teaching others to solidify your understanding.")
    else:
        st.info("💡 **Tip:** Consider pursuing advanced topics like calculus or mathematical modeling.")

# Display selected strand alignment
st.info(f"📚 **Common Core Alignment:** {strand}")
