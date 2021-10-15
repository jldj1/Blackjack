from buttons.button import Button

class TicTacToeBox(Button):
    def __init__(self, screen, x, y, height, width, text, color=(29,29,29)):
        super().__init__(screen, x, y, height, width, text, color)
    
    def setValue(self, value):
        self.text = value;

    def getValue(self):
        options = "OX"
        return self.text if self.text in options else ""
