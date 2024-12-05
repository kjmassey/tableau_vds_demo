import json
import requests
from generate_tableau_jwt import generate_login_jwt
import datetime

from consts import REQ_URL, SITE_ID, TABLEAU_SERVER_NAME, DEFAULT_DATASOURCE_NAME


def do_orders_query():
    payload = {
        "connection": {
            "tableauServerName": TABLEAU_SERVER_NAME,
            "siteId": SITE_ID,
            "datasource": DEFAULT_DATASOURCE_NAME
        },
        "query": {
            "columns": [
                {
                    "columnName": "Order ID"
                },
                {
                    "columnName": "Category"
                },
                {
                    "columnName": "Sub-Category"
                },
                {
                    "columnName": "Country/Region"
                },
                {
                    "columnName": "State/Province"
                },
                {
                    "columnName": "City"
                },
                {
                    "columnName": "Postal Code"
                },
                {
                    "columnName": "Region"
                },
                {
                    "columnName": "Customer Name"
                },

                {
                    "columnName": "Product Name"
                },
                {
                    "columnName": "Order Date"
                },
                {
                    "columnName": "Quantity"
                },
                {
                    "columnName": "Sales"
                },
                {
                    "columnName": "Profit"
                },
                {
                    "columnName": "Discount"
                },
                {
                    "columnName": "Ship Mode"
                },
                {
                    "columnName": "Ship Date"
                }
            ],
        },

    }
    headers = {
        "credential-jwt": generate_login_jwt()
    }

    resp1 = requests.post(REQ_URL, json=payload, headers=headers)

    json_resp = json.loads(resp1.content)

    return json_resp
