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
  

def mainRescruitLogic(playerGoodsWFG,player,map):
  print("\n+++Player "+str(player)+"'s Stage: Recruit Armies+++")
  while True:
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
        if not(map[0][1]=="  " or map[1][0]=="  " or map[2][1]=="  " or map[1][2]=="  "):
          print("No place to recruit new armies.")
          return
      else:
        width=len(map[0])
        height=len(map)
        if (map[width-3][height-2]!="  " and map[width-2][height-3]!="  " and map[width-1][height-2]!="  " and map[width-2][height-1]!="  "):
          print("No place to recruit new armies.")
          return
      userInput = input("\nWhich type of army to recruit, (enter) ‘S’,‘A’, ‘K’, or ‘T’? Enter ‘NO’ to end this stage\n")
      userInput=userInput.strip()
      if commandPanel(userInput,map):
        continue
      if userInput=="S" or userInput=="A" or userInput=="K" or userInput=="T":
        if insaficientResourceCheck(playerGoodsWFG,userInput):
          print("Insufficient resources. Try again.")
          continue
        rescruit(userInput,player,map)
        break
      elif userInput=="NO":
        return
      else:
        print("Sorry, invalid input. Try again.")
        continue
    

def rescruit(userInput,player,map):
  if userInput=="S":
    name="Sperman"
  elif userInput=="A":
    name="Archer"
  elif userInput=="K":
    name="Knight" 
  else:
    name="Scout"
  while True:
    userXY = input("You want to recruit a "+name+". Enter two integers as format ‘x y’ to place your army.\n")
    userXY=userXY.strip()
    if commandPanel(userXY,map):
      continue
    xy=userXY.split(" ")
    
    try:
      if(len(xy)!=2):
        print("Sorry, invalid input. Try again.")
        continue
      x=int(xy[0])
      y=int(xy[1])
    except:
      print("Sorry, invalid input. Try again.")
      continue
    
    if ((player==1) and not((x==0 and y==1)or(x==1 and y==0) or (x==2 and y==1) or (x==1 and y==2))):
      print("You must place your newly recruited unit in an unoccupied position next to your home base. Try again.")
      continue
    elif player==2:
      width=len(map[0])
      height=len(map)
      if not(((x,y)==(width-3, height-2)) or ((x,y)==(width-2,height-3)) or ((x,y)==(width-1, height-2)) or ((x,y)==(width-2, height-1))):
        print("You must place your newly recruited unit in an unoccupied position next to your home base. Try again.")
        continue
    if map[x][y]!="  ":
      print("You must place your newly recruited unit in an unoccupied position next to your home base. Try again.")
      continue
    map[x][y]=userInput+str(player)
     
    print("You has recruited a "+name+"\n")
    return
    
    
    
def insaficientResourceCheck(playerGoodsWFG,userInput):
  if userInput=="S" and playerGoodsWFG[0]>0 and playerGoodsWFG[1]>0:
    playerGoodsWFG[0]=playerGoodsWFG[0]-1
    playerGoodsWFG[1]=playerGoodsWFG[1]-1
    return False
  elif userInput=="A" and playerGoodsWFG[0]>0 and playerGoodsWFG[2]>0:
    playerGoodsWFG[0]=playerGoodsWFG[0]-1
    playerGoodsWFG[2]=playerGoodsWFG[2]-1
    return False
  elif userInput=="K" and playerGoodsWFG[1]>0 and playerGoodsWFG[2]>0:
    playerGoodsWFG[1]=playerGoodsWFG[1]-1
    playerGoodsWFG[2]=playerGoodsWFG[2]-1
    return False
  elif userInput=="T" and playerGoodsWFG[0]>0 and playerGoodsWFG[1]>0 and playerGoodsWFG[2]>0:
    playerGoodsWFG[0]=playerGoodsWFG[0]-1
    playerGoodsWFG[1]=playerGoodsWFG[1]-1
    playerGoodsWFG[2]=playerGoodsWFG[2]-1
    return False
  return True



  
