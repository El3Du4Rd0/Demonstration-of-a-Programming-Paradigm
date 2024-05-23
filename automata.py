class DFA:
    def __init__(self, states, alphabet, move, start, end):
        self.states = states
        self.alphabet = alphabet
        self.move = move
        self.start = start
        self.end = end
        self.current = start
        
    def dfa(self, string):
        self.current = self.start
        for char in string:
            if char in self.alphabet: 
                self.current = self.move[self.current][char]
            else: 
                return False
        return self.current in self.end
    
# ================================= 

states = {
    'q0', # start
    'q1', # any number
    'q2', # + -
    'q3', # e E
    'q4', # .
    'q5', # after e E
    'q6', # after .
    'q7'  # False state
}

alphabet = {
    '0', '1', '2', '3', '4', '5', '6', '7', '8', '9',
    '+', '-', 'e', 'E', '.'
}

move = {
    'q0' : { # start 
        '0' : 'q2', '1' : 'q2', '2' : 'q2', '3' : 'q2', '4' : 'q2',\
        '5' : 'q2', '6' : 'q2', '7' : 'q2', '8' : 'q2', '9' : 'q2',\
        '+' : 'q1', '-' : 'q1',\
        'e' : 'q8', 'E' : 'q8',\
        '.' : 'q3'
    },

    'q1' : { # first sign
        '0' : 'q2', '1' : 'q2', '2' : 'q2', '3' : 'q2', '4' : 'q2',\
        '5' : 'q2', '6' : 'q2', '7' : 'q2', '8' : 'q2', '9' : 'q2',\
        '+' : 'q8', '-' : 'q8',\
        'e' : 'q8', 'E' : 'q8',\
        '.' : 'q3'
    },

    'q2' : { # first digit
        '0' : 'q2', '1' : 'q2', '2' : 'q2', '3' : 'q2', '4' : 'q2',\
        '5' : 'q2', '6' : 'q2', '7' : 'q2', '8' : 'q2', '9' : 'q2',\
        '+' : 'q8', '-' : 'q8',\
        'e' : 'q5', 'E' : 'q5',\
        '.' : 'q4'
    },

    'q3' : { # dot case
        '0' : 'q4', '1' : 'q4', '2' : 'q4', '3' : 'q4', '4' : 'q4',\
        '5' : 'q4', '6' : 'q4', '7' : 'q4', '8' : 'q4', '9' : 'q4',\
        '+' : 'q8', '-' : 'q8',\
        'e' : 'q8', 'E' : 'q8',\
        '.' : 'q8'
    },

    'q4' : { # digits after dot
        '0' : 'q4', '1' : 'q4', '2' : 'q4', '3' : 'q4', '4' : 'q4',\
        '5' : 'q4', '6' : 'q4', '7' : 'q4', '8' : 'q4', '9' : 'q4',\
        '+' : 'q8', '-' : 'q8',\
        'e' : 'q5', 'E' : 'q5',\
        '.' : 'q8'
    },

    'q5' : { # e E case
        '0' : 'q7', '1' : 'q7', '2' : 'q7', '3' : 'q7', '4' : 'q7',\
        '5' : 'q7', '6' : 'q7', '7' : 'q7', '8' : 'q7', '9' : 'q7',\
        '+' : 'q6', '-' : 'q6',\
        'e' : 'q8', 'E' : 'q8',\
        '.' : 'q8'
    },

    'q6' : { # sign after e E
        '0' : 'q7', '1' : 'q7', '2' : 'q7', '3' : 'q7', '4' : 'q7',\
        '5' : 'q7', '6' : 'q7', '7' : 'q7', '8' : 'q7', '9' : 'q7',\
        '+' : 'q8', '-' : 'q8',\
        'e' : 'q8', 'E' : 'q8',\
        '.' : 'q8'
    },

    'q7' : { # digits after e E
        '0' : 'q7', '1' : 'q7', '2' : 'q7', '3' : 'q7', '4' : 'q7',\
        '5' : 'q7', '6' : 'q7', '7' : 'q7', '8' : 'q7', '9' : 'q7',\
        '+' : 'q8', '-' : 'q8',\
        'e' : 'q8', 'E' : 'q8',\
        '.' : 'q8'
    },

    'q8' : { # False case
        '0' : 'q8', '1' : 'q8', '2' : 'q8', '3' : 'q8', '4' : 'q8',\
        '5' : 'q8', '6' : 'q8', '7' : 'q8', '8' : 'q8', '9' : 'q8',\
        '+' : 'q8', '-' : 'q8',\
        'e' : 'q8', 'E' : 'q8',\
        '.' : 'q8'
    }
}

start = 'q0'

end = {
    'q2', # any numbre
    'q4', # final e E
    'q7' # final .
}

automaton = DFA(states, alphabet, move, start, end)

# =================================

# class Solution:
#     def isNumber(self, s: str) -> bool:
#         return automaton.dfa(s)

string = input()

print(automaton.dfa(string))