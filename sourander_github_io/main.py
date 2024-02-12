import requests

from pathlib import Path
from jinja2 import Environment, FileSystemLoader

from sourander_github_io.models.github import Site

# Fetch the repositories from the API
response = requests.get("https://api.github.com/users/sourander/repos")
repositories = response.json()

# Filter repositories with non-null homepage
filtered_repositories = [r for r in repositories if r["homepage"] is not None]
filtered_repositories = [x for x in filtered_repositories if "github.io" in x.get("homepage", "")]

# Create the sites list
sites = [Site(name=repo["name"], description=repo["description"]) for repo in filtered_repositories]

# Load the Jinja2 template
env = Environment(loader=FileSystemLoader('templates/'))
template = env.get_template('index.template.md')

# Render the template with the provided data
output = template.render(sites=sites)

output_file = Path("docs/index.md")
output_file.write_text(output)