def checkForArmy(player,map,armiesToMove):
  result=False
  for row in range(len(map)):
    for col in range(len(map[0])):
      if map[row][col]=="S"+str(player):
        armiesToMove[0].append((row,col))
        result=True
        continue
      if map[row][col]=="K"+str(player):
        armiesToMove[1].append((row,col)) 
        result=True
        continue
      if map[row][col]=="A"+str(player): 
        armiesToMove[2].append((row,col))
        result=True
        continue
      if map[row][col]=="T"+str(player):
        armiesToMove[3].append((row,col)) 
        result=True
        continue    
  return result

def printArmiesToMove(armiesToMove):
  armies=["Spearman","Archer","Knight","Scout"]
  count=-1
  print("\nArmies to Move")
  for row in armiesToMove:
    count=count+1
    if len(row)==0:
      continue
    print(" "+armies[count]+":",end="")
    for ele in row:
      print(" ("+str(ele[0])+","+str(ele[1])+")",end="")
    print("")
  print("")
    
  

  
def mainMoveLogic(player,map,playerWFG,opositePlayer):
  print("\n===Player "+str(player)+"'s Stage: Move Armies===")
  
  while True:
    armiesToMove=[[],[],[],[]]
    if not checkForArmy(player,map,armiesToMove):
      print("\nNo Army to Move: next turn\n")
      return
    else:
      printArmiesToMove(armiesToMove)
      
    
    userInput=input("Enter four integers as a format ‘x0 y0 x1 y1’ to represent move unit from (x0, y0) to (x1, y1) or ‘NO’ to end this turn\n")
    
    if commandPanel(userInput,map):
      continue
    if userInput=="NO":
      return
    try:
      x1,y1,x2,y2=userInput.strip().split(" ")
      x1=int(x1)
      x2=int(x2)
      y1=int(y1)
      y2=int(y2)     
    except:
      print('Invalid move. Try again.')
      continue
    if not move(x1,y1,x2,y2,player,map,playerWFG,opositePlayer):
      print('Invalid move. Try again.')
      continue
    return
      

def move(x1,y1,x2,y2,player,map,playerWFG,opositePlayer):
  if player==1 and x2==1 and y2==1:
    return False
  elif player==2 and x2==len(map[0])-2 and y2==len(map)-2:
    return False
  elif not(x1==x2 and y1!=y2) and not(x1!=x2 and y1==y2):
    return False
  elif x1>len(map[0])-1 or x2>len(map[0])-1 or y1 >len(map)-1 or y2 >len(map)-1 or x1<0 or x2<0 or y1<0 or y2< 0:
    return False
  
  
  value=map[x1][y1].split(str(player))
  if len(value)!=2:
    return False
  armyType=value[0]
  name=getArmyName(armyType)

  if (armyType=="S" or armyType=="A" or armyType=="K") and not((abs(x1-x2)==1) or (abs(y1-y2)==1)):
    return False
  elif (armyType=="T") and not((abs(x1-x2)<=2) and (abs(y1-y2)<=2)):
    return False
  
  print("\nYou have moved "+name+" from ("+str(x1)+", "+str(y1)+") to("+str(x2)+", "+str(y2)+").")
  if armyType=="T" and (abs(x2-x1)>1 or abs(y2-y1)>1):
    xmid=x1 if x1==x2 else min(x1,x2)+1
    ymid=y1 if y1==y2 else min(y1,y2)+1
    
    if map[xmid][ymid]=="~~":
      map[x1][y1]="  "
      print("We lost the army "+name+" due to your command!")
      return True
    
    if  counterCheck(x1,y1,xmid,ymid,armyType,map,name,player,opositePlayer) and map[xmid][ymid]!="  ":
      return True
    
    if checkGoods(x1,y1,xmid,ymid,player,map,playerWFG,armyType) and checkGoods(xmid,ymid,x2,y2,player,map,playerWFG,armyType):
      return True
    else:
      counterval= counterCheck(xmid,ymid,x2,y2,armyType,map,name,player,opositePlayer)
      if not counterval:
        return False
      if counterval and (captureHomeCheck(x2,y2,map,player) or captureHomeCheck(xmid,ymid,map,player)):
        print("The army "+name+" captured the enemy’s capital.\n")
        commanderName=input("What’s your name, commander?")
        print("***Congratulation! Emperor "+commanderName+" unified the country in <year>.***")
        sys.exit(0)
      else:
        return counterval
  else :
    if checkGoods(x1,y1,x2,y2,player,map,playerWFG,armyType):
      return True
    else:
      counterval= counterCheck(x1,y1,x2,y2,armyType,map,name,player,opositePlayer)
      if counterval and captureHomeCheck(x2,y2,map,player):
        print("The army "+name+" captured the enemy’s capital.\n")
        commanderName=input("What’s your name, commander?")
        print("***Congratulation! Emperor "+commanderName+" unified the country in <year>.***")
        sys.exit(0)
      else:
        return counterval
      
    
    

