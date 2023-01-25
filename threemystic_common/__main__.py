import sys


def main(*args, **kwargs):
  from threemystic_common.cli import main
  
  # print(sys.path)
  main(*args, **kwargs)

if __name__ == '__main__':   
  main(sys.argv[1:])