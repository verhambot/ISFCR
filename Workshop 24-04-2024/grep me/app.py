#!/usr/bin/python3

import random
random_words = [
    "cybersecurity", "computer", "encryption", "firewall", "malware", 
    "virus", "network", "password", "authentication", "hacker", 
    "phishing", "cyberattack", "data", "privacy", "algorithm", 
    "cloud", "server", "router", "protocol", "software", 
    "hardware", "biometrics", "cyberspace", "firewall", 
    "antivirus", "spam", "DDoS", "trojan", "ransomware", 
    "backdoor", "sandbox", "patch", "exploit", "botnet", 
    "payload", "brute-force", "rootkit", "keylogger", 
    "cybercrime", "cyberwarfare", "identity", "access", 
    "authentication", "authorization", "injection", "firewall", 
    "cybersecurity", "vulnerability", "intrusion", "malware", 
    "spyware", "adware", "pharming", "cyberbullying", 
    "cyberstalking", "cyberterrorism", "cyberwarfare", 
    "bot", "worm", "zombie", "cookie", "certificate", 
    "decryption", "encryption", "firewall", "hacker", 
    "honeypot", "HTTPS", "IP", "MAC", "packet", 
    "plaintext", "port", "SSL", "TLS", "VPN", 
    "WPA", "WPA2", "DNS", "ARP", "HTML", 
    "JavaScript", "SQL", "API", "CPU", "GPU", 
    "RAM", "cache", "disk", "OS", "BIOS", 
    "kernel", "compiler", "debugger", "algorithm", 
    "data", "binary", "byte", "bit", "encryption"
]


str="isfcr{$uc3ssfully_Gr3p3d}"
y=random.randint(393,487)

for i in range(1000):
    if i==y:
        print(str, flush = True)
    for j in range(10):
        x=random.randint(0,len(random_words)-1)
        print(random_words[x], flush = True)
exit(0)
