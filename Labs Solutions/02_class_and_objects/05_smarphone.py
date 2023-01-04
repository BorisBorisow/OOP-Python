class Smartphone:
    def __init__(self, memory):
        self.memory = memory
        self.apps = []
        self.memory_used = 0
        self.is_on = False

    def power(self):
        self.is_on = not self.is_on

    # defensive programming
    def install(self, app, app_memory):
        if not self.is_on:
            return f"Turn on your phone to install {app}"

        if self.calculate_memory() < app_memory:
            return f"Not enough memory to install {app}"

        self.memory_used += app_memory
        self.apps.append(app)
        return f"Installing {app}"

    def status(self):
        return f"Total apps: {len(self.apps)}. Memory left: {self.calculate_memory()}"

    def calculate_memory(self):
        return self.memory - self.memory_used