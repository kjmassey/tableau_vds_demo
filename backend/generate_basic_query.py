import json
import requests
from generate_tableau_jwt import generate_login_jwt

from consts import REQ_URL, SITE_ID, TABLEAU_SERVER_NAME, DEFAULT_DATASOURCE_NAME


def do_basic_query():
    payload = {
        "connection": {
            "tableauServerName": TABLEAU_SERVER_NAME,
            "siteId": SITE_ID,
            "datasource": DEFAULT_DATASOURCE_NAME
        },
        "query": {
            "columns": [
                {
                    "columnName": "Category"
                },
                {
                    "columnName": "Sub-Category"
                },
                {
                    "columnName": "Order Month-Year",
                    "calculation": "DATETRUNC('month', [Order Date])"
                },
                {
                    "columnName": "Sales",
                    "function": "SUM",
                    "maxDecimalPlaces": 0,
                    "columnAlias": "Sales ($)"
                }
            ],
            "filters": [
                {
                    "columnName": "Order Date",
                    "filterType": "QUANTITATIVE",
                    "quantitativeFilterType": "MIN",
                    "minDate": {
                        "day": 1,
                        "month": 1,
                        "year": 2024
                    }
                }
            ]
        }
    }
    headers = {
        "credential-jwt": generate_login_jwt()
    }

    resp = requests.post(REQ_URL, json=payload, headers=headers)

    return json.loads(resp.content)
