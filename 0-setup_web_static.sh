#!/usr/bin/env bash
# script that sets up the web servers for the deployment of web_static

# Install Nginx if not already present
sudo apt-get update
sudo apt-get install -y nginx

# Create necessary directories
mkdir -p /data/web_static/releases/test/  # Create all parent directories if needed

# Create a fake HTML file for testing
echo "Hello, world! This is a test page for web_static deployment." > /data/web_static/releases/test/index.html

# Manage symbolic link for current release
rm -rf /data/web_static/current  # Remove existing link (if any)
ln -sf /data/web_static/releases/test/ /data/web_static/current

# Set ownership of /data/ recursively to ubuntu user and group
chown -R ubuntu:ubuntu /data/

# Update Nginx configuration
sed -i '51 i \
location /hbnb_static {\n\
\talias /data/web_static/current;\n\
\t}\n' /etc/nginx/sites-available/default

# Test configurations for syntax errors
sudo nginx -t

# Restart Nginx to apply changes
sudo service nginx restart

exit 0  # Ensure script always exits successfully

