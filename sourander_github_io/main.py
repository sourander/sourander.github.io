import requests

from sourander_github_io.models.github import Site
from pathlib import Path
from jinja2 import Environment, FileSystemLoader

def fetch_sites(namespace="sourander") -> list[Site]:
    # Fetch the repositories from the API
    response = requests.get(f"https://api.github.com/users/{namespace}/repos")
    repositories = response.json()

    # Filter repositories with non-null homepage
    filtered_repositories = [r for r in repositories if r["homepage"] is not None]
    filtered_repositories = [x for x in filtered_repositories if "github.io" in x.get("homepage", "")]

    assert len(filtered_repositories), "No GitHub Pages repositories found!"

    # Create the sites list
    return [Site(name=repo["name"], description=repo["description"]) for repo in filtered_repositories]


def write_index():
    # Load the Jinja2 template
    env = Environment(loader=FileSystemLoader('templates/'))
    template = env.get_template('index.template.md')

    # Render the template with the provided data
    sites = fetch_sites()
    output = template.render(sites=sites)

    output_file = Path("docs/index.md")
    output_file.write_text(output)

if __name__ == "__main__":
    write_index()
