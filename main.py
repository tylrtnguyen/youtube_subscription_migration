import os

import google_auth_oauthlib.flow
import googleapiclient.discovery
import googleapiclient.errors
import pandas as pd

scopes = ["https://www.googleapis.com/auth/youtube.force-ssl"]

def main():
    # Disable OAuthlib's HTTPS verification when running locally.
    os.environ["OAUTHLIB_INSECURE_TRANSPORT"] = "1"

    df = pd.read_csv('subscriptions.csv')

    api_service_name = "youtube"
    api_version = "v3"
    client_secrets_file = "client_secret_1.json"

    # Get credentials and create an API client
    flow = google_auth_oauthlib.flow.InstalledAppFlow.from_client_secrets_file(
        client_secrets_file, scopes)
    credentials = flow.run_console()
    youtube = googleapiclient.discovery.build(
        api_service_name, api_version, credentials=credentials)
    
    for channel_id in df['Channel Id']:
        # This is one way to check if a channel is available, but it's really costly tho
        # Google limit quota: 10000 requests/day
        channel_info_request = youtube.channels().list(
            part="snippet,contentDetails,statistics",
            id=channel_id
        )
        channel_info_response = channel_info_request.execute()
        # If channel no longer exists
        if channel_info_response['pageInfo']['totalResults'] == 0:
            continue

        subscription_insert_request = youtube.subscriptions().insert(
            part="snippet",
            body={
              "snippet": {
                "resourceId": {
                  "kind": "youtube#channel",
                  "channelId": channel_id
                }
              }
            }
        )

        subscription_insert_response = subscription_insert_request.execute()

        if 'id' in subscription_insert_response:
            print(f'Successfully subscribed to {subscription_insert_response["snippet"]["title"]}')
        

if __name__ == "__main__":
    main()