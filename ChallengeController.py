import SimulationController
import ChallengeView
import GameModel

class ChallengeController(SimulationController.SimulationController):
    def __init__(self, menu):
        super().__init__(menu)

        # game properties
        self.player_points = 0
        self.opponent_points = 0

    def setModules(self):
        self.model = GameModel.Model(self.cell_count, self.cell_count)
        self.view = ChallengeView.ChallengeView(self, self.cell_count)

    def updatePoints(self):
        self.player_points = 0
        self.opponent_points = 0

        # totaling point values
        for y, row in enumerate(self.model.pm.li):
            for x, value in enumerate(row):
                self.player_points += value

        for y, row in enumerate(self.model.om.li):
            for x, value in enumerate(row):
                self.opponent_points += value

        # printing point scores
        print(self.player_points, self.opponent_points)

        # updating the challenge view
        self.view.update_scores()

    def onCellUpdate(self):
        self.updatePoints()