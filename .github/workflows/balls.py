import subprocess
subprocess.check_call(["python", "-m", "pip", "install", "requests"])
import requests
# rest of your script
from discord_webhook import DiscordWebhook, DiscordEmbed

api_key = '68ed9af2-cfff-4261-b61a-6ae0f493fcb2'
player_uuid = '11a1f625e00743b2ac461fe2c8a69577'
webhook_url = 'https://discord.com/api/webhooks/1204058877335961620/aHl0hmeApnxHAeJHQJtAqnQ1R4QnBLkUk05xOz-GjJfbt2TGwQb6-_6fdy_RqAxc-XI-'
url = f'https://api.hypixel.net/status?key={api_key}&uuid={player_uuid}'
response = requests.get(url)

if response.status_code == 200 and response.json()['success'] and response.json()['session']['online']:
    data = response.json()
    print(data)
    webhook = DiscordWebhook(url=webhook_url)
    embed = DiscordEmbed(title='Elimm is Online!!!!!', description=('YIPPEEE!!!'))
    embed.set_image(url="https://media1.tenor.com/m/j-fJIMrTe2EAAAAC/happy-cat.gif")
    webhook.add_embed(embed)
    response = webhook.execute()
else:
    webhook = DiscordWebhook(url=webhook_url)
    embed = DiscordEmbed(title='OFFLINE!!!!', description=('START WORKING NOW!!!!!!'))
    webhook.add_embed(embed)
    embed.set_image(url="https://i.imgur.com/TdAAGqs.jpeg")
    response = webhook.execute()

