# Create a Controller class to connect the GUI and the model
class PyCalcCtrl:
    """PyCalc Controller class."""
    def __init__(self, view):
        """Controller initializer."""
        self._view = view
        # Connect signals and slots
        self._connectSignals()

    def _buildExpression(self, sub_exp):
        """Build expression."""
        expression = self._view.displayText() + sub_exp
        self._view.setDisplayText(expression)

    def _connectSignals(self):
        """Connect signals and slots."""
        for btnText, btn in self._view.buttons.items():
            if btnText not in {'=', 'C'}:
                btn.clicked.connect(partial(self._buildExpression, btnText))

        self._view.buttons['C'].clicked.connect(self._view.clearDisplay)
    def main():
       """Main function."""
      # Create an instance of QApplication
      pycalc = QApplication(sys.argv)
      # Show the calculator's GUI
      view = PyCalcUi()
      view.show()
      # Create instances of the model and the controller
      PyCalcCtrl(view=view)
      # Execute calculator's main loop
      sys.exit(pycalc.exec_())
