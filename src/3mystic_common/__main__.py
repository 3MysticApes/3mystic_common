import sys


def main(*args, **kwargs):
  from cli import main

  main(*args, **kwargs)

if __name__ == '__main__':   
  main(sys.argv[1:])