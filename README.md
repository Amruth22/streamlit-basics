# Streamlit Basics

A complete Streamlit application demonstrating basic widgets, text display, data visualization, and interactive components.

## Installation

1. Clone this repository:
```bash
git clone https://github.com/Amruth22/streamlit-basics.git
cd streamlit-basics
```

2. Install dependencies:
```bash
pip install -r requirements.txt
```

## Running the App

Run the Streamlit application:
```bash
streamlit run app.py
```

The app will open automatically in your browser at `http://localhost:8501`

## Running Tests

Run the unit tests:
```bash
python tests.py
```

Or using pytest:
```bash
pytest tests.py -v
```

## Features Included

- **Text Display**: Titles, headers, markdown, captions
- **Text Input**: Text fields, text areas, password fields
- **Buttons**: Interactive buttons with actions
- **Sliders**: Single value, range, and select sliders
- **Data Display**: DataFrames, tables, and metrics
- **Charts**: Line, area, and bar charts
- **Widgets**: Checkboxes, radio buttons, select boxes, multi-select
- **File Upload**: CSV file upload and display
- **Progress Bars**: Progress indicators and status updates
- **Sidebar**: Navigation and additional controls

## Requirements

- Python 3.8+
- Streamlit 1.29.0
- Pandas 2.1.4
- NumPy 1.26.2
- Pytest 7.4.3 (for testing)

## Project Structure

```
streamlit-basics/
├── app.py              # Main Streamlit application
├── tests.py            # Unit tests
├── requirements.txt    # Python dependencies
└── README.md          # This file
```

## Learn More

- [Streamlit Documentation](https://docs.streamlit.io)
- [Streamlit Gallery](https://streamlit.io/gallery)
