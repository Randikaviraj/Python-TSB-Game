import sys

# Please implement this function according to Section "Read Configuration File"
def load_config_file(filepath):
  # It should return width, height, waters, woods, foods, golds based on the file
  # Complete the test driver of this function in file_loading_test.py
  width, height = 0, 0
  waters, woods, foods, golds = [], [], [], [] # list of position tuples
  labels=["Frame","Water","Wood","Food","Gold"]
  
  with open(filepath,"r") as f:
    count=0
    while True:
      # Get next line from file
      line = f.readline()
      #  line is empty end of file is reached
      if not line:
        break
      line=line[:line.rfind("#")]
      line=line.strip()
      lineValues=line.split(":")
      func=checker(count)
      func(lineValues)
      count=+1
  
  return width, height, waters, woods, foods, golds

# checker funtion supplier
def checker(lineNo: int):
  if lineNo>0:
    return defaultCheck
  return lineOneCheck

# line one checker
def lineOneCheck(args):
  print("1")

# default checker
def defaultCheck(args):
  print("2")

if __name__ == "__main__":
  if len(sys.argv) != 2:
    print("Usage: python3 little_battle.py <filepath>")
    sys.exit()
  width, height, waters, woods, foods, golds = load_config_file(sys.argv[1])