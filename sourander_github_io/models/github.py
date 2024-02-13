from dataclasses import dataclass

@dataclass
class Site:
    """Site
    
    A data class representing a GitHub Pages site.

    Parameters
    ----------
    namespace:
        the Github namespace of the repository
    name:
        the name of the repository
    url:
        the URL of the GitHub Pages site
    description:
        the GitHub repository's description
    category:
        the category of the site from siteinfo.json
    latest_commit:
        the latest commit (e.g. "2024-12-31T10:10:10Z")
    related_repo:
        the related repository Markdown one-liner
    """
    namespace: str
    name: str
    url: str
    description: str
    latest_commit: str = ""
    category: str = "Uncategorized"
    related_repo: str = ""

@dataclass
class Category:
    """Category 
    Category 
    
    A data class representing a category of GitHub Pages sites.
    
    Parameters
    ----------
    name:
        name of the category
    sites:
        list of Sites in the category
    """
    name: str
    sites: list[Site]