from draw_output import *
import heapq

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

def get_neighbours(current_position, visited_nodes):
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
    visited_nodes=  [[0 for i in range(num_columns)] for j in range(num_rows)]

    open_queue.append(node)
    total_cost = 0

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
        total_cost += 1

        #Check to see if chosen node is end node
        path.append(pos)

        if pos == endpos:
            final_node = (pos,path)
            path_cost = len(path)
            return final_node, visited_nodes, path_cost, total_cost

        # Add neighbours coordinates
        neighbours = get_neighbours(pos, visited_nodes)

        
        
        #Create nodes for each neighbour. Add neighbours to closed queue
        for neighbour in neighbours:
            if neighbour != None:
                new_node = (neighbour,path[:])
                open_queue.append(new_node)


def dfs_search(node,endpos):
    # Add starting node
    open_queue = []
    visited_nodes=  [[0 for i in range(num_columns)] for j in range(num_rows)]

    open_queue.append(node)
    total_cost = 0

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
        total_cost +=1


        #Check to see if chosen node is end node
        path.append(pos)

        if pos == endpos:
            final_node = (pos,path)
            path_cost = len(path)
            return final_node, visited_nodes, path_cost, total_cost

        # Add neighbours coordinates
        neighbours = get_neighbours(pos, visited_nodes)

        
        
        #Create nodes for each neighbour. Add neighbours to closed queue
        for neighbour in neighbours:
            if neighbour != None:
                new_node = (neighbour,path[:])
                open_queue.append(new_node)


def A_star(node,endpos):
    # Create a heapq
    open_queue = []
    heapq.heapify(open_queue)


    #Set up visited nodes matrix
    visited_nodes=  [[0 for i in range(num_columns)] for j in range(num_rows)]

    # Create and add initial node
    astar_node = (0,node)
    heapq.heappush(open_queue, astar_node)
    total_cost = 0


    #G(n) is given by the current cost so far for n, h(n) is cost to endpos from n, f(n) is esitmated total cost of path through n

    # Use Manhattan distance as an acceptable heuristic function

    while open_queue:
        #Pop out from closed queue
        astar_pop = heapq.heappop(open_queue)


        # Set local vars
        popped_node = astar_pop[1]
        path = popped_node[1]
        pos = popped_node[0]

        #Check to see if already visited
        curr_row = pos[0]
        curr_column = pos[1]
        if (visited_nodes[curr_row][curr_column] == 1):
            continue

        #Set node as visited
        visited_nodes[curr_row][curr_column] = 1
        total_cost +=1


        #Add current position to the path
        path.append(pos)

        #Check to see if current node is end node
        path_cost = len(path)
        if pos == endpos:
            final_node = (pos,path)
            return final_node, visited_nodes, path_cost, total_cost



        # When evaluating manhattan distance, we need to add nodes to the queue, but we need to add 
        # The node, along with its f(n) so that we can organise according to its f(n) value. 
        # To do this, we calculate the f(n) of each item being added to the queue when its added, and
        # we organise it by that value.



        # Add neighbours coordinates to queue
        neighbours = get_neighbours(pos, visited_nodes)
        for neighbour in neighbours:
            if neighbour != None:
                #Evaluate Manhattan distance
                man_dist = (abs(endpos[0]-curr_row) + abs(endpos[1]-curr_column))
                f_n = man_dist + path_cost
                new_node = (neighbour, path[:])
                new_astar_node = (f_n, new_node)
                heapq.heappush(open_queue, new_astar_node)




