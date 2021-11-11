from typing import List

from mkdocs.structure.pages import Page
from mkdocs.structure.toc import AnchorLink
from mkdocs.utils import normalize_url

import logging

_LOGGER = logging.getLogger("mkdocs.plugins." + __name__)

_KEY = "{childrenWithSubtitle}"


def insert_children_with_subtitle(output, page: Page, config):
    if _KEY in output:
        if not page.parent:
            _LOGGER.warning("Page has no parent. Stopping!")
            return output

        children: List[Page] = [child for child in page.parent.children if child is not page]
        return output.replace(_KEY, _format_links(children, page))


def _format_links(items: List[Page], page: Page):
    result = "<ul>"

    for item in items:
        if item.title == "General" or not item.toc:
            continue

        result += f"<li>{item.title}<ul>"

        entry: AnchorLink
        for entry in item.toc.items[0].children:
            url = normalize_url(item.url, page)
            result += f"<li><a href=\"{url}\">{entry.title}</a></li>"

        result += "</ul></li>"

    result += "</ul>"
    return result
