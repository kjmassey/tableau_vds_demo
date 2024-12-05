import json
import requests
from generate_tableau_jwt import generate_login_jwt

from consts import REQ_URL, SITE_ID, TABLEAU_SERVER_NAME, DEFAULT_DATASOURCE_NAME


def do_library_query():
    payload = {
        "connection": {
            "tableauServerName": TABLEAU_SERVER_NAME,
            "siteId": SITE_ID,
            "datasource": DEFAULT_DATASOURCE_NAME
        },
        "query": {
            "columns": [
                {
                    "columnName": "Book Id"
                },
                {
                    "columnName": "Author"
                },
                {
                    "columnName": "Book Title"
                },
                {
                    "columnName": "Genre"
                },
                {
                    "columnName": "Super Genre"
                },
                {
                    "columnName": "Checkouts",
                    "function": "SUM",
                    "columnAlias": "Total Checkouts"
                },
                {
                    "columnName": "Release Year"
                },
                {
                    "columnName": "Total Stock",
                    "function": "AVG",
                    "columnAlias": "Copies Owned"
                },
                {
                    "columnName": "Copies Available",
                    "function": "AVG",
                    "columnAlias": "Available Copies"
                },
                {
                    "columnName": "Cover URL"
                },
                {
                    "columnName": "Synopsis"
                },
                {
                    "columnName": "Rank by Genre",
                    "function": "MAX",
                    "columnAlias": "Genre Rank"
                }
            ]
        }
    }
    headers = {
        "credential-jwt": generate_login_jwt()
    }

    resp1 = requests.post(REQ_URL, json=payload, headers=headers)

    payload = {
        "connection": {
            "tableauServerName": "10ax.online.tableau.com",
            "siteId": "kjmbeta",
            "datasource": "VDSLibrary"
        },
        "query": {
            "columns": [
                {
                    "columnName": "Book Id"
                },
                {
                    "columnName": "Month"
                },
                {
                    "columnName": "Checkouts"
                }
            ]
        }
    }

    resp2 = requests.post(REQ_URL, json=payload, headers=headers)

    json_resp = json.loads(resp1.content)

    for item in json_resp['data']:
        item['checkout history'] = [book['Checkouts'] for book in json.loads(
            resp2.content)['data'] if book['Book Id'] == item['Book Id']]

    return json_resp
