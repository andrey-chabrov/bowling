class Game(object):

    '''The main game class
    '''

    def __init__(self, points):
        self.points = points
        self.pin_count = 10
        self.frame_count = 10

    def _get_score(self):
        # Calculates the total game score.
        # One should wrap this method into a "try...except" block.
        point_ind = 0
        score = 0
        for _ in xrange(self.frame_count):
            if self.points[point_ind] == self.pin_count:
                score += sum(self.points[point_ind:point_ind + 3])
                point_ind += 1
            elif sum(self.points[point_ind:point_ind + 2]) == self.pin_count:
                score += sum(self.points[point_ind:point_ind + 3])
                point_ind += 2
            else:
                score += sum(self.points[point_ind:point_ind + 2])
                point_ind += 2

        return score

    def get_score(self):
        try:
            return self._get_score()
        except IndexError:
            raise ValueError('Point list is too shot.')
