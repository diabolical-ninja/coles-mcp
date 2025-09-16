# Coles MCP

Testing the idea of exposing an API to an LLM, in this case the coles.com.au public API used by the website to search for and retrieve detailed product information, wrapped behind a lightweight local MCP server and then exposed to Claude Desktop.


## Setup

The project uses `uv`. Assuming it's installed you can run:

```sh
uv sync
```

Then to run the server:
```sh
uv run server.py
```

To run the server in debug mode:
```sh
uv run mcp dev server.py
```
Follow the provided url to open the MCP Inspector. The first time you run this it'll need to install the MCP Inspector. 

## NOTES:
THIS IS NOT ROBUST. DO NOT USE THIS FOR PRODUCTION!!!

The `BASE_URL` used in the `ColesAPI` client rotates. To fix, go to coles.com.au, serach for a product, open your browsers devtools, jump to the network tab & search for the `GET` request for `products.json?q={your search term}`. Inspect the request, extract the URL & update `BASE_URL` in `ColesAPI`.

I suspect there are many, many other flakes to be found. This project is just to test an idea.