import socket
import platform
import os
import json
from datetime import datetime
from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/')
def get_node_info():
    """返回当前节点的信息"""
    hostname = socket.gethostname()
    ip_address = socket.gethostbyname(hostname)
    
    node_info = {
        "hostname": hostname,
        "ip_address": ip_address,
        "platform": platform.platform(),
        "python_version": platform.python_version(),
        "system": platform.system(),
        "processor": platform.processor(),
        "cpu_count": os.cpu_count(),
        "current_time": datetime.now().isoformat(),
        "environment_variables": dict(os.environ)
    }
    
    return '命中节点:%s' %node_info['ip_address']

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
