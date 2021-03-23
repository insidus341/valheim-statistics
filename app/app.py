import os
from statistics import ServerStatistics

from dotenv import load_dotenv
load_dotenv()

SERVER_IP = os.getenv('SERVER_IP')
SERVER_DOMAIN = os.getenv('SERVER_DOMAIN')
SERVER_PORT = int(os.getenv('SERVER_PORT'))
SERVER_ADDRESS = (SERVER_IP, SERVER_PORT)

INFLUXDB_HOST = os.getenv('INFLUXDB_HOST')
INFLUXDB_PORT = os.getenv('INFLUXDB_PORT')
INFLUXDB_DATABASE = os.getenv('INFLUXDB_DATABASE')

if SERVER_ADDRESS is None or SERVER_DOMAIN is None or INFLUXDB_HOST is None or INFLUXDB_PORT is None or INFLUXDB_DATABASE is None:
    exit(1)

def run():
    start_statistics()

def start_statistics():
    statistics = ServerStatistics(SERVER_ADDRESS, SERVER_DOMAIN, INFLUXDB_HOST, INFLUXDB_PORT, INFLUXDB_DATABASE)
    statistics.run()

if __name__ == "__main__":
    run()