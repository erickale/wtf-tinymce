#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Example Flask application demonstrating wtf-tinymce usage with text colors.
"""

from flask import Flask, render_template, redirect, url_for, flash
from flask_wtf import FlaskForm
from wtforms import SubmitField
from wtf_tinymce.forms.fields import TinyMceField

# Create Flask application
app = Flask(__name__)
app.config['SECRET_KEY'] = 'your-secret-key'  # Change this in production!

# Initialize wtf_tinymce
from wtf_tinymce import wtf_tinymce
wtf_tinymce.init_app(app)

# Create a form with TinyMCE field
class ExampleForm(FlaskForm):
    welcome_text = TinyMceField(
        "Company Welcome Text",
        tinymce_options={
            "block_formats": "Paragraph=p;Header 1=h1;Header 2=h2;Header 3=h3",
            # Note: textcolor is now integrated into the core in TinyMCE 6.x
            "plugins": "link code lists",
            # Use a single toolbar property with pipe characters to separate groups
            "toolbar": "formatselect fontselect fontsizeselect | bold italic underline | forecolor backcolor | alignleft aligncenter alignright alignjustify | bullist numlist | link | code",
            # Define color options
            "color_map": [
                "#BFEDD2", "Light Green",
                "#FBEEB8", "Light Yellow",
                "#F8CAC6", "Light Red",
                "#ECCAFA", "Light Purple",
                "#C2E0F4", "Light Blue",
                "#2DC26B", "Green",
                "#F1C40F", "Yellow",
                "#E03E2D", "Red",
                "#B96AD9", "Purple",
                "#3598DB", "Blue",
                "#169179", "Dark Green",
                "#E67E23", "Orange",
                "#BA372A", "Dark Red",
                "#843FA1", "Dark Purple",
                "#236FA1", "Dark Blue",
                "#000000", "Black",
                "#525252", "Dark Gray",
                "#737373", "Gray",
                "#A6A6A6", "Light Gray",
                "#FFFFFF", "White"
            ]
        }
    )
    submit = SubmitField('Submit')

@app.route('/', methods=['GET', 'POST'])
def index():
    form = ExampleForm()
    submitted_content = None
    
    if form.validate_on_submit():
        submitted_content = form.welcome_text.data
        flash('Form submitted successfully!')
        
    return render_template('color_example.html', form=form, submitted_content=submitted_content)

if __name__ == '__main__':
    app.run(debug=True) 