def main():

    #Define variables for positions
    start_pos = (11,2)
    E1 = (19,23)
    E2 = (21,2)
    null_pos = (0,0)
    final_pos = (24,24)
    start_to_end = (null_pos,[])
    S_to_E1 = (start_pos,[])
    S_to_E2 = (start_pos, [])

    # final_node, visited_nodes, path_cost, total_cost = bfs_search(S_to_E1, E1)
    # print("Path taken", final_node[1])
    # print("Final Path Cost:", path_cost)
    # print("Total Cost", total_cost)
    # print()
    ## PERFORM BFS
    # FIRST RUN FROM S TO E1 
    # PATH TAKEN: Path taken [(11, 2), (12, 2), (13, 2), (14, 2), (15, 2), (16, 2), (16, 3), (16, 4), 
    #                         (16, 5), (16, 6), (16, 7), (16, 8), (16, 9), (17, 9), (17, 10), (17, 11), 
    #                         (18, 11), (19, 11), (19, 12), (19, 13), (19, 14), (19, 15), (19, 16), 
    #                         (19, 17), (19, 18), (19, 19), (19, 20), (19, 21), (19, 22), (19, 23)]
    # PATH COST: 30
    # TOTAL VISITING COST: 379

    # final_node, visited_nodes, path_cost, total_cost = bfs_search(S_to_E2, E2)
    # print("Path taken", final_node[1])
    # print("Final Path Cost:", path_cost)
    # print("Total Cost", total_cost)
    # print()
    # SECOND RUN FROM S TO E2
    # PATH TAKEN: [(11, 2), (12, 2), (13, 2), (14, 2), (15, 2), (16, 2), (16, 3), (16, 4), (16, 5), 
    #              (16, 6), (16, 7), (17, 7), (18, 7), (19, 7), (19, 6), (19, 5), (19, 4), (19, 3), 
    #              (19, 2), (20, 2), (21, 2)]
    #
    # PATH COST: 21
    # TOTAL VISITNG COST: 260

    # final_node, visited_nodes, path_cost, total_cost = bfs_search(start_to_end, final_pos)
    # print("Path taken", final_node[1])
    # print("Final Path Cost:", path_cost)
    # print("Total Cost", total_cost)
    # print()
    # THIRD RUN FROM (0,0) TO (24,24)
    # PATH TAKEN: [(0, 0), (1, 0), (2, 0), (3, 0), (3, 1), (3, 2), (3, 3), (4, 3), (5, 3), (6, 3), 
    #              (6, 4), (6, 5), (7, 5), (8, 5), (9, 5), (10, 5), (11, 5), (12, 5), (13, 5), 
    #              (14, 5), (15, 5), (16, 5), (16, 6), (16, 7), (16, 8), (16, 9), (17, 9), (17, 10),
    #              (17, 11), (18, 11), (19, 11), (20, 11), (21, 11), (22, 11), (23, 11), (23, 12), 
    #              (23, 13), (23, 14), (23, 15), (23, 16), (23, 17), (23, 18), (23, 19), (24, 19), 
    #              (24, 20), (24, 21), (24, 22), (24, 23), (24, 24)]
    # PATH COST: 49
    # TOTAL VISITNG COST: 448
    

    ## PERFORM DFS
    # final_node, visited_nodes, path_cost, total_cost = dfs_search(S_to_E1, E1)
    # print("Path taken", final_node[1])
    # print("Final Path Cost:", path_cost)
    # print("Total Cost", total_cost)
    # print()
    # FIRST RUN FROM S TO E1
    # PATH TAKEN: [(11, 2), (11, 2), (11, 3), (12, 3), (12, 4), (12, 5), (12, 6), (12, 7), (12, 8),
    #              (12, 9), (13, 9), (13, 8), (13, 7), (13, 6), (13, 5), (13, 4), (13, 3), (13, 2), 
    #              (13, 1), (13, 0), (14, 0), (14, 1), (14, 2), (14, 3), (14, 4), (14, 5), (14, 6), 
    #              (14, 7), (15, 7), (15, 8), (15, 9), (16, 9), (17, 9), (17, 10), (17, 11), (17, 12),
    #              (17, 13), (17, 14), (17, 15), (17, 16), (17, 17), (17, 18), (17, 19), (17, 20), 
    #              (17, 21), (17, 22), (17, 23), (17, 24), (18, 24), (18, 23), (18, 22), (18, 21), 
    #              (19, 21), (19, 22), (19, 23)]
    # PATH COST: 55
    # TOTAL VISITNG COST: 100

    # final_node, visited_nodes, path_cost, total_cost = dfs_search(S_to_E2, E2)
    # print("Path taken", final_node[1])
    # print("Final Path Cost:", path_cost)
    # print("Total Cost", total_cost)
    # print()
    # FIRST RUN FROM S TO E1
    # PATH TAKEN: [(11, 2), (11, 2), (11, 3), (12, 3), (12, 4), (12, 5), (12, 6), (12, 7), (12, 8), 
    #              (12, 9), (13, 9), (13, 8), (13, 7), (13, 6), (13, 5), (13, 4), (13, 3), (13, 2), 
    #              (13, 1), (13, 0), (14, 0), (14, 1), (14, 2), (14, 3), (14, 4), (14, 5), (14, 6), 
    #              (14, 7), (15, 7), (15, 8), (15, 9), (16, 9), (16, 8), (16, 7), (17, 7), (18, 7), 
    #              (18, 6), (18, 5), (18, 4), (18, 3), (18, 2), (18, 1), (18, 0), (19, 0), (19, 1), 
    #              (19, 2), (20, 2), (20, 1), (20, 0), (21, 0), (21, 1), (21, 2)]
    # PATH COST: 52
    # TOTAL VISITNG COST: 77

    # final_node, visited_nodes, path_cost, total_cost = dfs_search(start_to_end, final_pos)
    # print("Path taken", final_node[1]) 
    # print("Final Path Cost:", path_cost)
    # print("Total Cost", total_cost)
    # print()
    # FIRST RUN FROM S TO E1
    # PATH TAKEN: [(0, 0), (0, 0), (0, 1), (0, 2), (0, 3), (0, 4), (0, 5), (0, 6), (0, 7), (0, 8), 
    #              (0, 9), (0, 10), (0, 11), (0, 12), (0, 13), (0, 14), (0, 15), (0, 16), (0, 17),
    #              (0, 18), (0, 19), (0, 20), (0, 21), (0, 22), (0, 23), (0, 24), (1, 24), (1, 23), 
    #              (1, 22), (1, 21), (1, 20), (2, 20), (2, 21), (2, 22), (2, 23), (2, 24), (3, 24), 
    #              (3, 23), (3, 22), (3, 21), (3, 20), (4, 20), (4, 21), (4, 22), (4, 23), (4, 24), 
    #              (5, 24), (6, 24), (7, 24), (7, 23), (7, 22), (7, 21), (7, 20), (7, 19), (8, 19), 
    #              (8, 20), (9, 20), (9, 19), (10, 19), (10, 20), (11, 20), (11, 19), (12, 19), (12, 20),
    #              (13, 20), (13, 19), (13, 18), (13, 17), (14, 17), (14, 18), (14, 19), (14, 20), 
    #              (14, 21), (15, 21), (15, 22), (16, 22), (16, 23), (17, 23), (17, 24), (18, 24), 
    #              (18, 23), (18, 22), (18, 21), (19, 21), (19, 22), (19, 23), (19, 24), (20, 24), 
    #              (20, 23), (20, 22), (20, 21), (21, 21), (21, 22), (21, 23), (21, 24), (22, 24), 
    #              (22, 23), (22, 22), (22, 21), (23, 21), (23, 22), (23, 23), (23, 24), (24, 24)]
    # PATH COST: 104
    # TOTAL VISITNG COST: 105



    final_node, visited_nodes, path_cost, total_cost = A_star(start_to_end, final_pos)
    print("Path taken", final_node[1]) 
    print("Final Path Cost:", path_cost)
    print("Total Cost", total_cost)
    print()



    maze = MazeDraw('A_STAR S->E1')
    maze.draw(grid_layout, visited_nodes, final_node[1], null_pos, final_pos)
    maze.hold()

    
if __name__ == "__main__":
    main()