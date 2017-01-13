class State:
    def __init__(self, values=None, parent=None): #values: list of lists, moves: list of states, parent: state
       self.values = values
       self.parent = None
    def print_state(self):
        for row in self.values:
            for col in row:
                print col,
            print("\n")
    def makeState(self, nw, n, ne, w, c, e, sw, s, se):
        self.values = [[nw, n, ne], [w, c, e], [sw, s, se]]
    def is_goal(self, goal):
        # goal = State()
        #return self.values == [[1,2,3],[4,5,6],[7,8," "]]
        return self.values == goal.values
    def copy_values(self): #self is a state
        copy = State()
        copy.values = [[0,0,0],[0,0,0],[0,0,0]]
        for i in range(len(copy.values)):
            for j in range(len(copy.values[i])):
                copy.values[i][j] = self.values[i][j]
        copy.parent = self
        return copy
    def hash(self):
        hashed = ""
        for i in range(len(self.values)):
            for j in range(len(self.values[i])):
                hashed += str(self.values[i][j])
        return hashed
    def possible_moves(self):
        moves = []
        for i in range(len(self.values)):
            for j in range(len(self.values[i])):
                if self.values[i][j] == " ":
                    if i != 2:
                        move1 = self.copy_values()
                        temp = move1.values[i+1][j]
                        move1.values[i+1][j] = move1.values[i][j]
                        move1.values[i][j] = temp
                        moves.append(move1)
                    if i != 0:
                        move2 = self.copy_values()
                        temp = move2.values[i-1][j]
                        move2.values[i-1][j] = move2.values[i][j]
                        move2.values[i][j] = temp
                        moves.append(move2)
                    if j != 2:
                        move3 = self.copy_values()
                        temp = move3.values[i][j+1]
                        move3.values[i][j+1] = move3.values[i][j]
                        move3.values[i][j] = temp
                        moves.append(move3)
                    if j != 0:
                        move4 = self.copy_values()
                        temp = move4.values[i][j-1]
                        move4.values[i][j-1] = move4.values[i][j]
                        move4.values[i][j] = temp
                        moves.append(move4)
        return moves
    def get_path(self):
        if not(self.parent == None):
            self.print_state()
            print("\n")
            self.parent.get_path()
    def count_depth(self):
    #count the depth of the path
        depth = 0
        if not(self.parent == None):
            depth += 1
            self.parent.count_depth()
        return depth
    def uninformed_search(self, goal, limit):  #self is a state
        current = self.copy_values()
        open_state = [current]
        close_state = {}
        count = 0
        for l in range(limit):
            open_temp = []
            for s in open_state:
                if s.hash() not in close_state:
                    if s.is_goal(goal):
                        s.get_path()
                        return 0
                    open_temp.append(s)
                    close_state[s.hash()] = True
            open_state = []
            for t in open_temp:
                open_state.extend(t.possible_moves())
            count += 1
            print("run time: {} times".format(count))
    def informed_search(self, goal, limit):  #self is a state
        #goal = State(values=[[1,2,3],[4,5,6],[7,8," "]])
        current = self.copy_values()
        open_state = [current]
        close_state = {}
        count = 0
        best = []
        for l in range(limit):
            heuristic_ls = {}
            for num in range(0,len(best)):
                open_state.extend(best[num].possible_moves())
                open_state.pop(num)
                close_state[best[num].hash()] = 0
            best = []
            open_state = [new for new in open_state if new.hash() not in close_state]
            for s in open_state:
                if s.is_goal(goal):
                    s.get_path()
                    return 0
                heuristic_ls[s] = heuristic(s.values, goal.values) + s.count_depth()
            minValue = min(heuristic_ls.values())
            best = [key for key in heuristic_ls if heuristic_ls[key] == minValue]
            j = 0
            for i in best:
                open_state.remove(i)
                open_state.insert(j, i)
                j += 1
            count += 1
            print("run time: {} times".format(count))

def heuristic2(matrix, goal):  #args are state.values
#calculates # of blocks out of position
    count = 0
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            if(matrix[i][j] != " " and matrix[i][j] != goal[i][j]):
                count += 1
    return count
#Heuristic Procedure
def heuristic(matrix, goal):  #args are state.values
# Calculates how far each tile is from its goal state, and sums those distances
    sum = 0
    for i in range(0, len(goal)):
        for j in range(0, len(goal)):
            tile = goal[i][j]
            for k in range(0, len(matrix)):
                for l in range(0, len(matrix)):
                    if matrix[k][l] == tile:
                        sum += (k - i) * (k - i) + (j - l) * (j - l)
    return sum
def testUninformedSearch(init, goal, limit):
    init.uninformed_search(goal, limit)
def testInformedSearch(init, goal, limit):
    init.informed_search(goal, limit)

#test
test = State(values = [[6," ",1],[2,3,7],[5,4,8]])
test2 = State(values = [[7,8,6],[4,3," "],[2,5,1]])
goal = State(values = [[1,2,3],[4,5,6],[7,8," "]])
#test.informed_search(goal)
#test.uninformed_search(goal)
testUninformedSearch(test2, goal, 30)
testInformedSearch(test, goal, 300)
