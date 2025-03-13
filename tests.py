import unittest
from maze import Maze

class Tests(unittest.TestCase):
    def test_maze_create_cells(self):
        num_cols = 12
        num_rows = 10
        m1 = Maze(0, 0, num_rows, num_cols, 10, 10)
        self.assertEqual(
            len(m1._cells),
            num_cols,
        )
        self.assertEqual(
            len(m1._cells[0]),
            num_rows,
        )

    def test_break_entrance_and_exit(self):
        # Create a maze without a window (we're just testing the logic)
        maze = Maze(0, 0, 5, 5, 10, 10)
        
        # Initial state: all cells should have all walls
        entrance_cell = maze._cells[0][0]
        exit_cell = maze._cells[4][4]  # For a 5x5 maze, bottom-right is at (4,4)
        
        # Verify initial state
        self.assertTrue(entrance_cell.has_top_wall)
        self.assertTrue(exit_cell.has_bottom_wall)
        
        # Call the function we're testing
        maze._break_entrance_and_exit()
        
        # Verify that walls were broken
        self.assertFalse(entrance_cell.has_top_wall)
        self.assertFalse(exit_cell.has_bottom_wall)
        
        # All other walls should still be intact
        self.assertTrue(entrance_cell.has_left_wall)
        self.assertTrue(entrance_cell.has_right_wall)
        self.assertTrue(entrance_cell.has_bottom_wall)
        
        self.assertTrue(exit_cell.has_left_wall)
        self.assertTrue(exit_cell.has_right_wall)
        self.assertTrue(exit_cell.has_top_wall)

if __name__ == "__main__":
    unittest.main()
if __name__ == "__main__":
    unittest.main()