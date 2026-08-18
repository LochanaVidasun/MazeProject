MAZE = [  # 0 = wall , 1 = path
    [0, 0, 0, 0, 0],
    [0, 1, 1, 1, 0],
    [0, 1, 1, 1, 0],
    [0, 0, 0, 0, 0],
]

class Maze:
    """Main Maze class that stores the grid and handles display."""

    def __init__(self, maze):
        """Initialises the maze grid.

        Args:
            maze (list): 2D list representing maze layout.
        """
        self.maze = maze

    def display(self, avatar=None, goal=None):
        """Prints the maze with optional avatar and goal.

        Args:
            avatar (Avatar): The avatar object.
            goal (Goal): The goal object.
        """
        for r in range(len(self.maze)):
            display_row = []
            for c in range(len(self.maze[r])):
                cell = self.maze[r][c]
                if avatar and (r, c) == (avatar.row, avatar.col):
                    display_row.append("A")
                elif goal and (r, c) == (goal.row, goal.col):
                    display_row.append("G")
                elif cell == 1:
                    display_row.append(".")
                else:
                    display_row.append("#")
            print("".join(display_row))
        print()

    def can_move(self, row, col):
        """Checks if a move is valid (inside the maze and not a wall).

        Args:
            row (int): target row.
            col (int): target column.

        Returns:
            bool: True if the move is valid, False otherwise.
        """
        if row < 0 or col < 0:
            return False
        if row >= len(self.maze) or col >= len(self.maze[0]):
            return False
        return self.maze[row][col] == 1


class Goal:
    """Represents the goal position in the maze."""

    def __init__(self, row, col):
        """Initializes the goal position."""
        self.row = row
        self.col = col

    def __repr__(self):
        return f"({self.row}, {self.col})"


class Avatar:
    """Represents the avatar in the maze."""

    def __init__(self, row, col):
        """Initializes the avatar position."""
        self.row = row
        self.col = col

    def move(self, direction, maze):
        """Moves the avatar in the specified direction if valid.

        Args:
            direction (str): One of 'w', 'a', 's', or 'd'.
            maze (Maze): The maze object to check for valid moves.
        """
        new_row, new_col = self.row, self.col
        direction = direction.lower()
        if direction == "w":
            new_row -= 1
        elif direction == "s":
            new_row += 1
        elif direction == "a":
            new_col -= 1
        elif direction == "d":
            new_col += 1
        else:
            print("Please enter W, A, S, or D.")
            return

        if maze.can_move(new_row, new_col):
            self.row, self.col = new_row, new_col
        else:
            print("Invalid move! You hit a wall or moved out of bounds.")

    def collide(self, goal):
        """Checks if the avatar has reached the goal.

        Args:
            goal (Goal): The goal object to check against.

        Returns:
            bool: True if the avatar is at the goal position, False otherwise.
        """
        return self.row == goal.row and self.col == goal.col

    def __repr__(self):
        return f"({self.row}, {self.col})"


def main(maze_layout):

    maze = Maze(maze_layout)
    goal = Goal(2, 3)
    avatar = Avatar(1, 1)

    print("Reach the goal (G)! Use W A S D to move the avatar\n")
    while not avatar.collide(goal):
        maze.display(avatar=avatar, goal=goal)
        move = input("Enter your move (W/A/S/D): ").strip()
        avatar.move(move, maze)

        maze.display(avatar=avatar, goal=goal)
    print("Congratulations! You've reached the goal!")


if __name__ == "__main__":
    main(MAZE)

import tkinter as tk
from PIL import Image, ImageTk
from tkinter import messagebox

class MazeGUI:
    def __init__(self, root, logic):
        self.root = root
        self.logic = logic 
        self.root.wm_title("Maze Game")
        self.root.iconphoto(True, ImageTk.PhotoImage(file= 'my_image.png'))

def main ():
    root = tk.Tk()
    logic = MazeLogic()
    maze_gui=MazeGUI (root,logic)
    root.mainloop()