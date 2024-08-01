# sudo apt-get install wget gpg
# wget -qO- https://packages.microsoft.com/keys/microsoft.asc | gpg --dearmor > packages.microsoft.gpg
# sudo install -D -o root -g root -m 644 packages.microsoft.gpg /etc/apt/keyrings/packages.microsoft.gpg
# echo "deb [arch=amd64,arm64,armhf signed-by=/etc/apt/keyrings/packages.microsoft.gpg] https://packages.microsoft.com/repos/code stable main" |sudo tee /etc/apt/sources.list.d/vscode.list > /dev/null
# rm -f packages.microsoft.gpg

#https://code.visualstudio.com/Download#
# https://code.visualstudio.com/sha/download?build=stable&os=linux-deb-arm64
# sudo apt install ./<file>.deb


snap version
apt install nano

## Analytics ##

sudo apt update
sudo apt install software-properties-common
sudo add-apt-repository ppa:deadsnakes/ppa
sudo apt update
sudo apt install python3.12



## WEBSITES ##

#go for hugo
sudo snap install go --classic
go version

#node npm 
curl -o- https://raw.githubusercontent.com/nvm-sh/nvm/v0.38.0/install.sh | bash
source ~/.bashrc
nvm install 20.12.2
nvm use 20.12.2

node --version
npm --v