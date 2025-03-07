import os

# Set up your fake Wi-Fi network settings
SSID = "FakeWiFi"  # Network name
password = "123456789"  # Network password

# Set up interface name for wireless adapter
interface = "wlan0"  # Change this to the correct interface name if necessary

# Create a fake Wi-Fi network using hostapd
os.system(f"sudo hostapd -B /etc/hostapd/hostapd.conf")

# Configure dnsmasq to manage DHCP and DNS requests
os.system(f"sudo dnsmasq -C /etc/dnsmasq.conf")

# Start the fake network
os.system(f"sudo ifconfig {interface} up")


