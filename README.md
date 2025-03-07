# Fake Wi-Fi Project

## Overview
This project allows you to create a Fake Wi-Fi network to prank people by tricking them into connecting to it.

## How to Run

### Install Dependencies

First, we need to install some packages. Open **Termux** (for Android), **Kali Linux**, or your terminal on **Mac** and run the following commands:

#### For Termux:
```bash
$pkg update && pkg upgrade
$pkg install python
$pkg install python2
$pkg install git
$pkg install aircrack-ng
$pkg install hostapd
$pkg install dnsmasq

**Kali Linux**

$sudo apt update && sudo apt upgrade
$sudo apt install python
$sudo apt install python2
$sudo apt install git
$sudo apt install aircrack-ng
$sudo apt install hostapd
$sudo apt install dnsmasq

**For Mac**

$brew update
$brew install python
$brew install git
$brew install aircrack-ng
$brew install hostapd
$brew install dnsmasq

Clone the Repository
Next, clone the repository using the following command:

$git clone https://github.com/TahsinXRiyad/FakeXWifi.git
$cd FakeXWifi

Install Python Dependencies
After cloning the repo, install the required Python packages:

$pip install -r requirements.txt

Run the Fake Wi-Fi
To run the Fake Wi-Fi network, use the following command:

$python fake_wifi.py


