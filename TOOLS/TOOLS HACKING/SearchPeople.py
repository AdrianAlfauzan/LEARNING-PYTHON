import os
from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build


def authenticate_google_api():
    SCOPES = ["https://www.googleapis.com/auth/contacts.readonly"]
    creds = None

    if os.path.exists("token.json"):
        creds = Credentials.from_authorized_user_file("token.json")

    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            flow = InstalledAppFlow.from_client_secrets_file(
                "path/to/your/credentials.json", SCOPES
            )
            creds = flow.run_local_server(port=0)

        with open("token.json", "w") as token:
            token.write(creds.to_json())

    return creds


def get_user_info(service):
    results = (
        service.people()
        .connections()
        .list(
            resourceName="people/me",
            personFields="names,emailAddresses",
        )
        .execute()
    )

    connections = results.get("connections", [])

    if not connections:
        print("No connections found.")
    else:
        for person in connections:
            names = person.get("names", [])
            email_addresses = person.get("emailAddresses", [])

            if names:
                name = names[0].get("displayName", "No display name")
                print(f"Name: {name}")

            if email_addresses:
                email = email_addresses[0].get("value", "No email address")
                print(f"Email: {email}")


def main():
    creds = authenticate_google_api()
    service = build("people", "v1", credentials=creds)
    get_user_info(service)


if __name__ == "__main__":
    main()
