from jinja2 import Template

#TODO load template from files
template_string = """
# {{ notebook.bookTitle }}
Author: {{ notebook.author }}
{% for section in notebook.sections %}
## {{ section.title }}
    {% for chapter in section.chapters %}
### {{ chapter }}
        {% for note in section.chapters[chapter] %}
> {{ note.text }}
        {% endfor %}
    {% endfor %}
{% endfor %}
"""

def render_md_from_notebook(notebook):
    template = Template(template_string, trim_blocks=True,lstrip_blocks=True)

    return template.render(notebook=notebook)

