## what you'll need :
-[] nmap
-[] VNC Viewer
-[] raspberry pi

##whatis nmap ?
nmap (1) - Network exploration tool and security / port scanner
We'll use it to find the raspberry's IP address display it while running Ubuntu/ROS/etc: Open up your terminal
```
$sudo apt-get install nmap

We need the subnet address for the pi, run:
$ ip address show

In general, ethernet connections begin with 'e', wireless 'w'. In the example below, look at number 2 and find 'inet 10.42.0.1/24' (On your system this number may be different). For these notes, I will refer to it as your-enet-address.
---------------------------------------
2: eno1: <BROADCAST,MULTICAST,UP,LOWER_UP> mtu 1500 qdisc fq_codel state UP group default qlen 1000
    link/ether 48:ba:4e:b6:73:17 brd ff:ff:ff:ff:ff:ff
    inet 10.42.0.1/24 brd 10.42.0.255 scope global noprefixroute eno1
       valid_lft forever preferred_lft forever
    inet6 fe80::c2d6:1435:bc0c:a8a3/64 scope link noprefixroute 
       valid_lft forever preferred_lft forever
3: wlo1: <BROADCAST,MULTICAST,UP,LOWER_UP> mtu 1500 qdisc noqueue state UP group default qlen 1000
    link/ether f8:94:c2:27:74:82 brd ff:ff:ff:ff:ff:ff
    inet 10.85.170.31/21 brd 10.85.175.255 scope global dynamic noprefixroute wlo1
       valid_lft 1484sec preferred_lft 1484sec
    inet6 fe80::6938:d0a9:1c7d:5597/64 scope link noprefixroute 
       valid_lft forever preferred_lft forever
----------------------------------------

use nmap to identify what devices are running on your system, and get the real enet-address using your-enet-address :
*IMPORTANT* you want to search for ALL devices running on the system so you need a wildcard. How to use a wildcard, using my enet-address :
10.42.0.1/24 would be written as 10.42.0.*

$ nmap your-enet-address

Results------------------------------------
Starting Nmap 7.60 ( https://nmap.org ) at 2020-02-21 11:09 PST
Nmap scan report for sisyphus (10.42.0.1)
Host is up (0.00066s latency).
Not shown: 999 closed ports
PORT   STATE SERVICE
53/tcp open  domain

Nmap scan report for 10.42.0.178
Host is up (0.0032s latency).
Not shown: 998 closed ports
PORT     STATE SERVICE
22/tcp   open  ssh
5900/tcp open  vnc

Nmap done: 256 IP addresses (2 hosts up) scanned in 3.11 seconds
------------------------------------------
We now have the full e-net address on the report for ( 10.42.0.178 ). 

Create a secure shell to interface with raspberry pi:
our network name is pi
$ ssh pi@10.42.0.178
you will use your own address from the result above.
```


2 ways to install:
---
1. https://www.realvnc.com/en/connect/download/viewer/
2. Ubuntu->Software->Search for 'realvnc-vnc-viewer'

To connect you will need:
---
1. your-enet-address
2. username : pi
3. password : password

End.

