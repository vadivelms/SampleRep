# import cowsay

# cowsay.trex("Kumar")
import sys
from sayings import hello

if len(sys.argv)==2:
    hello(sys.argv[1])