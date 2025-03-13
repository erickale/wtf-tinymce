# WTF-TinyMCE Example

This is a simple example Flask application demonstrating how to use the WTF-TinyMCE package.

## Setup

1. Install the required packages:

```bash
pip install flask flask-wtf wtf-tinymce
```

2. Run the application:

```bash
python app.py
```

3. Open your browser and navigate to http://127.0.0.1:5000/

## Features Demonstrated

- Basic TinyMCE integration with Flask-WTF
- Custom TinyMCE configuration
- Form submission and display of rich text content
- Focus/blur styling for the editor

## File Structure

- `app.py` - The Flask application
- `templates/index.html` - The HTML template with TinyMCE integration

## Notes

- This example uses Bootstrap 5 for styling
- The TinyMCE editor is initialized in the template using the `init_wtf_tinymce` macro
- The submitted content is displayed with the `safe` filter to render the HTML
