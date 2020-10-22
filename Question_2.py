from draw_output import *

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


visited_nodes=  [[0 for i in range(num_columns)] for j in range(num_rows)]

def get_neighbours(current_position):
    # I need to check 2 things. Whether the position is OOB or if its blocked
    #First, add the top neighbour
    curr_row = current_position[0]
    curr_column = current_position[1]
    if (curr_row == 0):
        up_neighbour = None
    else:
        up_neighbour = None
        if (grid_layout[curr_row-1][curr_column] != 1):
            if (visited_nodes[curr_row-1][curr_column] != 1):
                up_neighbour = (curr_row-1,curr_column)
    
    #Down neighbour
    if curr_row == 24:
        down_neighbour = None
    else:
        down_neighbour = None
        if (grid_layout [curr_row+1][curr_column] != 1):
            if (visited_nodes [curr_row+1][curr_column] != 1):
                down_neighbour = (curr_row+1,curr_column)
    
    #Left neighbour
    if curr_column == 0:
        left_neighbour = None
    else:
        left_neighbour = None
        if (grid_layout [curr_row][curr_column-1] != 1):
            if (visited_nodes[curr_row][curr_column-1] != 1):
                left_neighbour = (curr_row,curr_column-1)
    
    #Right neighbour
    if curr_column == 24:
        right_neighbour = None
    else:
        right_neighbour = None
        if (grid_layout [curr_row][curr_column+1] != 1): 
            if (visited_nodes[curr_row][curr_column+1] != 1):
                right_neighbour = (curr_row,curr_column+1)

    # Add into an output list
    out_list =[up_neighbour, down_neighbour, left_neighbour, right_neighbour]
    return out_list





## Breath-First Search
#visit all nearby nodes before visitng next nodes
# we can only move up down left right


def bfs_search(node, endpos):
    # Add starting node
    open_queue = []

    open_queue.append(node)
    total_visited = 0

    while open_queue:
        #Pop out from closed queue
        popped_node = open_queue.pop(0)
        path = popped_node[1]
        pos = popped_node[0]

        #Check to see if already visited
        curr_row = pos[0]
        curr_column = pos[1]
        if (visited_nodes[curr_row][curr_column] == 1):
            continue

        #Set node as visited
        visited_nodes[curr_row][curr_column] = 1
        total_visited += 1

        #Check to see if chosen node is end node
        path.append(pos)

        if pos == endpos:
            final_node = (pos,path)
            total_cost = len(path)
            return final_node, visited_nodes, total_cost, total_visited

        # Add neighbours coordinates
        neighbours = get_neighbours(pos)

        
        
        #Create nodes for each neighbour. Add neighbours to closed queue
        for neighbour in neighbours:
            if neighbour != None:
                new_node = (neighbour,path[:])
                open_queue.append(new_node)


def dfs_search(node,endpos):
    # Add starting node
    open_queue = []

    open_queue.append(node)
    total_visited = 0

    while open_queue:
        #Pop out from closed queue
        popped_node = open_queue.pop()
        path = popped_node[1]
        pos = popped_node[0]


        #Check to see if already visited
        curr_row = pos[0]
        curr_column = pos[1]
        if (visited_nodes[curr_row][curr_column] == 1):
            continue

        #Set node as visited
        visited_nodes[curr_row][curr_column] = 1
        total_visited +=1


        #Check to see if chosen node is end node
        path.append(pos)

        if pos == endpos:
            final_node = (pos,path)
            total_cost = len(path)
            return final_node, visited_nodes, total_cost, total_visited

        # Add neighbours coordinates
        neighbours = get_neighbours(pos)

        
        
        #Create nodes for each neighbour. Add neighbours to closed queue
        for neighbour in neighbours:
            if neighbour != None:
                new_node = (neighbour,path[:])
                open_queue.append(new_node)

def main():

    #Define variables for positions
    start_pos = (11,2)
    E1 = (19,23)
    E2 = (21,2)
    null_pos = (0,0)
    final_pos = (24,24)
    starting_node = (start_pos,[])

    
    
    
    #Perform DFS
    result, visited, cost, total_visited = dfs_search(starting_node, E2)

    maze = MazeDraw('DFS')
    maze.draw(grid_layout, visited, result[1], start_pos, E2)
    maze.hold()


    print("Hold this:", cost)
    print("well that took forever", total_visited)

if __name__ == "__main__":
    main()