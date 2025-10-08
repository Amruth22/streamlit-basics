import unittest
from streamlit.testing.v1 import AppTest


class TestStreamlitApp(unittest.TestCase):
    """Unit tests for Streamlit Basics App"""

    def setUp(self):
        """Set up test app before each test"""
        self.at = AppTest.from_file("app.py")
        self.at.run()

    def test_app_loads_successfully(self):
        """Test 1: Verify the app loads without errors"""
        self.assertFalse(self.at.exception, "App should load without exceptions")
        self.assertTrue(len(self.at.title) > 0, "App should have a title")
        self.assertEqual(self.at.title[0].value, "Streamlit Basics - Complete Guide")

    def test_text_input_widgets(self):
        """Test 2: Verify text input widgets work correctly"""
        # Check if text input exists
        self.assertTrue(len(self.at.text_input) > 0, "App should have text input widgets")
        
        # Simulate entering a name
        self.at.text_input[0].set_value("John Doe")
        self.at.run()
        
        # Check if success message appears
        success_messages = [s.value for s in self.at.success]
        self.assertTrue(any("John Doe" in msg for msg in success_messages), 
                       "Success message should contain the entered name")

    def test_button_functionality(self):
        """Test 3: Verify buttons trigger actions"""
        # Get initial button count
        initial_buttons = len(self.at.button)
        self.assertTrue(initial_buttons >= 3, "App should have at least 3 buttons")
        
        # Click the first button
        self.at.button[0].click()
        self.at.run()
        
        # Verify success message appears after button click
        self.assertTrue(len(self.at.success) > 0, "Button click should trigger success message")

    def test_slider_widgets(self):
        """Test 4: Verify slider widgets exist and work"""
        # Check if sliders exist
        self.assertTrue(len(self.at.slider) >= 2, "App should have at least 2 sliders")
        
        # Set slider value
        self.at.slider[0].set_value(30)
        self.at.run()
        
        # Verify slider value is set
        self.assertEqual(self.at.slider[0].value, 30, "Slider value should be 30")

    def test_dataframe_display(self):
        """Test 5: Verify data display functionality"""
        # Check if dataframe exists
        self.assertTrue(len(self.at.dataframe) > 0, "App should display at least one dataframe")
        
        # Verify dataframe has data
        df = self.at.dataframe[0].value
        self.assertIsNotNone(df, "DataFrame should not be None")
        self.assertTrue(len(df) > 0, "DataFrame should have rows")
        self.assertTrue(len(df.columns) > 0, "DataFrame should have columns")
        
        # Check expected columns
        expected_columns = ['Name', 'Age', 'City', 'Salary']
        for col in expected_columns:
            self.assertIn(col, df.columns, f"DataFrame should have '{col}' column")


if __name__ == "__main__":
    unittest.main()
