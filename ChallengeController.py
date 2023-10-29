import SimulationController
import ChallengeView
import GameModel
import time

class ChallengeController(SimulationController.SimulationController):
    def __init__(self, menu):

        # game properties
        self.player_points = 0
        self.opponent_points = 0
        self.current_blocks = 0
        self.simulation_started = False

        # super class init
        super().__init__(menu)

    def setModules(self):
        self.model = GameModel.Model(self.cell_count, self.cell_count)
        self.view = ChallengeView.ChallengeView(self, self.cell_count)

    def calculate_points(self, model):
        total_points = 0
        for row in model.li:
            for value in row:
                total_points += value

        return total_points
    
    def updatePoints(self):
        self.simulation_started = True

        # updating the point scores
        self.player_points = round(self.calculate_points(self.model.pm), 2)
        self.opponent_points = round(self.calculate_points(self.model.om), 2)

        # updating the challenge view
        self.view.update_score()
        self.player_points = round(self.calculate_points(self.model.pm), 4)
        self.opponent_points = round(self.calculate_points(self.model.om), 4)
        # checking who won
        winner = None
        if self.opponent_points == 0:
            winner = "player"
        elif self.player_points == 0:
            winner = "opponent"
        
        if winner != None:
            self.stop()
            time.sleep(0.5)

            # displaying winner
            if winner == "player":
                self.view.player_win()
            else:
                self.view.opponent_win()

    def onCellUpdate(self):
        self.updatePoints()

    def update(self):
        super().update()

        # updating current blocks
        if self.simulation_started == False:
            self.current_blocks = int(self.calculate_points(self.model.pm))
            self.view.update_max_boxes()
