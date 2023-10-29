import SimulationController
import ChallengeView
import GameModel

class ChallengeController(SimulationController.SimulationController):
    def __init__(self):
        super().__init__(self)

    def setModules(self):
        self.model = GameModel.Model(self.cell_count, self.cell_count)
        self.view = ChallengeView.ChallengeView(self, self.cell_count)

controller = ChallengeController()