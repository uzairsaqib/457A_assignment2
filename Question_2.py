grid_layout = [[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
               [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0, 0],
               [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0, 0],
               [0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 1, 1, 1, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0, 0],
               [1, 1, 1, 0, 0, 0, 1, 1, 0, 0, 1, 1, 1, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0, 0],
               [1, 1, 1, 0, 0, 0, 1, 1, 0, 0, 1, 1, 1, 0, 0, 0, 0, 0, 1, 1, 1, 1, 0, 0, 0],
               [0, 0, 1, 0, 0, 0, 1, 1, 0, 0, 1, 1, 1, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 0],
               [0, 0, 1, 1, 1, 0, 1, 1, 0, 0, 1, 1, 1, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0],
               [0, 0, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 1, 0, 0, 0],
               [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 1, 0, 0, 0],
               [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 1, 0, 0, 1, 0, 0, 0],
               [0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 1, 0, 0, 1, 0, 0, 0],
               [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 1, 1, 0, 1, 0, 0, 1, 0, 0, 1],
               [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0, 1, 1, 1, 1],
               [0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 0, 0, 1, 1, 0, 0, 0, 0, 0, 1, 1, 1],
               [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1],
               [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
               [1, 1, 1, 1, 1, 1, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
               [0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0],
               [0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
               [0, 0, 0, 1, 1, 1, 0, 0, 1, 1, 1, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0],
               [0, 0, 0, 1, 1, 1, 0, 0, 1, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0],
               [1, 1, 1, 1, 1, 0, 0, 0, 1, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0],
               [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
               [0, 0, 0, 0, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0, 0, 0]]

num_rows = len(grid_layout)
num_columns = len(grid_layout[0])


visited_nodes=  [[0]*num_columns]*num_rows

#make this input a tuple
def get_neighbours(current_position):
    # I need to check 2 things. Whether the position is OOB or if its blocked
    row = current_position[0]
    column = current_position[1]
    #First, add the top neighbour
    if (current_position[0] == 0):
        up_neighbour = None
    else:
        up_neighbour = (current_position[0]+1, current_position[1])
        if (grid_layout [up_neighbour[0]][up_neighbour[1]] == 1) or (visited_nodes[up_neighbour[0]][up_neighbour[1]] == 1):
            up_neighbour = None
    
    #Down neighbour
    if current_position[0] == 24:
        down_neighbour = None
    else:
        down_neighbour = (current_position[0]-1, current_position[1])
        if (grid_layout [down_neighbour[0]][down_neighbour[1]] == 1) or (visited_nodes [down_neighbour[0]][down_neighbour[1]] == 1):
            down_neighbour = None
    
    #Left neighbour
    if current_position[1] == 0:
        left_neighbour = None
    else:
        left_neighbour = (current_position[0], current_position[1]-1)
        if (grid_layout [left_neighbour[0]][left_neighbour[1]] == 1) or (visited_nodes[left_neighbour[0]][left_neighbour[1]] == 1):
            left_neighbour = None
    
    #Right neighbour
    if current_position[1] == 24:
        right_neighbour = None
    else:
        right_neighbour = (current_position[0], current_position[1]+1)
        if (grid_layout [right_neighbour[0]][right_neighbour[1]] == 1) or (visited_nodes[right_neighbour[0]][right_neighbour[1]] == 1):
            right_neighbour = None

    # Add into an output list
    out_list =[up_neighbour, down_neighbour, left_neighbour, right_neighbour]
    return out_list





## Breath-First Search
#visit all nearby nodes before visitng next nodes
# we can only move up down left right
closed_queue = []
open_queue = [] #make this a list of tuple and add the path taken to get to each node along with the node

def bfs_search(closed_queue, open_queue, node, endpos):
    # Add starting node
    closed_queue.append(node)

    while closed_queue:
        #Pop out from closed queue
        popped_node = closed_queue.pop(0)
        pos = popped_node[0]

        #Set node as visited
        curr_row = pos[0]
        curr_column = pos[1]
        visited_nodes[curr_row][curr_column] = 1


        #Check to see if chosen node is end node
        if pos == endpos:
            return popped_node

        # Add neighbours coordinates
        neighbours = get_neighbours(pos)

        #Set the list of parent nodes
        add_parents = popped_node[1] #list of parents
        add_parents.append(pos) # Append new parent. Now add_parents is our complete list of parent nodes

        #Create nodes for each neighbour. Add neighbours to closed queue
        if neighbours[0] != None:
            up_add = (neighbours[0],add_parents)
            closed_queue.append(up_add)

        if neighbours[1] != None:
            down_add = (neighbours[1],add_parents)
            closed_queue.append(down_add)

        if neighbours[2] != None:
            left_add = (neighbours[2],add_parents)
            closed_queue.append(left_add)

        if neighbours[3] != None:
            right_add = (neighbours[3],add_parents)
            closed_queue.append(right_add)




def main():

    start_pos = (11,2)
    E1 = (23,19)
    # E2 = (3,21)
    starting_node = (start_pos,[])

    result = bfs_search(closed_queue, open_queue, starting_node, E1)
    print("Hold this")

if __name__ == "__main__":
    main()