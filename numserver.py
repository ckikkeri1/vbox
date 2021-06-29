#!/usr/bin/env python

import asyncio
import random
import datetime
import websockets
import json
import cv2
import base64



async def handler(websocket, path):
	print("asdf")
	dub = 0
	while True:
		if dub % 2 == 0:
			await websocket.send("goat")
			
				
				
		else:
			await websocket.send("beast")
			
		dub = dub + 1
		await asyncio.sleep(2)

start_server = websockets.serve(handler, "127.0.0.1", 8888)

asyncio.get_event_loop().run_until_complete(start_server)
asyncio.get_event_loop().run_forever()

