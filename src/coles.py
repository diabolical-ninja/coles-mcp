import httpx


class ColesAPI:
    """
    A client for interacting with the Coles API.
    """

    BASE_URL = (
        "https://www.coles.com.au/_next/data/20250910.2-94eac02bf9675b685ea17b771023fada9319d0f3/en"
    )
    HEADERS = {
        "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/140.0.0.0 Safari/537.36",
        "sec-ch-ua-mobile": "?0",
        "dnt": "1",
        "sec-gpc": "1",
        "host": "www.coles.com.au",
        "Cookie": "nlbi_2800108_2670698=eK1eTTOFWQ5ga6VN5VPXvwAAAADAWbN30w6YenVSjiyT1yNn; ad-memory-token=bpzUzdkGYykaHLw%2FkcasWYS8FGkKDhIMCJy0kMYGEL6Oxp0BGgIIAiIA; dsch-sessionid=2f01a06f-cfae-45da-9059-477e31d2795b; dsch-visitorid=19a60b31-5772-49e6-a031-462b8e13e523; incap_ses_780_2800108=7bE/PQLn62lq6nEj7B3TCncWxGgAAAAAfgLwDLAmasYB5Q8ZdJdgXQ==; incap_sh_2800108=ExnEaAAAAABvvjlfBgAQk7KQxga99J8C8ymVoWG356I24mny; nlbi_2800108_3037207=7ULDKZQL+xxn20to5VPXvwAAAADz8QV5hTWJIC0e02OKHSZ8; visid_incap_2800108=UQk4pjSyQZqkRJscYvIaKjEWxGgAAAAAQUIPAAAAAACthheWIf1k0Tc3UffNkMYZ",
    }

    def __init__(self, timeout: float = 10.0):
        """
        Initialize the ColesAPI client.

        Args:
            timeout (float): The timeout for HTTP requests in seconds.
        """
        self.timeout = timeout

    def fetch_product_data(self, query: str) -> dict:
        """
        Fetch product data from Coles API based on the query.

        Args:
            query (str): The search query for the product.

        Returns:
            dict: The JSON response from the API.

        Raises:
            ValueError: If the query is empty.
            httpx.RequestError: If there is an issue with the HTTP request.
            httpx.HTTPStatusError: If the response status code is not 200.
        """
        if not query:
            raise ValueError("The query must not be empty.")

        url = f"{self.BASE_URL}/search/products.json?q={query}"

        return self._make_request(url)

    def fetch_product_details(self, product_slug: str) -> dict:
        """
        Fetch detailed product information from Coles API based on the product slug. This includes nutritional information, ingredients, and other details.

        Args:
            product_slug (str): The slug of the product.

        Returns:
            dict: The response JSON from the API.

        Raises:
            ValueError: If the product slug is empty.
            httpx.RequestError: If there is an issue with the HTTP request.
            httpx.HTTPStatusError: If the response status code is not 200.
        """
        if not product_slug:
            raise ValueError("The product slug must not be empty.")

        url = f"{self.BASE_URL}/product/{product_slug}.json?slug={product_slug}"

        return self._make_request(url)

    @staticmethod
    def create_product_slug(brand: str, name: str, size: str, product_id: str) -> str:
        """
        Create a product URL slug.

        Args:
            brand (str): The brand of the product.
            name (str): The name of the product.
            size (str): The size of the product.
            product_id (str): The ID of the product.

        Returns:
            str: The generated product slug in the format `{brand}-{name}-{size}-{id}`.
        """
        slug = f"{brand}-{name}-{size}-{product_id}"
        slug = slug.lower().replace(" ", "-")
        return slug

    def _make_request(self, url: str, return_json: bool = True):
        """
        Make an HTTP GET request to the given URL.

        Args:
            url (str): The URL to request.
            return_json (bool): Whether to return the response as JSON.

        Returns:
            dict or str: The response data.

        Raises:
            httpx.RequestError: If there is an issue with the HTTP request.
            httpx.HTTPStatusError: If the response status code is not 200.
        """
        try:
            response = httpx.get(url, headers=self.HEADERS, timeout=self.timeout)
            response.raise_for_status()
            return response.json() if return_json else response.text
        except httpx.RequestError as exc:
            raise httpx.RequestError(
                f"An error occurred while requesting {exc.request.url!r}."
            ) from exc
        except httpx.HTTPStatusError as exc:
            raise httpx.HTTPStatusError(
                f"Error response {exc.response.status_code} while requesting {exc.request.url!r}."
            ) from exc
