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
  
def displayMap(map):
  print("Please check the battlefield, commander.\n")
  print("  X00", end ="")
  for i in range(1,len(map[0])):
    print(" ", end ="")
    print("0"+str(i),end ="")
  print("X")
  print(" Y+--",end ="")
  for i in range(1,len(map)):
    print("-", end ="")
    print("--",end ="")
  print("Y")
  j=0
  for row in map:
    print("0"+str(j), end ="")
    for ele in row:
      print("|", end ="")
      print(ele,end ="")
    print("")
    j=j+1 
  print(" Y+--",end ="")
  for i in range(1,len(map)):
    print("-", end ="")
    print("--",end ="")
  print("Y")


def commandPanel(command,map):
  if command=="QUIT":
    sys.exit()
  elif command=="DIS":
    displayMap(map)
    return True
  elif command=="PRIS":
    printRecruitPrices()
    return True
  else:
    return False
     

def initMap(width, height, waters, woods, foods, golds):
    matrix = [["  "] * width for _ in range(height)]
    for water in waters:
      matrix[water[0]][water[1]]="~~"
      
    for wood in woods:
      matrix[wood[0]][wood[1]]="WW"
      
    for food in foods:
      matrix[food[0]][food[1]]="FF"
    for gold in golds:
      matrix[gold[0]][gold[1]]="GG"
    return matrix
  

def mainLogic(playerGoodsWFG,player,map):
  print("+++Player "+str(player)+"'s Stage: Recruit Armies+++")
  print("[Your Asset: Wood – "+str(playerGoodsWFG[0])+" Food – "+str(playerGoodsWFG[1])+" Gold – "+str(playerGoodsWFG[2])+"]")
  while True:
    emptyGoods=0
    for good in playerGoodsWFG:
      if good==0:
        emptyGoods=emptyGoods+1
    if emptyGoods==2:
      print("No resources to recruit any armies")
      return
    
    if player==1:
      if not(map[0][1]!="  " or map[1][0]!="  " or map[2][1]!="  " or map[1][2]!="  "):
        print("No place to recruit new armies.")
        return
    else:
      width=len(map[0])
      height=len(map)
      if not(map[width-3][height-2]!="  " or map[width-2][height-3]!="  " or map[width-1][height-2]!="  " or map[width-2][height-1]!="  "):
        print("No place to recruit new armies.")
        return
    userInput = input("\nWhich type of army to recruit, (enter) ‘S’,‘A’, ‘K’, or ‘T’? Enter ‘NO’ to end this stage\n")
    userInput=userInput.strip()
    if commandPanel(userInput,map):
      continue
    if userInput=="S":
      if insaficientResourceCheck(playerGoodsWFG,userInput):
        print("Insufficient resources. Try again.")
        continue
    elif userInput=="A":
      if insaficientResourceCheck(playerGoodsWFG,userInput):
        print("Insufficient resources. Try again.")
        continue
    elif userInput=="K":
      if insaficientResourceCheck(playerGoodsWFG,userInput):
        print("Insufficient resources. Try again.")
        continue
    elif userInput=="T":
      if insaficientResourceCheck(playerGoodsWFG,userInput):
        print("Insufficient resources. Try again.")
        continue
    elif userInput=="NO":
      return
    else:
      print("Sorry, invalid input. Try again.")
      continue
    

def rescruit(userInput):
  userXY = input("You want to recruit a "+userInput+".Enter two integers as format ‘x y’ to place your army.")
  while True:
    
    
def insaficientResourceCheck(playerGoodsWFG,userInput):
  if userInput=="S" and player1WFG[0]>0 and playerGoodsWFG[1]>0:
    return False
  elif userInput=="A" and player1WFG[0]>0 and playerGoodsWFG[2]>0:
    return False
  elif userInput=="K" and player1WFG[1]>0 and playerGoodsWFG[2]>0:
    return False
  elif userInput=="T" and player1WFG[0]>0 and playerGoodsWFG[1]>0 and player1WFG[2]>0:
    return False
  return True
  
  
  
    
def playerOneBlock(args):
  pass

def playerTwoBlock(args):
  pass

if __name__ == "__main__":
  if len(sys.argv) != 2:
    print("Usage: python3 little_battle.py <filepath>")
    sys.exit()
  try:
    width, height, waters, woods, foods, golds = load_config_file(sys.argv[1])
    print("Configuration file "+sys.argv[1]+" was loaded.",)
    print("Game Started: Little Battle! (enter QUIT to quit the game)\n")
    map=initMap(width, height, waters, woods, foods, golds)
    displayMap(map)
    print("\nEnter DIS to display the map")
    printRecruitPrices()
    print("Enter PRIS to display the price list\n")
    
    year=617
    player1WFG=[2,2,2]
    player2WFG=[2,2,2]
    while True:
      print("-Year "+str(year)+"-")
      year=year+1
      
  except Exception as e:
    print('An exception occurred :'+str(e))
    sys.exit()
  