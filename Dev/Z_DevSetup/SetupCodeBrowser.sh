## Analytics ##

sudo apt update
sudo apt install software-properties-common
sudo add-apt-repository ppa:deadsnakes/ppa
sudo apt update
sudo apt install python3.12

python3.12 --version

## WEBS ##

#go
wget https://go.dev/dl/go1.22.5.linux-arm64.tar.gz
sudo tar -C /usr/local -xzf go1.22.5.linux-arm64.tar.gz
export PATH=$PATH:/usr/local/go/bin
source ~/.bashrc
go version

#hugo
#wget https://github.com/gohugoio/hugo/releases/tag/v0.108.0/hugo_extended_0.108.0_linux-amd64.deb -O hugo_latest.deb
wget https://github.com/gohugoio/hugo/releases/download/v0.108.0/hugo_0.108.0_linux-arm64.deb -O hugo_latest_arm64.deb
sudo dpkg -i hugo_latest_arm64.deb

#node npm 
curl -o- https://raw.githubusercontent.com/nvm-sh/nvm/v0.38.0/install.sh | bash
source ~/.bashrc
nvm install 20.12.2
nvm use 20.12.2

node --version
npm --v