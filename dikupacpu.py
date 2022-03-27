#! /usr/bin/env python3
#SHEBANG
from netmiko import ConnectHandler
from time import sleep
from NMtcpdump import mac
import time
import matplotlib.pyplot as plt
#import modules with methods in this space

def network():
        ipl = '192.168.3.1'
        details = {
            'device_type':'cisco_ios',
            'ip': ipl,
            'username': 'cisco',
            'password': 'cisco123',
            'secret': 'cisco123',
            }
        print("successfully SSH into the router 1 using Netmiko \n Login details are shown below:")
        print(details)
        t_end = time.time() + 60*2 #60*2=120seconds
        open("cpu.txt","w")
        graph=[]
        print("Monitoring CPU and Creating Graph. Please wait for 2 minutes")
        while time.time() < t_end:   
            vty = ConnectHandler(**details)
            vty.enable()
            ping = f'sh processes cpu sorted | e 0.00%'
            output = vty.send_command(ping)
            vty.disconnect()
            with open("cpu.txt","w") as g:
                g.write(output)
            with open("cpu.txt","r") as l:
                j=l.readlines()
                z=j[0][33:36].strip()
                graph.append(z)
            time.sleep(5)
        plt.plot(graph)	 
        plt.xlabel('x-axis label')
        plt.title('Router CPU Utilization')	 
        plt.savefig("router_cpu_utilization.jpg")
#main function		    	    
def main():
       try:
             network()                  
       except KeyboardInterrupt: #ctrl+c sequence is included
              print("Exiting because of program interpreted by user"); print("Thanks for using my application");       
              
if __name__=='__main__':
       main() 
