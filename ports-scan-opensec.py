#!/usr/local/bin/python3
# -*- coding: utf-8 -*-

# Echo Cliente
# Ejecutar : python portscanner.py direccion_ip puerto_inicial puerto_final
import socket
import sys

if len(sys.argv) != 4:
  print ("\nUso: python " + sys.argv[0] + " <dirección-ip>" + " <puerto inicial>" + " <puerto final>\n")
  sys.exit(0)

HOST = sys.argv[1]    # El host remoto
PORT1 = int(sys.argv[2])
PORT2 = int(sys.argv[3])
currentport = PORT1
stream = "SeguridadOfensiva\n\n"

while (currentport <= PORT2):
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    resultado = s.connect_ex((HOST, currentport))
    if resultado == 0:
        print(currentport)
        #s.send(stream)
        #s.settimeout(5.0)
        data = s.recv(1024)
        #data = "dummy"
        #if resultado == 0:
        print ('Puerto --->',currentport,'Abierto.  ---> Software :',repr(data))
        s.close()
    else:
        print('Puerto --->',currentport,"Cerrado o Filtrado")
    currentport = currentport + 1
