from os import system,name
from time import sleep
import random

#Function to clear Screen
def clear(): 
    if name == 'nt': 
        _ = system('cls')


n=int(input("Enter Grid size"))   #Input of Grid Size

gen=random.sample(range(n),2)     #Generating 2 random numbers

#Class to generate grid
class Grid:
    
    def __init__(self,n):
        self.n=n
        self.start=(0,gen[0])
        self.goal=(self.n-1,gen[1])
        self.Obstacle=Obstacle() #Calling Obstacle class
        self.Reward=Reward()  #Calling Reward class
        
    myObstacles=[]  #List of obstacles
    myRewards=[]    #List of Rewards
    Grid=[]         #List to store Grid

    #helper function to generate obstacles
    def obs(self):
        for a in range(random.randint(3,n)):
            self.myObstacles.append(self.Obstacle.points())

    #Helper function to generate reward
    def rew(self):
        for a in range(random.randint(3,n)):
            self.myRewards.append(self.Reward.points())
            
    #Function to rotate grid clockwise
    def rotateClockwise(self):
        self.Grid[gen[0]][0]='.'
        self.Grid[gen[1]][n-1]='.'
        for i in range(int(self.n/2)):
            for j in range(i,self.n-i-1):
                temp=self.Grid[i][j]
                self.Grid[i][j]=self.Grid[n-1-j][i]
                self.Grid[n-1-j][i]=self.Grid[n-1-i][n-1-j]
                self.Grid[n-1-i][n-1-j]=self.Grid[j][n-1-i]
                self.Grid[j][n-1-i]=temp
        self.Grid[gen[0]][0]='S'
        self.Grid[gen[1]][n-1]='G'

    #Function to rotate grid anticlockwise   
    def rotateAnticlockwise(self):
        self.Grid[gen[0]][0]='.'
        self.Grid[gen[1]][n-1]='.'
        for i in range(int(self.n/2)):
            for j in range(i,self.n-i-1):
                temp=self.Grid[i][j]
                self.Grid[i][j]=self.Grid[j][n-1-i]
                self.Grid[j][n-1-i]=self.Grid[n-1-i][n-1-j]
                self.Grid[n-1-i][n-1-j]=self.Grid[n-1-j][i]
                self.Grid[n-1-j][i]=temp
        self.Grid[gen[0]][0]='S'
        self.Grid[gen[1]][n-1]='G'

    #Helper function to generate initial Grid
    def initialGrid(self):
        for i in range(self.n):
            self.Grid.append([])
            for j in range(self.n):
                self.Grid[i].append('.')
                
        for i in range(self.n):
            for j in range(self.n):
                if j==self.start[0] and i==self.start[1]:
                    self.Grid[i][j]='S'
                elif j==self.goal[0] and i==self.goal[1]:
                    self.Grid[i][j]='G'
                elif (i,j) in self.myObstacles:
                    self.Grid[i][j]='#'
                elif (i,j) in self.myRewards:
                    self.Grid[i][j]=self.Reward.val()

     #Function to show Grid               
    def showGrid(self):
        for i in range(self.n):
            for j in range(self.n):
                print(self.Grid[i][j],end=' ')
            print()
                

#Class to generate obstacle
class Obstacle:
    def points(self):
        self.x=random.sample(range(n),1)[0]
        self.y=random.sample(range(n),1)[0]
        return (self.x,self.y)


#Class to generate Reward
class Reward:

    #Function to generate random point
    def points(self):
        self.x=random.sample(range(n),1)[0]
        self.y=random.sample(range(n),1)[0]
        return (self.x,self.y)
    
    #Function to generate random value of reward between 1 to 9 
    def val(self):
        self.value=random.randint(1,9)
        return self.value


