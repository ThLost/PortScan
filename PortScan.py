#!/usr/bin/env python
# -*- encoding: utf-8 -*-
#@Author TheLost
#Progect:PortScan

import socket
import thread
socket.setdefaulttimeout(1)

PORT_FILE = 'port.txt'
HOST = '103.255.93.246'

class PortScaner:

    '''Read port from file'''
    def get_port_file(self, file_name = PORT_FILE):
        port = []
        file = open(file_name)
        for line in file:
            port.append(line)
        return port

    '''Scan open port'''
    def port_scaner(self, ip, port):

        try:
            print port
            sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            result = sock.connect_ex((ip, int(port)))
            #print result
            if result == 0:
                print ip + ':' + port + '---------------------------------------> open'
                sock.close()
                return True
            else:
                sock.close()
                return False
        except:
            print str(port) + '--------Error...'
            return False

    '''Scan all  port from 0 to 65535'''
    def port_scan_all(self, ip):

        open_port = []
        for x in xrange(0, 65535):
            if(self.port_scaner(ip, str(x))):
                open_port.append(x)

        return open_port

    '''Scan port from file'''
    def port_scan_file(self, ip, file_name = PORT_FILE):

        open_port = []
        ports = self.get_port_file(file_name)
        for port in ports:
            if(self.port_scaner(ip, port)):
                open_port.append(int(port))

        return open_port

if __name__ == '__main__':

    ps = PortScaner()
    open_port = ps.port_scan_file(HOST)
    #open_port = ps.port_scan_all(HOST)
    print open_port
    print 'Port Scan Finish !'
