#此脚本用于监测客户端运行情况 设定 断开自动重启 
	
'''
cron: 0 0 6 * * *
const $ = new Env("樱花frp运行监测");
'''

import os
import datetime


process_name = "frpc"

def is_process_running(process_name):
    try:
        command = f"pgrep {process_name}"
        result = os.popen(command).read()

        if result == "":
            return False
        else:
            return True

    except FileNotFoundError:
        return False

def is_client_connected_to_server(server_ip, port):
    try:
        command = f"nc -z -w 1 {server_ip} {port}"
        result = os.system(command)

        if result == 0:
            return True
        else:
            return False

    except FileNotFoundError:
        return False

def start_client():
    conf_path = "/root/frpc.ini"
    cmd = f"frpc -c {conf_path}"
    os.system(cmd)


server_ip = "61.139.65.135"
port = 32867

is_connected = is_client_connected_to_server(server_ip, port)

current_time = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")

if is_connected:
    if not is_process_running(process_name):
        start_client()
    else:
        print("客户端已经在运行，无需执行当前任务")

else:
    print(f"{current_time}: 客户端与服务器断开")
    datetime.datetime.now() + datetime.timedelta(seconds=20)
    is_connected = is_client_connected_to_server(server_ip, port)

    if is_connected:
        print(f"{current_time}: 客户端与服务器连接恢复")
    else:
        print(f"{current_time}: 客户端仍未连接到服务器，执行启动命令")
        start_client()
