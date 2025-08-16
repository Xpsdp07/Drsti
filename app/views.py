from django.shortcuts import render

def login(request):
    return render(request, 'login.html')
def home(request):
    return render(request, 'Home.html')


def connections(request):

    connections = [
        {"name": "MQTT Test", "type": "MQTT Client", "polling": "5s", "address": "192.168.0.10", "status": "OK", "enabled": True},
        {"name": "MQTT Backup", "type": "MQTT Client", "polling": "10s", "address": "192.168.0.11", "status": "NO", "enabled": False},
    ]
    return render(request, 'connection_configurations.html', {"connections": connections})
