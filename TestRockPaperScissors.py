import unittest
import rock_paper_scissors

class TestRockPaperScissors(unittest.TestCase):

    def test_get_who_won(self):
        self.assertEqual(0, rock_paper_scissors.get_who_won("R", "R"))
        self.assertEqual(1, rock_paper_scissors.get_who_won("R", "S"))
        self.assertEqual(2, rock_paper_scissors.get_who_won("R", "P"))
        self.assertEqual(2, rock_paper_scissors.get_who_won("S", "R"))
        self.assertEqual(0, rock_paper_scissors.get_who_won("S", "S"))
        self.assertEqual(1, rock_paper_scissors.get_who_won("S", "P"))
        self.assertEqual(1, rock_paper_scissors.get_who_won("P", "R"))
        self.assertEqual(2, rock_paper_scissors.get_who_won("P", "S"))
        self.assertEqual(0, rock_paper_scissors.get_who_won("P", "P"))


if __name__ == '__main__':
    unittest.main()
