#!/usr/bin/env python3
"""
Helper to get Google Sheets API credentials from gog tokens
"""
import json
import subprocess
import sys

def get_gog_token():
    """Get token from gog auth"""
    result = subprocess.run(
        ['gog', 'auth', 'list', '--json'],
        capture_output=True,
        text=True
    )
    
    if result.returncode != 0:
        print(f"Error getting gog auth: {result.stderr}", file=sys.stderr)
        return None
    
    data = json.loads(result.stdout)
    accounts = data.get('accounts', [])
    
    for acc in accounts:
        if acc.get('email') == 'nweferling82@gmail.com':
            return acc
    
    return None

def get_access_token():
    """Get fresh access token using gog's stored credentials"""
    # gog handles token refresh automatically
    # We can trigger an API call to ensure token is fresh
    result = subprocess.run(
        ['gog', 'drive', 'get', '1TOx2xmbhy9IpTMxDveLiGZ-581eZu6Pt', 
         '--account', 'nweferling82@gmail.com', '--json'],
        capture_output=True,
        text=True
    )
    
    if result.returncode != 0:
        return None
        
    # Token is now fresh, gog stores it internally
    # We need to extract it...
    # Actually, better approach: use gog's credentials directly
    
    with open('/Users/nwe/Downloads/client_secret.json', 'r') as f:
        creds = json.load(f)
    
    return creds['installed']

if __name__ == '__main__':
    token_info = get_gog_token()
    if token_info:
        print(json.dumps(token_info, indent=2))
    else:
        print("No token found", file=sys.stderr)
        sys.exit(1)
