import json
import requests
from generate_tableau_jwt import generate_login_jwt_kjmdev
from consts import REQ_URL, TABLEAU_SERVER_NAME

SITE_ID = 'kjmdev797388'


def do_support_desk_query():
    payload = {
        "connection": {
            "tableauServerName": TABLEAU_SERVER_NAME,
            "siteId": SITE_ID,
            "datasource": "VDSServiceDesk"
        },
        "options": {
            "debug": False,
            "returnFormat": "OBJECTS"
        },
        "query": {
            "columns": [
                {
                    "columnName": "Number",
                    "columnAlias": "number"
                },
                {
                    "columnName": "Short Description",
                    "columnAlias": "shortDescription"
                },
                {
                    "columnName": "Assigned To",
                    "columnAlias": "assignee"
                },
                {
                    "columnName": "Comments",
                    "columnAlias": "comments"
                },
                {
                    "columnName": "Details",
                    "columnAlias": "details"
                },
                {
                    "columnName": "Escalated",
                    "columnAlias": "escalated"
                },
                {
                    "columnName": "Opened",
                    "columnAlias": "opened"
                },
                {
                    "columnName": "Reporter",
                    "columnAlias": "reporter"
                },
                {
                    "columnName": "Status",
                    "columnAlias": "status"
                },
                {
                    "columnName": "csat",
                    "function": "SUM"
                },
                {
                    "columnName": "assigneeTicketCount",
                    "calculation": "{FIXED [Assigned To]: COUNTD([Number])}"
                },
                {
                    "columnName": "ageDays",
                    "calculation": "DATEDIFF('day',[Opened], TODAY())"
                },
                {
                    "columnName": "isPastDue",
                    "calculation": "IF DATEDIFF('day',[Opened],TODAY()) > 120 THEN true ELSE false END"
                }
            ]
        }
    }

    headers = {"credential-jwt": generate_login_jwt_kjmdev()}

    resp = requests.post(REQ_URL, json=payload, headers=headers)
    json_resp = json.loads(resp.content)

    return sorted(json_resp['data'], key=lambda x: x['opened'], reverse=True)
