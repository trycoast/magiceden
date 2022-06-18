import requests
from ratelimit import ratelimit
from tenacity import retry, stop_after_attempt, wait_fixed


cache = {}


@retry(stop=stop_after_attempt(2), wait=wait_fixed(5))
@ratelimit(burst=1, duration=2, sleep=True)
def fetch(query: str) -> dict:
    """ Fetch data from the API.

    Args:
        endpoint (str): The endpoint to fetch from.
        query (str): The query to fetch.

    Returns:
        dict: The data.
    """
    host = 'https://api-mainnet.magiceden.dev/v2'
    return requests.get(f'{host}/{query}').json()


def get_collections(offset: int) -> dict:
    """ Get collections metadata

    Args:
        offset (int): Offset to start from.

    Returns:
        dict: The collections metadata.
    """
    return fetch(f'collections?offset={offset}&limit=500')


def get_token_meta(token: str) -> dict:
    """ Get token metadata

    Args:
        token (str): The token (mint) to get metadata for.

    Returns:
        dict: The token metadata.
    """
    if token not in cache:
        cache[token] = fetch(f'tokens/{token}')
    return cache[token]


def get_collection_listings(collection: str) -> dict:
    """ Get collection listings

    Args:
        collection (str): The collection to get listings for.

    Returns:
        dict: The collection listings.
    """
    offset = 0
    listings = []
    while result := fetch(f'collections/{collection}/listings?offset={offset}&limit=20'):
        listings.extend(result)
        offset += 20

    return listings
