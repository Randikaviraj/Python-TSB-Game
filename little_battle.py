import sys

# Please implement this function according to Section "Read Configuration File"
def load_config_file(filepath):
  # It should return width, height, waters, woods, foods, golds based on the file
  # Complete the test driver of this function in file_loading_test.py
  width, height = [0], [0]
  waters, woods, foods, golds = [], [], [], [] # list of position tuples
  labels=["Frame","Water","Wood","Food","Gold"]
  alreadAdded=[]
  
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
      if lineValues[0]!=labels[count]:
        raise SyntaxError("Invalid Configuration File: format error!")
      
      if count==0:
        lineOneCheck(lineValues[1],width, height)
      elif count==1:
        defaultCheck(lineValues[1],width, height,waters,alreadAdded)
      elif count==2:
        defaultCheck(lineValues[1],width, height,woods,alreadAdded)
      elif count==3:
        defaultCheck(lineValues[1],width, height,foods,alreadAdded)
      elif count==4:
        defaultCheck(lineValues[1],width, height,golds,alreadAdded)
      count=count+1
  return width[0], height[0], waters, woods, foods, golds



# line one checker
def lineOneCheck(line,width, height):
  values=line.strip().split("x")
  if len(values)!=2:
    raise SyntaxError("Invalid Configuration File: frame should be in format widthxheight!")
  w=int(values[0])
  h=int(values[1])
  if not((w>=5 and w<=7) and (h>=5 and h<=7)):
    raise ArithmeticError("Invalid Configuration File: width and height should range from 5 to 7!")
  width[0]=w
  height[0]=h

# default checker
def defaultCheck(line,width, height,dataArray,alreadAdded):
  values=line.strip().split(" ")
  if len(values)%2!=0:
    raise SyntaxError("Invalid Configuration File: <line_name (e.g., Water)> has an odd number of elements!")
  for i in range(0,len(values),2):
    try:
      w=int(values[i])
      h=int(values[i+1])
    except:
      raise ValueError("Invalid Configuration File: <line_name> (e.g., Water) contains non integer characters!")

    if not(w< width[0] and h<height[0]) :
      raise ArithmeticError("Invalid Configuration File: <line_name> contains a position that is out of map")
    
    if (w,h) in alreadAdded:
      raise SyntaxError("Invalid Configuration File: Duplicate position (x, y)!")
    
    if ((w,h)==(1, 1)) or ((w,h)==(width[0]-2,height[0]-2)) or ((w,h)==(0, 1)) or ((w,h)==(1, 0)) or ((w,h)==(2, 1)) or ((w,h)==(1, 2)) or ((w,h)==(width[0]-3, height[0]-2)) or ((w,h)==(width[0]-2,height[0]-3)) or ((w,h)== (width[0]-1, height[0]-2)) or ((w,h)==(width[0]-2, height[0]-1)):
      raise ValueError("Invalid Configuration File: The positions of home bases or the positions next to the home bases are occupied!")
    
    alreadAdded.append((w,h))
    dataArray.append((w,h))
    
def printRecruitPrices():
  print("\nRecruit Prices: \n  Spearman (S) - 1W, 1F \n  Archer (A) - 1W, 1G \n  Knight (K) - 1F,1G \n  Scout (T) - 1W, 1F, 1G \n")
  


    
    

if __name__ == "__main__":
  if len(sys.argv) != 2:
    print("Usage: python3 little_battle.py <filepath>")
    sys.exit()
  try:
    width, height, waters, woods, foods, golds = load_config_file(sys.argv[1])
    print("Configuration file "+sys.argv[1]+" was loaded.",)
    print("Game Started: Little Battle! (enter QUIT to quit the game)")
    
  except Exception as e:
    print('An exception occurred :'+str(e))
    sys.exit()
  