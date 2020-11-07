import main_solver
import unittest

class Testhw2(unittest.TestCase):

    def test_num_placements_all(self):
        self.assertEqual(main_solver.num_placements_all(4), 1820)

    def test_num_placements_one_per_row(self):
        self.assertEqual(main_solver.num_placements_one_per_row(4), 256)

    def test_n_queens_valid(self):
        self.assertEqual(main_solver.n_queens_valid([0, 2]), True)
        self.assertEqual(main_solver.n_queens_valid([0, 3, 1]), True)

    def test_n_queens_solutions(self):
        solution = main_solver.n_queens_solutions(4)
        self.assertEqual(next(solution), [1, 3, 0, 2])
        self.assertEqual(len(list(main_solver.n_queens_solutions(8))), 92)
