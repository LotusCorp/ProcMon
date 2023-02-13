import psutil
import socket
import os
import time

process_name = input("[EXECUTABLE] &> ")    # file.exe

def clear():
    if os.name ==  "nt":
        os.system("cls")
    else:
        os.system("clear")

def get_connection_info(pid):
    process = psutil.Process(pid)
    connections = process.connections()
    for conn in connections:
        if conn.type == socket.SOCK_STREAM:
            with open(f"{process_name}.txt", "a") as f:
                f.write("Proc: {:<15} | Local IP: {:<15} | Local Port: {:<7} | Remote IP: {:<15} | Remote Port: {:<15}\n".format(process_name, conn.laddr.ip, conn.laddr.port, conn.raddr.ip, conn.raddr.port))
                print("Proc: {:<15} | Local IP: {:<15} | Local Port: {:<7} | Remote IP: {:<15} | Remote Port: {:<15}".format(process_name, conn.laddr.ip, conn.laddr.port, conn.raddr.ip, conn.raddr.port))

def main():
    for i in range(1000000):
        time.sleep(0.1)   
        processes = psutil.process_iter()
        for process in processes:
            if process.name() == process_name:
                pid = process.pid
                get_connection_info(pid)

clear()
main()
