import streamlit as st
import pandas as pd
import numpy as np

# Page configuration
st.set_page_config(
    page_title="Streamlit Basics",
    page_icon=":rocket:",
    layout="wide"
)

# Title and Introduction
st.title("Streamlit Basics - Complete Guide")
st.write("Welcome to your first Streamlit application!")

st.markdown("---")

# Section 1: Display Text
st.header("1. Display Text")
st.subheader("Different ways to display text")
st.text("This is plain text")
st.write("This is using st.write() - most versatile")
st.markdown("**This is markdown** with *formatting*")
st.caption("This is a caption - smaller text")

st.markdown("---")

# Section 2: Text Input Widget
st.header("2. Text Input Widget")
name = st.text_input("Enter your name:", placeholder="Type your name here...")
if name:
    st.success(f"Hello, {name}! Welcome to Streamlit!")

email = st.text_input("Enter your email:", type="default")
password = st.text_input("Enter password:", type="password")

text_area = st.text_area("Enter a message:", placeholder="Type your message here...")
if text_area:
    st.info(f"Your message: {text_area}")

st.markdown("---")

# Section 3: Buttons
st.header("3. Buttons")
col1, col2, col3 = st.columns(3)

with col1:
    if st.button("Click Me!"):
        st.balloons()
        st.success("Button clicked!")

with col2:
    if st.button("Show Warning"):
        st.warning("This is a warning message!")

with col3:
    if st.button("Show Error"):
        st.error("This is an error message!")

st.markdown("---")

# Section 4: Sliders
st.header("4. Sliders")

age = st.slider("Select your age:", min_value=0, max_value=100, value=25, step=1)
st.write(f"Your age is: {age}")

price_range = st.slider(
    "Select price range:",
    min_value=0.0,
    max_value=1000.0,
    value=(100.0, 500.0),
    step=10.0
)
st.write(f"Selected price range: ${price_range[0]} - ${price_range[1]}")

rating = st.select_slider(
    "Rate your experience:",
    options=["Poor", "Fair", "Good", "Very Good", "Excellent"]
)
st.write(f"Your rating: {rating}")

st.markdown("---")

# Section 5: Display Data
st.header("5. Display Data")

# Create sample dataframe
data = {
    'Name': ['John', 'Emma', 'Michael', 'Sophia', 'William'],
    'Age': [28, 34, 45, 29, 38],
    'City': ['New York', 'London', 'Paris', 'Tokyo', 'Sydney'],
    'Salary': [75000, 85000, 95000, 70000, 90000]
}
df = pd.DataFrame(data)

st.subheader("DataFrame Display")
st.dataframe(df, use_container_width=True)

st.subheader("Static Table")
st.table(df.head(3))

st.subheader("Metrics")
col1, col2, col3 = st.columns(3)
col1.metric("Total Employees", len(df), delta="5")
col2.metric("Average Age", f"{df['Age'].mean():.1f}", delta="-2")
col3.metric("Average Salary", f"${df['Salary'].mean():,.0f}", delta="5000")

st.markdown("---")

# Section 6: Charts
st.header("6. Simple Charts")

chart_data = pd.DataFrame(
    np.random.randn(20, 3),
    columns=['A', 'B', 'C']
)

st.subheader("Line Chart")
st.line_chart(chart_data)

st.subheader("Area Chart")
st.area_chart(chart_data)

st.subheader("Bar Chart")
st.bar_chart(chart_data)

st.markdown("---")

# Section 7: More Widgets
st.header("7. Additional Widgets")

col1, col2 = st.columns(2)

with col1:
    st.subheader("Checkbox")
    agree = st.checkbox("I agree to terms and conditions")
    if agree:
        st.success("Thank you for agreeing!")
    
    st.subheader("Radio Buttons")
    genre = st.radio(
        "Choose your favorite genre:",
        ["Comedy", "Drama", "Action", "Sci-Fi"]
    )
    st.write(f"You selected: {genre}")

with col2:
    st.subheader("Select Box")
    option = st.selectbox(
        "Choose a programming language:",
        ["Python", "JavaScript", "Java", "C++", "Go"]
    )
    st.write(f"You selected: {option}")
    
    st.subheader("Multi-select")
    options = st.multiselect(
        "Choose your skills:",
        ["Python", "Machine Learning", "Data Analysis", "Web Development", "Cloud Computing"],
        default=["Python"]
    )
    st.write(f"Selected skills: {', '.join(options)}")

st.markdown("---")

# Section 8: File Uploader
st.header("8. File Upload")
uploaded_file = st.file_uploader("Choose a CSV file", type="csv")
if uploaded_file is not None:
    df_uploaded = pd.read_csv(uploaded_file)
    st.write("Uploaded Data:")
    st.dataframe(df_uploaded)

st.markdown("---")

# Section 9: Progress and Status
st.header("9. Progress and Status")

if st.button("Show Progress"):
    import time
    progress_bar = st.progress(0)
    status_text = st.empty()
    
    for i in range(100):
        progress_bar.progress(i + 1)
        status_text.text(f"Progress: {i + 1}%")
        time.sleep(0.01)
    
    st.success("Complete!")

st.markdown("---")

# Sidebar
st.sidebar.title("Sidebar Navigation")
st.sidebar.write("This is the sidebar")
sidebar_option = st.sidebar.selectbox(
    "Choose a section:",
    ["Home", "About", "Contact"]
)
st.sidebar.info(f"Current section: {sidebar_option}")

# Footer
st.markdown("---")
st.markdown("### Thank you for exploring Streamlit Basics!")
st.markdown("Run this app with: `streamlit run app.py`")
