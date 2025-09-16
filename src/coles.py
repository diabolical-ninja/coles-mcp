import httpx


class ColesAPI:
    """
    A client for interacting with the Coles API.
    """

    BASE_URL = (
        "https://www.coles.com.au/_next/data/20250916.2-6e5279cb065214e15253b3ec472b8c75953deabd/en"
    )
    HEADERS = {
        "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/140.0.0.0 Safari/537.36",
        "sec-ch-ua-mobile": "?0",
        "dnt": "1",
        "sec-gpc": "1",
        "host": "www.coles.com.au",
        "Cookie": "nlbi_2800108_2670698=8eeAAmtU1jS7Jg8E5VPXvwAAAAArOJwZbFRa3tpBgKOJj4v5; nlbi_2800108_2147483392=v/aTEmGCXXmDaESg5VPXvwAAAAB1Ex3Yi6pdUAu3knJOqP6Z; sessionId=848b8ece-7f1e-4b53-ba50-c5d4b55f2bb7; nlbi_2800108_3037207=0dsnA9iWsReS1h5i5VPXvwAAAAD1Jj2u6DO3raLA0DxPerv3; dsch-searchid=f3dc7e95-93c2-4f82-944f-e4ef4d6d0b43; customer-channel=CsXPhXz6wX94JtGkpXVgN1mnO9pFJwlApegU12Po/Ak=; x-jsession-id=00005Nskv8zKyfYt6s4cTDrI70T:1ed8ae100; colesIdBarcode=2753499553981; sortOptionPreference=priceAscending; visid_incap_2800108=qKtA0+47Sz+MzXmoen59FC5NyWgAAAAAQUIPAAAAAABVQw5qz51KtNlu0jYlX1vH; incap_ses_780_2800108=6rY3Pn4sSxGJ/Wpf7h3TCi5NyWgAAAAAZ03H0U7TRHCiamCIDPBekQ==; AMCV_0B3D037254C7DE490A4C98A6%40AdobeOrg=179643557%7CMCIDTS%7C20347%7CMCMID%7C53290601075226421873442998385050145914%7CMCAID%7CNONE%7CMCOPTOUT-1758030158s%7CNONE%7CvVersion%7C5.5.0; AMCVS_0B3D037254C7DE490A4C98A6%40AdobeOrg=1; reese84=3:FkgM+JTk+LAuvxnip+RsjQ==:iRY6KktgVyNDHkCB01cGx605SQ7SRMoF+wxs07VbZJbetLL4cV7HUlz7Sr10sG4QrtJSUWxWlz0fAQCHsBYB2gGtMRbVZuZbS2h4q+g/J0VxAg7PXedBccLMK5JbjXlbJnwnXQQECviICgawMYLez5ncyyAf0BZKmO+E/SgEEZWlh91qZ3fmkkWlkd2TaL2SPjgErsQwNLilaR9FIGMqWw3svh7M0XyrXFtuEkTM1TLxmTQ7k5UhCmnaCZu8KaVyjheUwrlWQPPnSC2wFc90RgeU3ZkMCg6yies3yzMOAy8l2vAxzsauY977Hhcpo57Pyo2FuPOUodkB8I4Xw7GCOLpcnFY659sWdaLshI7rxUJjUi19dczIatdIwgbL0Ji/uJhOAVsHgBX8bh9z1Mwp2pqxLl3oI/THA0pRp+fwzAj39bicPc5hpOX/a8Io72zjYyqLlwbZCO+ZwYHa2Cf6Uw==:KCVjro/k7nYcLkolxTH/r7y3Nz4XSk8amDQ4wtVTPnc=; ld_user=b0425183-9e55-407d-9be7-6bb3211b208d; visitorId=6f061c4f-06eb-4109-9576-6e0dc4673390; shopping-method=delivery; analyticsIsLoggedIn=false; ldUserType=anonymous; at_check=true; s_ecid=MCMID|53290601075226421873442998385050145914; dsch-visitorid=76600305-feee-4939-b9e8-00764dd657fc; visid_incap_3206490=MiQ0gFV6Qtu7NgfjAOXsjy5NyWgAAAAAQUIPAAAAAABJPbWCfV3qQLguJcTYWnXA; nlbi_3206490=4cyOdUrdA3qFpPOmzp3KBgAAAABd55rsbV/ZuVcd7+XaTAQM; incap_ses_780_3206490=jFNAM8EdUS81/mpf7h3TCi5NyWgAAAAAV+QpulKgKC8vKnIsoZdLtg==; mbox=session#f9f6068229004479b40f3a8acd0ca327#1758024904; dsch-sessionid=9215248f-c4a3-4c5c-8794-317c8b5a08f7; ad-memory-token=T%2BFSOzhVMHnrbaK%2BnVyyqLQi%2F5cKDRILCPqapcYGEPSAohAaAggCIgA%3D",
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
