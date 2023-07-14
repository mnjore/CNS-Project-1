# DDoS attack Detection Model based on Entropy Computing
DDoS attacks pose a significant threat to network infrastructure as they can lead to service problems and potential economic losses. This project aims to detect DDoS attacks using entropy-based network traffic analysis. The model uses entropy, a measure of uncertainty or randomness, to identify unusual patterns that indicate potential attacks.
## Technologies Used
- VirtualBox
- Ubuntu
- Python
- Mininet
- Xterm
- POX controller
## Installation
To use the DDoS attack detection model, follow these steps:
1. Install a version of Linux that can install a python version between 3.7 to 3.9:

This can be found at https://releases.ubuntu.com/

2. Install Mininet for network simulation:

sudo apt install mininet
sudo apt install xterm

3. Install various tools to be used:

sudo apt install vim
sudo apt install python3-pip
sudo apt install git

4. Install Scapy for packet generation:

sudo apt-get install python3-scapy

5. Install a SDN controller (choose form Opendaylight, Ryu, Floodlight, Beacon, POX, ONOS, OpenMUL, Maestro):

pip install pox

git clone http://github.com/noxrepo/pox
## Authors 
Mark Njore
