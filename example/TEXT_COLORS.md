# Using Text Colors in TinyMCE 6.x

In TinyMCE 6.x, the way text colors are handled has changed from previous versions. This document explains how to properly configure text colors in your WTF-TinyMCE forms.

## Changes from TinyMCE 4.x to 6.x

1. **Plugin Integration**: The `textcolor` plugin is now integrated into the core in TinyMCE 6.x. You no longer need to include it as a separate plugin.

2. **Toolbar Buttons**: The text color buttons are now simply `forecolor` and `backcolor`.

3. **Color Configuration**: Colors are now configured using the `color_map` option.

## Example Configuration

```python
from wtf_tinymce.forms.fields import TinyMceField

welcome_text = TinyMceField(
    "Company Welcome Text",
    tinymce_options={
        # No need to include textcolor in plugins
        "plugins": "link code lists",
        # Include forecolor and backcolor in toolbar
        "toolbar": "formatselect | bold italic | forecolor backcolor | link | code",
        # Define color options
        "color_map": [
            "#000000", "Black",
            "#FFFFFF", "White",
            "#FF0000", "Red",
            "#00FF00", "Green",
            "#0000FF", "Blue"
        ]
    }
)
```

## Multiple Toolbar Rows

If you want to organize your toolbar into multiple rows, use the newline character `\n`:

```python
"toolbar": "formatselect fontselect fontsizeselect\n" +
           "bold italic underline | forecolor backcolor\n" +
           "alignleft aligncenter alignright | bullist numlist | link | code"
```

## Custom Color Picker

To enable the custom color picker, add the `color_picker` option:

```python
"color_picker": True
```

## Color Categories

You can organize colors into categories:

```python
"color_map_foreground": [
    {"title": "Basic", "items": [
        {"text": "Black", "value": "#000000"},
        {"text": "White", "value": "#FFFFFF"}
    ]},
    {"title": "Brand", "items": [
        {"text": "Primary", "value": "#0066CC"},
        {"text": "Secondary", "value": "#FF9900"}
    ]}
]
```

## Troubleshooting

If you see errors like:

```
GET http://127.0.0.1:5000/_wtf_tinymce/vendor/tinymce/js/tinymce/plugins/textcolor/plugin.min.js 404 (NOT FOUND)
```

This is because TinyMCE is trying to load the old textcolor plugin. Make sure you:

1. Remove `textcolor` from your plugins list
2. Use the updated toolbar configuration with `forecolor` and `backcolor`
3. Use `color_map` to define your colors

## Further Reading

For more information, see the [TinyMCE 6 documentation on text colors](https://www.tiny.cloud/docs/tinymce/6/user-formatting-options/#text-color).
