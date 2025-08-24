#!/bin/bash

# Deploy script for GoDaddy
# Usage: ./deploy-to-godaddy.sh

echo "🚀 Deploying just4u platform to GoDaddy..."

# Copy the main file as index.html
cp just4u-platform-complete.html index.html

echo "✅ Created index.html from just4u-platform-complete.html"

# If you have FTP credentials, you can use this:
# ftp -n your-domain.com <<EOF
# user your-username your-password
# binary
# put index.html
# quit
# EOF

echo "📁 Files ready for upload:"
echo "  - index.html (main platform file)"
echo ""
echo "🎯 Next steps:"
echo "1. Upload index.html to your GoDaddy hosting via File Manager"
echo "2. Or use FTP to upload to public_html folder"
echo "3. Visit your domain to see the platform!"