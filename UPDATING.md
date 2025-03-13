# Updating to WTF-TinyMCE 0.2.0

This guide will help you update from an older version of WTF-TinyMCE to version 0.2.0, which includes TinyMCE 6.8.3.

## Major Changes

1. **TinyMCE Version**: Updated from TinyMCE 4.x to TinyMCE 6.8.3
2. **jQuery Dependency**: Removed jQuery dependency
3. **Python Requirements**: Now requires Python 3.7+ and Flask 2.0.0+
4. **Modern Packaging**: Added pyproject.toml for modern Python packaging

## Update Steps

1. **Update the Package**:

   ```bash
   pip install --upgrade wtf-tinymce
   ```

2. **Update TinyMCE Options**:

   - Change `styleselect` to `styles` in toolbar options
   - Review the [TinyMCE 6 documentation](https://www.tiny.cloud/docs/tinymce/6/) for other API changes

3. **jQuery Removal**:
   - The package no longer requires jQuery
   - If your templates were using jQuery specifically for TinyMCE, you may need to update them

## Example Configuration

```python
from wtf_tinymce.forms.fields import TinyMceField

class MyForm(Form):
    content = TinyMceField(
        'Content',
        tinymce_options={
            'plugins': 'autolink link lists paste searchreplace code table image',
            'toolbar': 'undo redo | styles | bold italic | alignleft aligncenter alignright | bullist numlist | link image | code',
            'height': 400
        }
    )
```

## Template Usage

```html
{% import 'wtf_tinymce/editor.html' as tinymce with context %} {% block content
%}
<form method="POST">
  {{ form.csrf_token }} {{ form.content.label }} {{ form.content }}
  <button type="submit">Submit</button>
</form>
{% endblock %} {% block scripts %} {{ tinymce.init_wtf_tinymce() }} {% endblock
%}
```

## Additional Resources

- See the `example` directory for a complete working example
- Check the [TinyMCE 6 Migration Guide](https://www.tiny.cloud/docs/tinymce/6/migration-from-5x/) for details on migrating from TinyMCE 5.x to 6.x
- Review the [TinyMCE 6 documentation](https://www.tiny.cloud/docs/tinymce/6/) for all available options
