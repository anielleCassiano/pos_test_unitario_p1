from typing import Union

from src.models.store import Store
from src.models.user import User


class ServiceUser:
    def __init__(self):
        self.store = Store()

    def add_user(self, name, job) -> str:
        """
        Add a new user to the database
        :param name: username
        :param job: user job title
        :return: 'Usuário não adicionado' if the name or job is equal to None, 'Nome adicionado já existe' if the user is already in the databse, 'Usuário adicionado' if the user was saved in the database
        """
        if name is None or job is None:
            return 'Usuário não adicionado'

        user = self.check_user_exists(name)

        if type(user) == str:
            if name is not None and job is not None:
                if type(name) == str and type(job) == str:
                    user = User(name=name, job=job)
                    self.store.database.append(user)
                    return 'Usuário adicionado'

                return 'Usuário não adicionado'

        if name == user.name:
            return 'Nome adicionado já existe'

    def list(self) -> Union[str, list]:
        """
        List all the users in the database
        :return: 'Não há pessoas cadastradas' if there aren`t no user in the database or all the users
        """
        if len(self.store.database) <= 0:
            return 'Não há pessoas cadastradas'

        return self.store.database

    def delete_user(self, name):
        """
        Delete a user from the database by given a name
        :param name:  The username to be deleted from the database
        :return: 'Usuário removido com sucesso' if the user exists in the database or 'Usuário não encontrado' if the user is not in the database
        """
        user = self.check_user_exists(name)

        if type(user) == str:
            return user
        else:
            self.store.database.remove(user)
            return 'Usuário removido com sucesso'

    def update_user(self, name, job):
        """
        Update the user job title by the username
        :param name: User name
        :param job: Job title to by updated
        :return: 'Trabalho atualizado com sucesso' if the job title was updated successfully, 'Usuário não encontrado' if the user is not in the database
        """
        user = self.check_user_exists(name)

        if type(user) == str:
            return user

        else:
            index = self.store.database.index(user)
            user.job = job
            self.store.database[index] = user

            return 'Trabalho atualizado com sucesso'

    def get_user(self, name):
        """
        :param name: User name to query
        :return: Job title, or 'Usuário não encontrado' if not in the database
        """
        user = self.check_user_exists(name)

        if type(user) == str:
            return user

        if user.name == name:
            return user.job

    def check_user_exists(self, name: str) -> Union[User, str]:
        """
        Username to query
        :param name: Username
        :return: User if in the database or 'Usuário não encontrado' if the user is not in the database
        """
        for user in self.store.database:
            if user.name == name:
                return user

        return 'Usuário não encontrado'
