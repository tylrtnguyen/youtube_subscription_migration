# Youtube Subscriptions Migration

### API: https://developers.google.com/youtube/v3/docs/subscriptions
### Google Quickstart: https://developers.google.com/youtube/v3/quickstart/python
### Enable YouTube Data API v3: https://console.cloud.google.com/apis/library/youtube.googleapis.com
### Quota costs: https://developers.google.com/youtube/v3/getting-started#quota


#### Step 1: Follow this [link](https://www.pcmag.com/how-to/how-to-move-youtube-content-to-a-new-google-account) to download YouTube data from the old channel to your local machine
#### Step 2: Copy the subscriptions.csv file to the folder where the script is
#### Step 3: Download the client_secret_[URL].json when create OAuth Client id on [API Console](https://console.developers.google.com/). Remember to select 'Desktop App' when Configure Consent on API Console
#### Step 4: Install dependencies
```python
pip install -r requirements.txt
```
#### Step 5: Run the main.py script
```python
python main.py
```
#### Sample output when running the script
```bash
Please visit this URL to authorize this application: [OAuth URL]
Enter the authorization code: [Enter authorized code here]
Successfully subscribed to Honeypot
Successfully subscribed to Whiteboard Crypto
Successfully subscribed to HackerOne
```