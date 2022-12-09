import os, sys
try:
    __import__("share").bot()
except Exception as e:
    exit(str(e))
