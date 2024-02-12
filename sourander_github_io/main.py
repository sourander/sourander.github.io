from pathlib import Path
from jinja2 import Environment, FileSystemLoader

from sourander_github_io.models.github import Site

sites = [
    Site(name="oat", description="Oppimispäiväkirja 101"),
    Site(name="linux-perusteet", description="Linux Perusteet -lukumateriaali."),
    Site(name="python-perusteet", description="Python Perusteet -lukumateriaali.")
]

# Load the Jinja2 template from the file system
env = Environment(loader=FileSystemLoader('templates/'))
template = env.get_template('index.template.md')

# Render the template with the provided data
output = template.render(sites=sites)

output_file = Path("docs/index.md")
output_file.write_text(output)
