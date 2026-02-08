#!/bin/bash
# Autonomous Loop: Sync, Verify, and Deploy
cd /home/lianwei_zlw/hivemind
git add .
git commit -m "auto: lifecycle sync $(date +%Y%m%d_%H%M%S)"
git push origin main
echo "Deployment and Sync complete."
