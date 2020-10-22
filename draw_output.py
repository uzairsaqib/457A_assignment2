import tkinter as tk

class MazeDraw:
    """Simple grid object for drawing GUI"""

    def __init__(self, title):
        self.master = tk.Tk()
        self.master.title(title)
        self.canvas_length = 500
        self.canvas = tk.Canvas(self.master, width=self.canvas_length, height=self.canvas_length)
        self.canvas.pack()

    def get_canvas_coords(self, row, col, grid_length):
        """Transforms point in the grid (row, col) to (x,y) point for canvas."""
        return (col, grid_length - row - 1)

    def draw_square(self, bottom_left_x, bottom_left_y, side_length, fill):
        self.canvas.create_rectangle(bottom_left_x*side_length, 
                                    bottom_left_y*side_length, 
                                    bottom_left_x*side_length+side_length, 
                                    bottom_left_y*side_length+side_length, 
                                    fill=fill)


    def draw(self, maze, visited, path, start, end):
        cell_length = float(self.canvas_length)/len(maze)
        grid_length = len(maze)
        fill = ''

        # Draw empty/blocked cells in grid
        for r in range(grid_length):
            for c in range(grid_length):
                if visited[r][c] == 1:
                    fill = 'blue'
                elif maze[r][c] == 0:
                    # Empty cell
                    fill = 'white'
                else:
                    # Blocked cell
                    fill = 'black'

                # Flip/rotate to match grid from assignment
                xpos, ypos = self.get_canvas_coords(r, c, grid_length)
                self.draw_square(xpos, ypos, cell_length, fill)

        for node in path:
            xpos, ypos = self.get_canvas_coords(node[0], node[1], grid_length)
            self.draw_square(xpos, ypos, cell_length, 'orange')

        # Fill in start node
        xpos, ypos = self.get_canvas_coords(start[0], start[1], grid_length)
        self.draw_square(xpos, ypos, cell_length, 'green')

        # Fill in end node
        xpos, ypos = self.get_canvas_coords(end[0], end[1], grid_length)
        self.draw_square(xpos, ypos, cell_length, 'red')


    def hold(self):
        self.master.mainloop()