def checkGoods(x1,y1,x2,y2,player,map,playerWFG,armyType):
  if map[x2][y2]=="GG":
    map[x1][y1]="  "
    map[x2][y2]=armyType+str(player)
    print("Good. We collected 2 Gold")
    playerWFG[2]=playerWFG[2]+2
    return True
  elif map[x2][y2]=="WW":
    map[x1][y1]="  "
    map[x2][y2]=armyType+str(player)
    print("Good. We collected 2 Wood")
    playerWFG[0]=playerWFG[0]+2
    return True
  elif map[x2][y2]=="FF":
    map[x1][y1]="  "
    map[x2][y2]=armyType+str(player)
    print("Good. We collected 2 Food")
    playerWFG[1]=playerWFG[1]+2
    return True
  return False

def captureHomeCheck(x2,y2,map,player):
  if player==2 and x2==1 and y2==1:
    return True
  elif player==1 and x2==len(map[0])-2 and y2==len(map)-2:
    return True
  return False
  


def counterCheck(x1,y1,x2,y2,armyType,map,name,player,opositePlayer):
  
  if map[x2][y2]=="~~":
    map[x1][y1]="  "
    print("We lost the army "+name+" due to your command!")
    return True
  elif map[x2][y2]=="  ":
    map[x1][y1]="  "
    map[x2][y2]=armyType+str(player)
    return True
  
  value=map[x2][y2].split(str(opositePlayer))
  if len(value)!=2:
    return False
  enemyArmyType=value[0]
  enemyName=getArmyName(enemyArmyType)
  mycode=getArmyTypeCode(armyType)
  enemycode=getArmyTypeCode(enemyArmyType)
  counter=[[2,1,0,1],[0,2,1,1],[1,0,2,1],[0,0,0,2]]
  
  if counter[mycode][enemycode]==2:
    map[x1][y1]="  "
    map[x2][y2]="  "
    print("We destroyed the enemy "+enemyName+" with massive loss")
    return True
  if counter[mycode][enemycode]==0:
    map[x1][y1]="  "
    map[x2][y2]="  "
    print("We lost the army "+name+" due to your command!")
    return True
  if counter[mycode][enemycode]==1:
    map[x1][y1]="  "
    map[x2][y2]=armyType+str(player)
    print("Great! We defeated the enemy "+name+"!")
    return True
  

def getArmyTypeCode(armyType):
  if armyType=="S":
    return 0
  elif armyType=="K":
    return 1
  elif armyType=="A":
    return 2
  else:
    return 3
  

def getArmyName(armyType):
  if armyType=="S":
    name="Sperman"
  elif armyType=="A":
    name="Archer"
  elif armyType=="K":
    name="Knight" 
  else:
    name="Scout"
  return name
    
  
    
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
      mainRescruitLogic(player1WFG,1,map)
      mainMoveLogic(1,map,player1WFG,2)
      mainRescruitLogic(player2WFG,2,map)
      mainMoveLogic(2,map,player2WFG,1)
      
  except Exception as e:
    print('An exception occurred :'+str(e))
    sys.exit()
  