import requests

from sourander_github_io.models.github import Site, Category
from pathlib import Path
from jinja2 import Environment, FileSystemLoader
from sourander_github_io.auth import HEADERS
from urllib.parse import urlparse

def has_path(url):
    parsed_url = urlparse(url)
    return bool(parsed_url.path.strip("/"))

def fetch_sites(namespace="sourander") -> list[Site]:
    # Fetch the repositories from the API
    response = requests.get(f"https://api.github.com/users/{namespace}/repos", headers=HEADERS)
    repositories = response.json()

    # Filter
    filtered_repositories = []
    for repo in repositories:
        homepage = repo.get("homepage", "")

        # Drop private repositories
        if repo["private"]:
            continue

        # Drop those that have no homepage set
        if not homepage:
            continue

        # Drop non-GitHub Pages sites
        if "github.io" not in homepage:
            continue

        # Drop the main site
        if not has_path(homepage):
            continue

        filtered_repositories.append(repo)

    assert len(filtered_repositories), "No GitHub Pages repositories found!"

    # Create the sites list
    sites = [
        Site(
            namespace=namespace,
            name=repo["name"],
            url=repo["homepage"],
            description=repo["description"]
        ) for repo in filtered_repositories
    ]
    return sites

def enrich_commit_info(sites: list[Site], namespace="sourander") -> list[Site]:
    # Enrich the sites with the latest commit date
    for site in sites:
        response = requests.get(f"https://api.github.com/repos/{namespace}/{site.name}/commits", headers=HEADERS)
        commits = response.json()

        if len(commits) > 0:
            raw_commit_time = commits[0]["commit"]["author"]["date"]
            parsed_commit_time = raw_commit_time.split("T")[0]
            site.latest_commit = parsed_commit_time

    return sites

def enrich_json_info(sites: list[Site], namespace="sourander") -> list[Site]:
    # Enrich the sites with the latest commit date
    for site in sites:
        response = requests.get(f"https://raw.githubusercontent.com/{namespace}/{site.name}/master/siteinfo.json")
        
        try:
            data = response.json()
            if data.get("category"):
                site.category = data["category"].capitalize() # Force to "Lorem ipsum" case
            if data.get("related_repo"):
                site.related_repo = data["related_repo"]
        except:
            continue

    return sites

def group_sites_by_category(sites: list[Site]) -> list[Category]:
    
    # Group the sites by category into as dictionary.
    categories: dict[str, list[Site]] = {}
    for site in sites:
        if site.category not in categories:
            categories[site.category] = []

        categories[site.category].append(site)

    # Add the categories to a list and sort by newest commit
    cats: list[Category] = []
    for category in sorted(categories):
        sites = categories[category]
        sites_ordered = sorted(sites, key=lambda x: x.latest_commit, reverse=True)
        cat = Category(name=category, sites=sites_ordered)
        cats.append(cat)

    return cats

def write_index():

    # Load the Jinja2 template
    env = Environment(loader=FileSystemLoader('templates/'))
    template = env.get_template('index.template.md')

    # Render the template with the provided data
    sites = fetch_sites()
    sites = enrich_commit_info(sites)
    sites = enrich_json_info(sites)
    categories = group_sites_by_category(sites)
    output = template.render(categories=categories)

    output_file = Path("docs/index.md")
    output_file.write_text(output)
