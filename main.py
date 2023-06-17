"""Entry point"""
from .db import Client

uri = "mongodb+srv://admin:admin@cluster0.n6pwm8d.mongodb.net/?retryWrites=true&w=majority"




client = Client(uri, database='Client0')

client.ping()