#Class to generate and move Player
class Player:
    
    def __init__(self):
        self.Grid=Grid(n)
        self.x=self.Grid.start[0]
        self.y=self.Grid.start[1]

    energy=2*n   #Initial Energy of Player

    #Helper Function
    def helper(self):
        
        if self.Grid.Grid[self.y][self.x]=='#':
            self.energy-=4*n
            self.Grid.Grid[self.y][self.x]='O'
            clear()
            print("Energy=",self.energy)
            self.Grid.showGrid()
            sleep(1)
            self.Grid.Grid[self.y][self.x]='#'
        elif type(self.Grid.Grid[self.y][self.x])==int:
            i=self.Grid.Grid[self.y][self.x]
            self.energy+=i*n
            self.Grid.Grid[self.y][self.x]='O'
            clear()
            print("Energy=",self.energy)
            self.Grid.showGrid()
            sleep(1)
            self.Grid.Grid[self.y][self.x]=i
        elif self.Grid.Grid[self.y][self.x]=='G':
            clear()
            print("Energy=",self.energy)
            self.Grid.showGrid()
            return 
        else:
            self.Grid.Grid[self.y][self.x]='O'
            self.energy-=1
            clear()
            print("Energy=",self.energy)
            self.Grid.showGrid()
            sleep(1)
            self.Grid.Grid[self.y][self.x]='.'
            
    #Function to move the Player    
    def makeMove(self,s):
        s=s.upper()
        for i in s:
            b=s.find(i)
            if i=='R':                                  #For right move
                a=int(s[slice(b+1,b+2)])
                for i in range(a):
                    self.x+=1
                    if self.x==n:
                        self.x=0
                    self.helper()
                    if self.Grid.Grid[self.y][self.x]=='G':
                        return 1
                    elif self.energy<=0:
                        
                        print("Player Looses")
                        return 
            if i=='D':                                  #For down move
                a=int(s[slice(b+1,b+2)])
                for i in range(a):
                    self.y+=1
                    if self.y==n:
                        self.y=0
                    self.helper()
                    if self.Grid.Grid[self.y][self.x]=='G':
                        return 1
                    elif self.energy<=0:
                        print("Player Looses")
                        return 
            if i=='L':                                  #For Left move
                a=int(s[slice(b+1,b+2)])
                for i in range(a):
                    self.x-=1
                    self.helper()
                    if self.Grid.Grid[self.y][self.x]=='G':
                        return 1
                    elif self.energy<=0:
                        print("Player Looses")
                        return 
            if i=='U':                                  #For Up move
                a=int(s[slice(b+1,b+2)])
                for i in range(a):
                    self.y-=1
                    self.helper()
                    if self.Grid.Grid[self.y][self.x]=='G':
                        return 1
                    elif self.energy<=0:
                        print("Player Looses")
                        return
            if i=='C':                                  #To rotate grid clockwise
                a=int(s[slice(b+1,b+2)])
                for i in range(a):
                    self.Grid.Grid[self.y][self.x]='.'
                    self.Grid.rotateClockwise()
                    if self.Grid.Grid[self.y][self.x]=='#':
                        print("Can't rotate the grid")
                        input()
                        self.Grid.rotateAnticlockwise()
                    self.Grid.Grid[self.y][self.x]='O'
                    sleep(1)
                    self.energy-=n//3
                    clear()
                    print("Energy=",self.energy)
                    self.Grid.showGrid()
                    self.Grid.Grid[self.y][self.x]='.'
                    
            if i=='A':                                  #To rotate grid anticlockwise
                a=int(s[slice(b+1,b+2)])
                for i in range(a):
                    self.Grid.Grid[self.y][self.x]='.'
                    self.Grid.rotateAnticlockwise()
                    if self.Grid.Grid[self.y][self.x]=='#':
                        print("Can't rotate the grid")
                        input()
                        self.Grid.rotateClockwise()
                    self.Grid.Grid[self.y][self.x]='O'
                    sleep(1)
                    self.energy-=n//3
                    clear()
                    print("Energy=",self.energy)
                    self.Grid.showGrid()
                    self.Grid.Grid[self.y][self.x]='.'



P=Grid(n) #Creating object of Grid class
P.obs()     #Calling obs function to create obstacle
P.rew()     #Calling rew function to create rewards
P.initialGrid() #Calling initialGrid to create grid
P.showGrid()    #Calling showGrid to print the Grid

T=Player() #creating object of Player

while T.energy>=0:  #Making moves unless player wins or looses
    S=input("Input the move")
    if T.makeMove(S)==1:
        print("Player Wins")
        break

