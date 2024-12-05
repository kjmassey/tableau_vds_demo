import json
import requests
from generate_tableau_jwt import generate_login_jwt

from consts import REQ_URL, SITE_ID, TABLEAU_SERVER_NAME, DEFAULT_DATASOURCE_NAME


def do_region_query(request):

    payload = {
        "connection": {
            "tableauServerName": TABLEAU_SERVER_NAME,
            "siteId": SITE_ID,
            "datasource": DEFAULT_DATASOURCE_NAME
        },
        "query": {
            "columns": [
                {
                    "columnName": "Country/Region"
                },
                {
                    "columnName": "Region"
                },
                {
                    "columnName": "State/Province"
                },
                {
                    "columnName": "Regional Manager"
                },
                {
                    "columnName": "Sales",
                    "function": "SUM",
                    "columnAlias": "Total Sales"
                },
                {
                    "columnName": "Profit",
                    "function": "SUM",
                    "columnAlias": "Total Profit"
                },
                {
                    "columnName": "Order Count",
                    "calculation": "COUNTD([Order ID])"
                },
                {
                    "columnName": "Customer Count",
                    "calculation": "COUNTD([Customer Name])"
                }
            ],
            "filters": [
                {
                    "columnName": "Region",
                    "filterType": "SET",
                    "exclude": False,
                    "values": request.get('regions', [])
                }
            ],
            "options": {
                "debug": True
            }
        }
    }
    headers = {
        "credential-jwt": generate_login_jwt()
    }

    resp1 = requests.post(REQ_URL, json=payload, headers=headers)

    json_resp = json.loads(resp1.content)

    return json_resp
