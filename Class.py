from pythomata import SimpleDFA

class minimization(object):
    def __init__(self):
        self.states = {}
        self.path = {}
        self.start_state = ""
        self.finall_states = {}
        self.transitions = {}

    def input_info(self):
        self.states = set()
        print("Enter States by space: ")
        states = [x for x in input().split()]
        self.states = set(states)
        print()
        
        self.path = set()
        print("Enter pathes by space: ")
        path = [x for x in input().split()]
        self.path = set(path)
        print()
        
        self.start_state = input("Enter start state: ")
        print()
        
        self.finall_states = set()
        print("Enter Finall States by space: ")
        finall_states = [x for x in input().split()]
        self.finall_states = set(finall_states)
        print()
        
        for state in self.states:
            self.transitions[state] = {}
            for path in self.path:
                end_state = input("Enter end state that connect with state {} by path {}: ".format(state,path))
                self.transitions[state][path] = end_state
            print()

    def dfa_minimize(self):
        minimization.input_info(self)
        
        dfa = SimpleDFA(self.states,self.path,self.start_state,self.finall_states,self.transitions)

        graph = dfa.minimize().to_graphviz()

        print(graph.render("DFA_Minimized"))
