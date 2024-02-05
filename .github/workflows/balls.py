import requests
api_key = '68ed9af2-cfff-4261-b61a-6ae0f493fcb2'
player_uuid = '11a1f625e00743b2ac461fe2c8a69577'
webhook = 'https://discord.com/api/webhooks/1204058877335961620/aHl0hmeApnxHAeJHQJtAqnQ1R4QnBLkUk05xOz-GjJfbt2TGwQb6-_6fdy_RqAxc-XI-'
url = f'https://api.hypixel.net/v2/status?key=68ed9af2-cfff-4261-b61a-6ae0f493fcb2&uuid=11a1f625e00743b2ac461fe2c8a69577'
response = requests.get(url, headers={"API-Key":api_key})
if response.status_code == 200 and response.json()['success'] and response.json()['session']['online']:
    data = response.json()
    print(data)
    webhook = DiscordWebhook(url=webhook)
    embed = DiscordEmbed(title='Elimm', description=str(data))
    webhook.add_embed(embed)
    response = webhook.execute()
else:
    print(f'Error: HTTP {response.status_code}')

