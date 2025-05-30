How to change the **Cloudflare DNS records programatically** with python.

```sh
#python3 -m venv venv
source venv/bin/activate
#pip install requests pyyaml
chmod +x update_dns.py
python3 update_dns.py
```

The DNS record will be created as per the `cloudflare_config.yaml` file.

Check with:

```sh
nslookup hugo.jalcocertech.com
nslookup portainer.jalcocertech.com
nslookup pigallery.jalcocertech.com
nslookup pihole.jalcocertech.com

nslookup postiz.jalcocertech.com
```

You will need your `YOUR_CF_DNS_API_TOKEN` and the ZONE_ID of your domain:

```sh
curl -s -X GET "https://api.cloudflare.com/client/v4/zones?name=jalcocertech.com" \
  -H "Authorization: Bearer YOUR_CF_DNS_API_TOKEN" \
  -H "Content-Type: application/json" | jq -r '.result[0].id'
```

See the subdomains inside a domain (zoneID):

```sh
ZONE_ID=$(yq -r '.cloudflare.zone_id' cloudflare_config.yaml); \
[ -z "$ZONE_ID" ] || [ "$ZONE_ID" == "null" ] && \
ZONE_ID=$(curl -s -X GET "https://api.cloudflare.com/client/v4/zones?name=$(yq -r '.cloudflare.domain_name' cloudflare_config.yaml)" \
  -H "Authorization: Bearer $(yq -r '.cloudflare.api_token' cloudflare_config.yaml)" \
  -H "Content-Type: application/json" | jq -r '.result[0].id'); \
curl -s -X GET "https://api.cloudflare.com/client/v4/zones/$ZONE_ID/dns_records" \
  -H "Authorization: Bearer $(yq -r '.cloudflare.api_token' cloudflare_config.yaml)" \
  -H "Content-Type: application/json" | \
jq -r '.result[] | select(.type != "NS" and .type != "MX") | .name' | sort -u
```