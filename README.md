# git-xd-merge
Git merge driver for Adobe XD files

## Requirements
- A JSON merge driver, e.g. https://github.com/jonatanpedersen/git-json-merge
- python3
- git

## Installation
- put the python executable into your home directory
- install JSON merge driver (e.g. (https://github.com/jonatanpedersen/git-json-merge (`npm install --global git-json-merge`))
- add the following to your `.gitconfig` file:

      [merge "json"]
          name = custom merge driver for json files
          driver = git-json-merge %A %O %B
      [merge "xd"]
          name = custom merge driver for XD files
          driver = python3 ~/git-xd-merge.py %A %O %B
- add the following to your `.gitattributes` file:

      *.json merge=json
      *.agc merge=json
      *.xd merge=xd
