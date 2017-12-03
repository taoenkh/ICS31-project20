# ======================================================================
# FILE:        MyAI.py
#
# AUTHOR:      Abdullah Younis
#
# DESCRIPTION: This file contains your agent class, which you will
#              implement. You are responsible for implementing the
#              'getAction' function and any helper methods you feel you
#              need.
#
# NOTES:       - If you are having trouble understanding how the shell
#                works, look at the other parts of the code, as well as
#                the documentation.
#
#              - You are only allowed to make changes to this portion of
#                the code. Any changes to other portions of the code will
#                be lost when the tournament runs your code.
# ======================================================================

from Agent import Agent

class MyAI ( Agent ):

    def __init__ ( self ):
        # ======================================================================
        # YOUR CODE BEGINS
        # ======================================================================
        self.count = 0
        self.backlist = []
        self.moved = []
        self.gold = False #After grabbed gold this becomes true
        self.back = False #After encountered breeze, stench or bump, this becomes true
        self.next = [0,0]  #The current coordinate the agent is on
        self.direction = 0  # right = 0; up = 90; down = 270; left = 180;
        self.goup = False
        #self.safelist = [([0,0],3),([0,1],3),([0,2],3),([0,3],3),([0,4],3)]
        self.row2 = False
    # ======================================================================
    # YOUR CODE ENDS
    # ======================================================================
    def goback(self,actl)->list:
        """
        act1 = [([int,int],int),....]
        :param actl:
        :return:
        """
        turnaround = (actl[-1][0],1)
        backlist = []
        #backlist.append([0,0])
        for i in actl:
            if i[1] == 1:
                backlist.append((i[0],2))
            elif i[1] == 2:
                backlist.append((i[0], 1))
            elif i[1] == 4 or i[1] == 5:
                pass
            elif i[1] == 3:
                backlist.append((i[0],3))
        backlist.append(turnaround)
        return backlist
    def goback1(self,actl):
        turnaround = (actl[-1][0], 1)
        backlist = []
        # backlist.append([0,0])
        for i in actl:
            if i[1] == 1:
                backlist.append((i[0], 2))
            elif i[1] == 2:
                backlist.append((i[0], 1))
            elif i[1] == 4 or i[1] == 5:
                pass
            elif i[1] == 3:
                backlist.append((i[0], 3))
        backlist.append(turnaround)
        backlist.append(turnaround)
        return backlist
    def moveforaward(self):
        if self.direction == 90:
            self.next[0] += 1
        elif self.direction == 270:
            self.next[0] -= 1
        elif self.direction == 180:
            self.next[1] -= 1
        elif self.direction == 0:
            self.next[1] += 1
        return Agent.Action.FORWARD

    def gotgold(self):
        """

        :return: movement grab triggers gold generates a list move movements to move in the future
        """
        self.gold = True
        temp = self.goback1(self.moved)
        self.backlist = temp
        return Agent.Action.GRAB
    def aftergold(self,dire):
        move = ''
        if self.backlist!= []:
            move = self.backlist.pop()
        if self.direction == dire and self.next == [0, 0]:
            return Agent.Action.CLIMB
        if move[1] == 1:
            self.direction += 90
            return Agent.Action.TURN_LEFT
        elif move[1] == 2:
            self.direction -= 90
            return Agent.Action.TURN_RIGHT
        elif move[1] == 3:
            return self.moveforaward()
    def getAction( self, stench, breeze, glitter, bump, scream ):
        # ======================================================================
        # YOUR CODE BEGINS
        # ======================================================================
        if glitter: # After getting the gold gold will be triggered

             # Generates a list of tuples ([0,0],1) means agents is on 0 ,0 next move is forward

            return self.gotgold()
