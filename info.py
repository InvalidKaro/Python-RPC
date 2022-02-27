import rpc
import time
from time import mktime

print("Starting RPC...")
client_id = '901481842862080001'  # Your application's client ID as a string. (This isn't a real client ID)
rpc_obj = rpc.DiscordIpcClient.for_platform(client_id)  # Send the client ID to the rpc module
print("RPC connection successful.")

time.sleep(5)
start_time = mktime(time.localtime())
while True:
    activity = {
            "state": "Editing a file",  # anything you like
            "details": "Developing Siesta",  # anything you like
            "timestamps": {
                "start": start_time
            },
            "assets": {
                "small_text": "Python",  # anything you like
                "small_image": "python",  # must match the image key
                "large_text": "Siesta Discord Bot",  # anything you like
                "large_image": "siesta"  # must match the image key
            }
        }
    rpc_obj.set_activity(activity)
    time.sleep(900)
