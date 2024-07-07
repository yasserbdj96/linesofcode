#!/usr/bin/env python
# coding:utf-8
#   |                                                         |   #
# --+---------------------------------------------------------+-- #
#   |    Code by: yasserbdj96                                 |   #
#   |    Email: yasser.bdj96@gmail.com                        |   #
#   |    GitHub: github.com/yasserbdj96                       |   #
#   |    Sponsor: github.com/sponsors/yasserbdj96             |   #
#   |    BTC: bc1q2dks8w8uurca5xmfwv4jwl7upehyjjakr3xga9      |   #
#   |                                                         |   #
#   |    All posts with #yasserbdj96                          |   #
#   |    All views are my own.                                |   #
# --+---------------------------------------------------------+-- #
#   |                                                         |   #

#START{
import argparse
import os
import sys
import subprocess

# Create an ArgumentParser object
parser = argparse.ArgumentParser()

# Add arguments with names
parser.add_argument('--URL', '--url', dest='URL', type=str, default=os.getenv('URL', ''), help='')

# Parse the command-line arguments
args = parser.parse_args()

URL = args.URL

#
def clone_repo(repo_url, folder_name='temp'):
    try:
        # Ensure the folder name is a directory
        if not os.path.isdir(folder_name):
            os.makedirs(folder_name)
        # Run the git clone command
        subprocess.run(['git', 'clone', repo_url, folder_name], check=True)
        print(f"Repository cloned into {folder_name}")
    except subprocess.CalledProcessError as e:
        print(f"Error occurred while cloning the repository: {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

if __name__ == "__main__":
    repo_url = URL
    clone_repo(repo_url)








print(URL)