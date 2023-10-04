#!/usr/bin/env bash
# a Bash script that sets up your web servers for the deployment of web_static
# coloring
green='\033[0;34m'
#orange='\033[0;33m'
#red='\033[0;31m'
yellow='\033[1;33m'
cprint() {
  local color=$1
  local text=$2
  local NC='\033[0m'
  echo -e "${color}${text}${NC}"
}

cprint "$green" "Good Moring I would like to update && upgrade and Installing Nginx... so bring snaks"

sudo apt-get -y update
sudo apt-get -y upgrade
sudo apt-get -y install nginx

cprint "$green" "Nginx installed"
cprint "$green" "Creating folder for your static web and Configuring Nginx..."

sudo mkdir -p /data/web_static/releases/test /data/web_static/shared
# create a index.html file
config=\
"
<html>
  <head>
  </head>
  <body>
    Holberton School
  </body>
</html>
"
echo "$config" | sudo tee /data/web_static/releases/test/index.html
# create a symbolic link to index.html
sudo ln -sf /data/web_static/releases/test/ /data/web_static/current

# Give ownership of the /data/

sudo chown -hR ubuntu:ubuntu /data/

# Update the Nginx configuration to serve the content of 
#/data/web_static/current/ to hbnb_static (ex: https://mydomainname.tech/hbnb_static).

cprint "$yellow" "[ ! ] Configuring Nginx..."
sudo sed -i '38i\\tlocation /hbnb_static/ {\n\t\talias /data/web_static/current/;\n\t}\n' /etc/nginx/sites-available/default
sudo service nginx restart

cprint "$green" "[ * ] Nginx configured"
