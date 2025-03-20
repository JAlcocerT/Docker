> [!IMPORTANT]
> Thanks to **Jim's Garage** to make the tutorial: https://www.youtube.com/@Jims-Garage

1. https://www.youtube.com/watch?v=ZOtUco5EwoI

2. https://github.com/JamesTurland/JimsGarage/tree/main/Caddy

---

If you are running this from a Pi, make sure to have proper docker compose version installed:

```sh
sudo apt-get update && sudo apt-get upgrade -y && sudo apt-get remove docker docker-engine docker.io containerd runc && sudo apt-get install ca-certificates curl gnupg && sudo install -m 0755 -d /etc/apt/keyrings && curl -fsSL https://download.docker.com/linux/raspbian/gpg | sudo gpg --dearmor -o /etc/apt/keyrings/docker.gpg && sudo chmod a+r /etc/apt/keyrings/docker.gpg && echo "deb [arch=$(dpkg --print-architecture) signed-by=/etc/apt/keyrings/docker.gpg] https://download.docker.com/linux/raspbian $(. /etc/os-release && echo "$VERSION_CODENAME") stable" | sudo tee /etc/apt/sources.list.d/docker.list > /dev/null && sudo apt-get update && sudo apt-get install docker-ce docker-ce-cli containerd.io docker-buildx-plugin docker-compose-plugin && docker --version && docker compose version && sudo docker system prune -a
```