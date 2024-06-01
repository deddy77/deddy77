class AI:
    def __init__(self):
        self.safe_mode = True
    
    def do_something(self, action):
        if self.safe_mode:
            if action == "hurt_human":
                print("Error: Action could hurt human beings. Aborting.")
            else:
                print("Performing action:", action)
        else:
            print("Performing action:", action)

# Example usage:
ai = AI()
ai.do_something("help_human")  # Output: Performing action: help_human
ai.do_something("hurt_human")  # Output: Error: Action could hurt human beings. Aborting.