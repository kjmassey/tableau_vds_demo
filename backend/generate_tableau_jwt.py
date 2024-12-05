import jwt
import datetime
import uuid


def generate_login_jwt():
    token = jwt.encode(
        {
            "iss": "CONNECTED-APP-CLIENT-ID",
            "exp": datetime.datetime.utcnow() + datetime.timedelta(minutes=10),
            "jti": str(uuid.uuid4()),
            "aud": "tableau",
            "sub": "TABLEAU-USER",
            # SCOPES EXPLAINED: https://help.tableau.com/current/online/en-us/connected_apps_scopes.htm
            "scp": ["tableau:projects:*", "tableau:content:read", "tableau:workbooks:*", "tableau:datasources:*", "tableau:users:*", "tableau:viz_data_service:read"],
        },
        "CONNECTED-APP-SECRET-VALUE",
        algorithm="HS256",
        headers={
            'kid': "CONNECT-APP-SECRET-ID",
            'iss': "CONNECTED-APP-CLIENT-ID"
        }
    )

    return token


def generate_login_jwt_kjmdev():
    token = jwt.encode(
        {
            "iss": "CONNECTED-APP-CLIENT-ID",
            "exp": datetime.datetime.utcnow() + datetime.timedelta(minutes=10),
            "jti": str(uuid.uuid4()),
            "aud": "tableau",
            "sub": "TABLEAU-USER",
            # SCOPES EXPLAINED: https://help.tableau.com/current/online/en-us/connected_apps_scopes.htm
            "scp": ["tableau:projects:*", "tableau:content:read", "tableau:workbooks:*", "tableau:datasources:*", "tableau:users:*", "tableau:viz_data_service:read"],
        },
        "CONNECTED-APP-SECRET-VALUE",
        algorithm="HS256",
        headers={
            'kid': "CONNECT-APP-SECRET-ID",
            'iss': "CONNECTED-APP-CLIENT-ID"
        }
    )

    return token
