import os, sys
import requests
from typing import List
from urllib.parse import urljoin, urlparse
from bs4 import BeautifulSoup, SoupStrainer


def scrape_site(URL: str, visited: List[str] = []):
    """
    Given a url and a list of already visited urls, does a depth first search of all
    URLs given.

    Args:
        URL (str): URL String to parse for links.
        visited (List[str]): The list of visited URLs to ignore. Defaults to []. 

    Returns:
        visited (List[str]): The list of already visited URLs.

    """
    if URL in visited:
        return visited
    page = requests.get(URL)

    if page.status_code != 200:
        return visited

    domain = urlparse(URL).netloc

    visited.append(URL)

    for link in BeautifulSoup(
        page.content, "html.parser", parse_only=SoupStrainer("a")
    ):
        if (
            link.has_attr("href")
            and ("http" not in link["href"])
            and ("mailto" not in link["href"])
            and (link["href"] not in visited)
        ):
            link_href = link["href"].split("#")[0]
            to_visit = urljoin(URL, link_href)
            visited = scrape_site(to_visit, visited)

    return visited
