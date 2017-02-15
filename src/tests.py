import unittest

from .game import Game


class TestScore(unittest.TestCase):

    def test_bad_frame_count(self):
        data = (
            [],
            [1, 5, 7],
        )
        for d in data:
            game = Game(d)
            self.assertRaises(ValueError, game.get_score)

    def test_simple_game(self):

        test_data = (
            ((0, 1, 2, 3, 4, 5, 0, 1, 2, 3, 4, 5, 0, 1, 2, 3, 4, 5, 0, 1), 46),
        )

        for data, result in test_data:
            game = Game(data)
            self.assertEquals(game.get_score(), result)

    def test_game_with_spare(self):

        test_data = (
            ((0, 10, 2, 3, 4, 5, 0, 1, 2, 3, 4, 5, 0, 1, 2, 3, 4, 5, 0, 1), 57),
            ((0, 1, 2, 3, 4, 5, 0, 1, 2, 3, 4, 5, 0, 1, 2, 3, 4, 5, 0, 10, 5), 60),
        )

        for data, result in test_data:
            game = Game(data)
            self.assertEquals(game.get_score(), result)

    def test_game_with_strike(self):

        test_data = (
            ((10, 2, 3, 4, 5, 0, 1, 2, 3, 4, 5, 0, 1, 2, 3, 4, 5, 0, 1), 60),
            ((0, 1, 2, 3, 4, 5, 0, 1, 2, 3, 4, 5, 0, 1, 2, 3, 4, 5, 10, 5, 5), 65),
            ((0, 1, 2, 3, 4, 5, 0, 1, 2, 3, 4, 5, 0, 1, 2, 3, 4, 5, 10, 10, 10), 75),
        )

        for data, result in test_data:
            game = Game(data)
            self.assertEquals(game.get_score(), result)

    def test_complex_game(self):

        test_data = (
            ((10, 3, 7, 6, 1, 10, 10, 10, 2, 8, 9, 0, 7, 3, 10, 10, 10), 193),
            ((10, 3, 7, 6, 1, 10, 10, 10, 2, 8, 9, 0, 7, 3, 1, 9, 10), 174),
        )

        for data, result in test_data:
            game = Game(data)
            self.assertEquals(game.get_score(), result)


if __name__ == '__main__':
    unittest.main()
