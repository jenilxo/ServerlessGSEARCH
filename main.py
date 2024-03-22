import os
import logging

import requests
from bs4 import BeautifulSoup

log = logging.getLogger("func")

def main(request):
    log.info("Processing request...")

    keyword = request["query"]["keyword"]
    log.debug(f"Keyword: {keyword}")

    try:
        # Perform a Google search and return the first result link
        search_results = search(keyword, num_results=1)
        for result in search_results:
            return {"result": {"link": result}}

    except Exception as e:
        message = f"Error processing request: {str(e)}"
        log.error(message)
        return {"error": message}, 500