###########################################
        if self.row2:             #From [0,0] goes to the second row
            if glitter:           #if grabbed gold during this move directly go back
                return self.gotgold()
            if self.gold:         # After grabbed gold Start going back

                return self.aftergold(270)       #When the agent moved to [0,0] from upward, then the agent will climb

            if self.back:
                if self.backlist != []:
                    move = self.backlist.pop()             #deletes the last element in backlist and returns a most recent move
                    if self.direction == 270 and self.next == [0,0]:
                        return Agent.Action.CLIMB
                    if move[1] == 1:
                        self.direction += 90
                        return Agent.Action.TURN_LEFT
                    elif move[1] == 2:
                        self.direction -= 90
                        return Agent.Action.TURN_RIGHT
                    elif move[1] == 3:
                        return self.moveforaward()

            if breeze or stench or bump:     #After meet any of these the agent will start go back
                self.back = True
                temp = self.goback(self.moved)
                self.backlist = temp
                self.direction += 90
                return Agent.Action.TURN_LEFT
            if not breeze and not stench and not bump: #If the agent detect nothing
                if self.count == 1:
                    self.count += 1
                    self.moved.append((self.next, 3))
                    return self.moveforaward()
                elif self.count == 2:
                    self.count += 1
                    self.direction -= 90
                    self.moved.append((self.next,2))
                    return Agent.Action.TURN_RIGHT
                elif self.count == 0:           #Turn right since agent came from up  -> facing down  =270
                    self.direction -= 90        # Turn right will make the direction 90 (270-90-90)
                    self.count +=1
                    self.moved.append(((self.next),2))
                    return Agent.Action.TURN_RIGHT
                else:
                    self.moved.append((self.next, 3))
                    return self.moveforaward()
        ##########################################################
        if self.goup:     #Triggers after the agent has explore its right direction
            if glitter:
                return self.gotgold()
            if self.gold:
                return self.aftergold(270)
            if self.back:     # After triggered start go back to 0,0
                if self.backlist != []:
                    move = self.backlist.pop()
                    if self.direction == 270 and self.next == [0,0]:
                        self.row2 = True
                        self.direction -= 90
                        self.moved = []
                        return Agent.Action.TURN_RIGHT
                    if move[1] == 1:
                        self.direction += 90
                        return Agent.Action.TURN_LEFT
                    elif move[1] == 2:
                        self.direction -= 90
                        return Agent.Action.TURN_RIGHT
                    elif move[1] == 3:
                        return self.moveforaward()
            if breeze or stench or bump:                   # After meet one of those start move back (Triggers back)
                self.back = True
                temp = self.goback(self.moved)
                self.backlist = temp
                self.direction += 90
                return Agent.Action.TURN_LEFT
            if not breeze and not stench and not bump:        #The agent will keep go up when its not bumped
                self.moved.append(((self.next),3))
                return self.moveforaward()
        ##########################################################################
        #Initially moving to right
        if self.moved != [] and self.next == [0,0] and not self.gold:   #After going right agent backed to 0,0, but still didn't find the golf
            if not self.goup:                                           #It will trigger goup start going up
                self.goup = True
                self.direction -= 90
                self.moved = []
                self.moved.append(([0,0],2))
                return Agent.Action.TURN_RIGHT
            else:
                self.row2 = True                                        #After going up still did not find gold will go to row2
        if self.gold:                                          # Found gold during going to right
            return self.aftergold(180)
        if self.back :
            if self.backlist !=[]:
                move = self.backlist.pop()
                if move[1] == 1:
                    self.direction +=90
                    return Agent.Action.TURN_LEFT
                elif move[1] == 2:
                    self.direction -= 90
                    return Agent.Action.TURN_RIGHT
                elif move[1] == 3:
                    return self.moveforaward()
        if self.next == [0,0]:
            if breeze or stench:
                return Agent.Action.CLIMB
            else:
                self.next = [0,1]
                self.moved.append((self.next,3))
                return Agent.Action.FORWARD
        if breeze or stench or bump:
            self.back = True
            temp = self.goback(self.moved)
            self.backlist = temp
            self.direction += 90
            return Agent.Action.TURN_LEFT
        if not breeze and not stench and not bump:
            self.next[1] += 1
            self.moved.append((self.next,3))
            return Agent.Action.FORWARD
        # ======================================================================
        # YOUR CODE ENDS
        # ======================================================================

        # ======================================================================
        # YOUR CODE BEGINS
        # ======================================================================


        # ======================================================================
        # YOUR CODE ENDS
        # ======================================================================

