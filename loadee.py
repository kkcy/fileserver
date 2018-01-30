import chirpsdk
import sys
import threading
import time

sdk = chirpsdk.ChirpSDK('iRxy7msaMmn2xw3DG7TRxvnzA', 'cJJMu9ujBJ3WF1EE8z9pgh9HuykZbfkB0qPXw6cQ4kR1ppfxu8')

sdk.set_protocol('ultrasonic')
chirp = sdk.create_chirp(sys.argv[1])
# chirp = sdk.create_chirp()

# print chirp.identifier
sdk.streaming_interval = 500
sdk.start_streaming(chirp)

while True:
	time.sleep(100)
