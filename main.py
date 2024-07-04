import tkinter as tk
from tkinter import messagebox

class SudokuSolver:
    def __init__(self, root):
        self.root = root
        self.root.title("Sudoku Solver")

        self.cells = [[None for _ in range(9)] for _ in range(9)]
        self.create_grid()

        solve_button = tk.Button(self.root, text="Solve", command=self.solve)
        solve_button.grid(row=10, column=4, columnspan=2, pady=10)

    def create_grid(self):
        for row in range(9):
            for col in range(9):
                cell = tk.Entry(self.root, width=5, justify='center', font=('Arial', 14))
                cell.grid(row=row, column=col, padx=1, pady=1)
                self.cells[row][col] = cell

    def get_grid(self):
        grid = []
        for row in range(9):
            current_row = []
            for col in range(9):
                value = self.cells[row][col].get()
                if value == '':
                    current_row.append(0)
                else:
                    current_row.append(int(value))
            grid.append(current_row)
        return grid

    def set_grid(self, grid):
        for row in range(9):
            for col in range(9):
                if grid[row][col] != 0:
                    self.cells[row][col].delete(0, tk.END)
                    self.cells[row][col].insert(0, str(grid[row][col]))

    def is_valid(self, grid, row, col, num):
        for x in range(9):
            if grid[row][x] == num:
                return False
        for x in range(9):
            if grid[x][col] == num:
                return False
        start_row = row - row % 3
        start_col = col - col % 3
        for i in range(3):
            for j in range(3):
                if grid[i + start_row][j + start_col] == num:
                    return False
        return True

    def solve_sudoku(self, grid, row, col):
        if row == 8 and col == 9:
            return True
        if col == 9:
            row += 1
            col = 0
        if grid[row][col] > 0:
            return self.solve_sudoku(grid, row, col + 1)
        for num in range(1, 10):
            if self.is_valid(grid, row, col, num):
                grid[row][col] = num
                if self.solve_sudoku(grid, row, col + 1):
                    return True
            grid[row][col] = 0
        return False

    def solve(self):
        grid = self.get_grid()
        if self.solve_sudoku(grid, 0, 0):
            self.set_grid(grid)
        else:
            messagebox.showinfo("Sudoku Solver", "No solution exists")

if __name__ == "__main__":
    root = tk.Tk()
    app = SudokuSolver(root)
    root.mainloop()
