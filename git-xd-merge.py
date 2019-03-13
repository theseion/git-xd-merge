#/usr/bin/env python3

import sys
from zipfile import ZipFile, BadZipFile
import tempfile
import subprocess
import shutil
import os.path

def run(ancestor, current, other):
	path = os.getcwd()
	import pdb; pdb.set_trace()
	with tempfile.TemporaryDirectory() as directory:
		subprocess.run(["git", "init"], cwd=directory)

		subprocess.run(["git", "checkout", "-b", "ancestor"], cwd=directory)
		try:
			ZipFile(os.path.join(path, ancestor)).extractall(directory)
			subprocess.run(["git", "add", "-A"], cwd=directory)
			subprocess.run(["git", "commit", "-am", "'foo'"], cwd=directory)
		except BadZipFile:
			pass

		subprocess.run(["git", "checkout", "-b", "current"], cwd=directory)
		try:
			ZipFile(os.path.join(path, current)).extractall(directory)
			subprocess.run(["git", "add", "-A"], cwd=directory)
			subprocess.run(["git", "commit", "-am", "'foo'"], cwd=directory)
		except BadZipFile:
			pass

		subprocess.run(["git", "checkout", "ancestor"], cwd=directory)
		subprocess.run(["git", "checkout", "-b", "other"], cwd=directory)
		try:
			ZipFile(os.path.join(path, other)).extractall(directory)
			subprocess.run(["git", "commit", "-am", "'foo'"], cwd=directory)
		except BadZipFile:
			pass
		
		subprocess.run(["git", "checkout", "current"], cwd=directory)
		completed = subprocess.run(["git", "merge", "other", "-m", "'foo'"], capture_output=True, cwd=directory)
		if completed.returncode != 0:
			sys.exit(-1)

		subprocess.run(["rm", "-rf", ".git"], cwd=directory)
		subprocess.run(["zip", "-r", "stuff", "."], cwd=directory)
		shutil.copy(os.path.join(directory, 'stuff.zip'), os.path.join(path, current))

		sys.exit(0)

# pylint: disable=no-value-for-parameter
run(*sys.argv[1:])