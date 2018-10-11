import argparse

if __name__ == '__main__':

  parser = argparse.ArgumentParser()
  parser.add_argument("--token", help="Credential", type=str)
  parser.add_argument("--word", help="Random Word", type=str)

  args = parser.parse_args()

  print("Credentials :: " + args.token)
  print("Word :: " + args.word)