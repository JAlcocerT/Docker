#sudo apt install python3-pip
#pip3 install requests pyyaml
#apt install python3-pyyaml


#python3 -m venv venv
#source venv/bin/activate
#pip install requests pyyaml
# Creating update_dns.py

import os
import sys
import yaml
import requests
import socket
import logging
from pathlib import Path

# Set up logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s',
    handlers=[
        logging.StreamHandler(sys.stdout)
    ]
)
logger = logging.getLogger(__name__)

# Configuration
CONFIG_FILE = Path(__file__).parent / 'cloudflare_config.yaml'
CLOUDFLARE_API = 'https://api.cloudflare.com/client/v4'

def load_config():
    """Load configuration from YAML file."""
    try:
        with open(CONFIG_FILE, 'r') as f:
            config = yaml.safe_load(f)
        return config
    except Exception as e:
        logger.error(f"Error loading config: {e}")
        sys.exit(1)

def get_public_ip():
    """Get current public IP address."""
    try:
        response = requests.get('https://api.ipify.org?format=json', timeout=10)
        return response.json()['ip']
    except Exception as e:
        logger.error(f"Error getting public IP: {e}")
        return None

def get_dns_record_id(zone_id, record_name, record_type, headers):
    """Get DNS record ID by name and type."""
    try:
        url = f"{CLOUDFLARE_API}/zones/{zone_id}/dns_records"
        params = {
            'name': f"{record_name}.jalcocertech.com",  # Adjust domain as needed
            'type': record_type
        }
        response = requests.get(url, headers=headers, params=params)
        response.raise_for_status()
        records = response.json()['result']
        return records[0]['id'] if records else None
    except Exception as e:
        logger.error(f"Error getting DNS record: {e}")
        return None

def update_dns_record(zone_id, record_id, record_name, record_type, ip_address, proxied, headers):
    """Update DNS record with new IP address."""
    url = f"{CLOUDFLARE_API}/zones/{zone_id}/dns_records/{record_id}"
    data = {
        'type': record_type,
        'name': f"{record_name}.jalcocertech.com",  # Adjust domain as needed
        'content': ip_address,
        'ttl': 1,  # 1 for auto
        'proxied': proxied
    }
    
    try:
        response = requests.put(url, headers=headers, json=data)
        response.raise_for_status()
        logger.info(f"Successfully updated {record_name} to {ip_address}")
        return True
    except Exception as e:
        logger.error(f"Error updating DNS record: {e}")
        if hasattr(e, 'response') and e.response is not None:
            logger.error(f"Response: {e.response.text}")
        return False

def main():
    # Load configuration
    config = load_config()
    cf_config = config['cloudflare']
    api_token = cf_config['api_token']
    zone_id = cf_config['zone_id']
    
    # Set up headers
    headers = {
        'Authorization': f'Bearer {api_token}',
        'Content-Type': 'application/json'
    }
    
    # Get current public IP
    current_ip = get_public_ip()
    if not current_ip:
        logger.error("Could not determine public IP")
        sys.exit(1)
    
    logger.info(f"Current public IP: {current_ip}")
    
    # Update each record in config
    success = True
    for record in cf_config['records']:
        record_name = record['name']
        record_type = record['type']
        proxied = record.get('proxied', False)
        
        logger.info(f"Processing record: {record_name} ({record_type})")
        
        # Get record ID
        record_id = get_dns_record_id(zone_id, record_name, record_type, headers)
        if not record_id:
            logger.warning(f"Record {record_name} not found, attempting to create it...")
            # Determine IP to use (custom content or public IP)
            ip_address = record.get('content', current_ip)
            success = success and create_dns_record(zone_id, record_name, record_type, ip_address, proxied, headers)
            continue
        
        # Determine IP to use (custom content or public IP)
        ip_address = record.get('content', current_ip)

        # Update record
        success = success and update_dns_record(
            zone_id, record_id, record_name, record_type, ip_address, proxied, headers
        )
    
    sys.exit(0 if success else 1)

def create_dns_record(zone_id, record_name, record_type, ip_address, proxied, headers):
    """Create a new DNS record."""
    url = f"{CLOUDFLARE_API}/zones/{zone_id}/dns_records"
    data = {
        'type': record_type,
        'name': f"{record_name}.jalcocertech.com",  # Adjust domain as needed
        'content': ip_address,
        'ttl': 1,  # 1 for auto
        'proxied': proxied
    }
    
    try:
        response = requests.post(url, headers=headers, json=data)
        response.raise_for_status()
        logger.info(f"Successfully created record {record_name} with IP {ip_address}")
        return True
    except Exception as e:
        logger.error(f"Error creating DNS record: {e}")
        if hasattr(e, 'response') and e.response is not None:
            logger.error(f"Response: {e.response.text}")
        return False

if __name__ == '__main__':
    main()