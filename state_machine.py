class StateMachine:
    def __init__(self):
        self.state = "Init"

    def transition(self, new_state):
        print(f"Transitioning from {self.state} to {new_state}")
        self.state = new_state

    def run(self, items, process_function):
        try:
            self.transition("Process")
            for item in items:
                process_function(item)
        except Exception as e:
            self.transition("Error")
            print(f"Error encountered: {e}")
        finally:
            self.transition("End")
