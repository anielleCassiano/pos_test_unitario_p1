

class User:
    def __init__(self, name, job):
        self.name = name
        self.job = job

    def __str__(self):
        return f'name: {self.name}, job: {self.job}'
