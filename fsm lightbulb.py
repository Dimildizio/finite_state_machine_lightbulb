'lightbulb'


from random import randint
from time import sleep


class State:
    pass


class LightOn(State):
    def Execute(self):
        print('light is ON!')


class LightOff(State):
    def Execute(self):
        print('light is OFF!')


class Transitions:
    def __init__(self, toState):
        self.toState = toState

    def Execute(self):
        print ('Transitioning...')



class SimpleFSM:
    def __init__(self, char):
        self.char = char
        self.state = {}             #store all states
        self.transitions = {}       #store all trasitions
        self.curState = None        #current state
        self.curTrans = None        #current transition


    def set_state(self, stateName):
        self.curState = self.state[stateName]

    def transition(self, transName):
        self.curTrans = self.transitions[transName]

    def Execute(self):
        if self.curTrans:
            self.curTrans.Execute()
            self.set_state(self.curTrans.toState)
            self.curTrans = None
        self.curState.Execute()


class Char:
    def __init__(self):
        self.FSM = SimpleFSM(self)
        self.LightOn = True

if __name__ == '__main__':
    light = Char()
    light.FSM.state['On'] = LightOn()
    light.FSM.state['Off'] = LightOff()
    light.FSM.transitions['toOn'] = Transitions('On')
    light.FSM.transitions['toOff'] = Transitions('Off')

    light.FSM.set_state('On')

    for i in range(20):
        sleep(1)
        if randint(0,2):
            if light.LightOn:
                light.FSM.transition('toOff')
                light.LightOn = False
            else:
                light.FSM.transition('toOn')
                light.LightOn = True
        light.FSM.Execute()






