from src.models.store import Store
from src.models.user import User


class ServiceUser:
    def __init__(self):
        self.store = Store()

    def add_user(self, name, job):
        if name is None or job is None:
            return 'Usuário não adicionado'

        for user in self.store.database:
            if name == user.name:
                return 'Nome adicionado já existe'

        if name is not None and job is not None:
            if type(name) == str and type(job) == str:
                user = User(name=name, job=job)
                self.store.database.append(user)
                return 'Usuário adicionado'
            else:
                return 'Usuário não adicionado'

    def list(self):
        if len(self.store.database) <= 0:
            return 'Não há pessoas cadastradas'

        return self.store.database

    def delete_user(self, name):
        for user_database in self.store.database:
            if name == user_database.name:
                self.store.database.remove(user_database)
                return 'Usuário removido com sucesso'

        return 'Usuário não encontrado'

    def update_user(self, name, job):
        for user_database in self.store.database:
            if name == user_database.name:
                index = self.store.database.index(user_database)
                user_database.name = name
                user_database.job = job
                self.store.database[index] = user_database

                return 'Job atualizado com sucesso'

    ### TODO
    # recuperar o nome da pessoa dado o trabalho dela
    def get_user(self, job):
        for user_database in self.store.database:
            if job == user_database.job:
                return user_database.name
