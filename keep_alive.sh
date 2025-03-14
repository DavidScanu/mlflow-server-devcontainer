#!/bin/bash
# keep_alive.sh - Script to keep a GitHub Codespace active
# This prevents automatic shutdown due to inactivity

echo "Starting Codespace keep-alive script..."
echo "Press Ctrl+C to stop"

while true; do
    # Create a small file change to simulate activity
    echo "Keeping codespace alive at $(date)" >> .codespace-activity.log
    
    # Git operations can also work as activity
    # git status > /dev/null 2>&1
    
    # Show a status message
    echo "Ping at $(date)"
    
    # Sleep for 30 minutes (1800 seconds)
    # GitHub typically has a 30-minute inactivity timeout
    sleep 300
done