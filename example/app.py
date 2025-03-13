#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Example Flask application demonstrating wtf-tinymce usage.
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
    content = TinyMceField('Content', 
                          tinymce_options={
                              'height': 300,
                              'toolbar': 'undo redo | styles | bold italic | alignleft aligncenter alignright | bullist numlist | link image | code',
                              'plugins': 'link image code lists'
                          })
    submit = SubmitField('Submit')

@app.route('/', methods=['GET', 'POST'])
def index():
    form = ExampleForm()
    submitted_content = None
    
    if form.validate_on_submit():
        submitted_content = form.content.data
        flash('Form submitted successfully!')
        
    return render_template('index.html', form=form, submitted_content=submitted_content)

if __name__ == '__main__':
    app.run(debug=True) 