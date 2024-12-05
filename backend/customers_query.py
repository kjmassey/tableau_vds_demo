import json
import requests
from generate_tableau_jwt import generate_login_jwt

from consts import REQ_URL, SITE_ID, TABLEAU_SERVER_NAME, DEFAULT_DATASOURCE_NAME


def do_customers_query(request):
    payload = {
        "connection": {
            "tableauServerName": TABLEAU_SERVER_NAME,
            "siteId": SITE_ID,
            "datasource": DEFAULT_DATASOURCE_NAME
        },
        "query": {
            "columns": [
                {
                    "columnName": "Customer Name"
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
                    "columnName": "Order Count",
                    "calculation": "COUNTD([Order ID])",
                    "sortPriority": 1,
                    "sortDirection": "DESC"
                },
                {
                    "columnName": "Sales",
                    "function": "SUM",
                    "columnAlias": "Sales",
                    "maxDecimalPlaces": 2
                },
                {
                    "columnName": "Profit",
                    "function": "SUM",
                    "columnAlias": "Profit",
                    "maxDecimalPlaces": 2
                },
                {
                    "columnName": "Discount",
                    "function": "AVG",
                    "columnAlias": "Avg Discount",
                    "maxDecimalPlaces": 2
                },
                {
                    "columnName": "Order Date",
                    "function": "MIN",
                    "columnAlias": "First Order Date"
                },
                {
                    "columnName": "Order Date",
                    "function": "MAX",
                    "columnAlias": "Most Recent Order Date"
                }
            ],
            "filters": [
                {
                    "columnName": "Order Count",
                    "filterType": "QUANTITATIVE",
                    "quantitativeFilterType": "MIN",
                    "min": 2 if request.get('repeat_customers') else 1
                }
            ]
        }
    }
    headers = {
        "credential-jwt": generate_login_jwt()
    }

    resp1 = requests.post(REQ_URL, json=payload, headers=headers)

    json_resp = json.loads(resp1.content)

    return json_resp
