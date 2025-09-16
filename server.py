import logging

from mcp.server.fastmcp import FastMCP

from src.coles import ColesAPI

# Initialize FastMCP server
mcp = FastMCP("coles", log_level="DEBUG")

COLES = ColesAPI()


@mcp.tool()
async def fetch_product_data(query: str) -> dict:
    """Fetch product data from Coles API based on the query."""
    logging.info("fetch_product_data")
    return COLES.fetch_product_data(query)


@mcp.tool()
async def fetch_product_details(product_slug: str) -> dict:
    """Fetch detailed product information from Coles API based on the product slug."""
    logging.info("fetch_product_details")
    return COLES.fetch_product_details(product_slug)


@mcp.tool()
async def create_product_slug(brand: str, name: str, size: str, product_id: str) -> str:
    """Create a product URL slug. To be used to create the product_slug for fetch_product_details."""
    logging.info("create_product_slug")
    return COLES.create_product_slug(brand, name, size, product_id)


if __name__ == "__main__":
    # Initialize and run the server
    print("Server running...")
    mcp.run(transport="stdio")
