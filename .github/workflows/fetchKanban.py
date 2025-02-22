# You need to install the requests library, run:
# pip install requests
import requests
import json

import os

# Get the GitHub token from the environment variable
github_token = os.environ['GITHUB_TOKEN']

# You'll need to obtain a personal access token from GitHub and set it as an environment variable.
# WARNING: Personal access tokens should be kept secret!
# In a GitHub action, you would set this as a secret and use it as an environment variable.
# github_token = 'your_github_token_here'

# The headers to authenticate with the GitHub API using your personal access token
headers = {
    'Authorization': f'token {github_token}',
    'Accept': 'application/vnd.github.inertia-preview+json'  # Custom media type for projects
}

# The URL for the GitHub project's API endpoint
# You will need to modify this URL to match your project's API endpoint
project_url = 'https://api.github.com/projects/1'

# Make a GET request to the GitHub API to fetch the project board data
response = requests.get(project_url, headers=headers)

# Check if the request was successful
if response.status_code == 200:
    # Parse the JSON response
    project_data = response.json()
    print(json.dumps(project_data, indent=4))  # This is for debugging; print the project data
else:
    print(f"Failed to fetch data: {response.status_code}")
