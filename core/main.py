class HuobzLang:
    def __init__(self):
        self.variables = {}

    def define(self, name, value):
        """Define a new variable."""
        self.variables[name] = value

    def execute(self, command, args):
        """Execute a command."""
        if command == "say":
            print(args)
        elif command == "transfer":
            print(f"Transferring {args['amount']} to {args['address']}")
        else:
            raise ValueError("Unknown command")

# Example usage
lang = HuobzLang()
lang.define("username", "huobz_user")
lang.execute("say", "Welcome to Huobz!")
