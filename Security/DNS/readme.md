1. Bind9
2. PiHole
3. Unbound
4. PiHole
5. Wirehole

**WireHole** is a **Docker Compose project** that combines three powerful tools to create a comprehensive, self-managed VPN solution:

1.  **WireGuard:** A modern, fast, and secure VPN protocol. WireHole uses it to create a full or split-tunnel VPN, allowing you to encrypt your internet traffic and route it through your own server.
2.  **Pi-hole:** A network-wide ad blocker and DNS sinkhole. When integrated with WireGuard, it blocks ads, trackers, and malicious domains for all devices connected to your VPN, even when you're away from your home network.
3.  **Unbound:** A validating, recursive, and caching DNS resolver. Unbound enhances your DNS privacy by performing DNS queries directly to the authoritative nameservers, bypassing your ISP's DNS, and also speeds up lookups through caching.

In essence, WireHole provides an all-in-one solution for:

* **Secure VPN access:** Encrypt your internet connection and protect your online privacy.
* **Network-wide ad and tracker blocking:** Enjoy an ad-free Browse experience on all your devices.
* **Enhanced DNS privacy and speed:** Control your DNS resolution and improve Browse performance.

Many WireHole implementations also include a **web UI (User Interface)**, often based on `wg-easy`, to simplify the management of WireGuard clients (creating, editing, deleting clients, generating QR codes for easy setup on devices).

It's a popular choice for self-hosters who want greater control over their network and online privacy.