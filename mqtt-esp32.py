import paho.mqtt.client as mqttClient
import time
from frame import DataFrame
from datetime import datetime, timezone
from parkir import Parkir
import requests
import json


def on_connect(client, userdata, flags, rc):
    if rc == 0:
        print("Connected to broker")
        global Connected
        Connected = True
    else:
        print("Connection failed")


def on_message(client, userdata, message):
    print("Message received: " + message.payload.decode())
    dt = DataFrame(message.payload.decode())
    utc_time = datetime.fromtimestamp(int(dt.transaksi, 16), timezone.utc)
    local_time = utc_time.astimezone()
    tanggal_transaksi = local_time.strftime("%Y-%m-%d %H:%M:%S")
    utc_time = datetime.fromtimestamp(int(dt.expired, 16), timezone.utc)
    local_time = utc_time.astimezone()
    tanggal_expired = local_time.strftime("%Y-%m-%d %H:%M:%S")
    st = False if dt.st_masuk == 1 else True
    parkir = Parkir(dt.serial, dt.kode_gate, dt.nopol.replace(".", ""), tanggal_transaksi, tanggal_expired, dt.frame,
                    st)
    park = json.dumps(parkir.__dict__)
    print(park)

    resp = requests.post(api_address + "/api/v1/parkirs", data=park, headers={'Content-Type': 'application/json'})
    print(resp)
    if resp.status_code != 201:
        raise Exception('POST /tasks/ {}'.format(resp.status_code))
    print('Created trx. ID: {}'.format(resp.json()["id"]))


Connected = False

broker_address = "localhost"
api_address = "http://localhost:8080"
port = 1883
user = ""
password = ""

client = mqttClient.Client("Python")
client.on_connect = on_connect
client.on_message = on_message

client.connect(broker_address, port)
client.loop_start()

while Connected != True:
    time.sleep(0.1)
client.subscribe("parkir/card")

try:
    while True:
        time.sleep(1)

except KeyboardInterrupt:
    print("exiting")
    client.disconnect()
    client.loop_stop()
