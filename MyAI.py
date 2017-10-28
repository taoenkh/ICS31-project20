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
        self.first = [0,0]
        self.count = 0
        self.moved = []
        # ======================================================================
        # YOUR CODE ENDS
        # ======================================================================

    def getAction( self, stench, breeze, glitter, bump, scream ):
        # ======================================================================
        # YOUR CODE BEGINS
        # ======================================================================
        if breeze and len(self.moved) == 0:
            return Agent.Action.CLIMB
        elif stench and len(self.moved) == 0:
            return Agent.Action.CLIMB
        else:
            if self.count == 0:
                self.count += 1
                self.moved.append(1)
                return Agent.Action.FORWARD
            elif self.count == 1:
                self.count += 1
                self.moved.append(1)
                return Agent.Action.TURN_LEFT
            elif self.count == 2:
                self.count += 1
                self.moved.append(1)
                return Agent.Action.TURN_LEFT
            elif self.count == 3:
                self.count += 1
                self.moved.append(1)
                return Agent.Action.GRAB
            elif self.count == 4:
                self.count += 1
                self.moved.append(1)
                return Agent.Action.FORWARD
            elif self.count == 5:
                self.count += 1
                self.moved.append(1)
                return Agent.Action.CLIMB

        # ======================================================================
        # YOUR CODE ENDS
        # ======================================================================
    
    # ======================================================================
    # YOUR CODE BEGINS
    # ======================================================================

    
    # ======================================================================
    # YOUR CODE ENDS
    # ======================================================================
