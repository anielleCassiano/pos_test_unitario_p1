import pytest

from src.services.service_user import ServiceUser
from src.models.user import User


class TestServiceUser:

    @pytest.fixture
    def service(self):
        return ServiceUser()

    def test_add_user_name_none_and_job_none(self, service):
        tester = service.add_user(name=None, job=None)

        assert tester == 'Usuário não adicionado'

    def test_add_user_name_none_and_job_str(self, service):
        result = service.add_user(name=None, job='Tester')

        assert result == 'Usuário não adicionado'

    def test_add_user_name_str_and_job_none(self, service):
        result = service.add_user(name='John Doe', job=None)

        assert result == 'Usuário não adicionado'

    def test_add_user_already_exists(self, service):
        service.add_user(name='John Doe', job='Tester')

        result = service.add_user(name='John Doe', job='Analista')

        assert result == 'Nome adicionado já existe'

    def test_add_user_type_name_str_and_type_job_int(self, service):
        result = service.add_user(name='John Doe', job=0)

        assert result == 'Usuário não adicionado'

    def test_add_user_type_name_int_and_type_job_str(self, service):
        result = service.add_user(name=0, job='Tester')

        assert result == 'Usuário não adicionado'

    def test_add_user_type_name_int_and_type_job_int(self, service):
        result = service.add_user(name=0, job=0)

        assert result == 'Usuário não adicionado'

    def test_add_user(self, service):
        result = service.add_user(name='John Doe', job='Tester')

        assert result == 'Usuário adicionado'

    def test_list_with_not_users(self, service):
        result = service.list()

        assert result == 'Não há pessoas cadastradas'

    def test_list(self, service):
        service.add_user('John Doe', 'Tester')
        result = len(service.list())

        assert result == 1

    def test_delete_user(self, service):
        service.add_user(name='John Doe', job='Tester')

        result = service.delete_user(name='John Doe')

        assert result == 'Usuário removido com sucesso'

    def test_delete_user_not_found(self, service):
        result = service.delete_user(name='John Doe')

        assert result == 'Usuário não encontrado'

    def test_update_user(self, service):
        service.add_user(name='John Doe', job='Tester')

        result = service.update_user(name='John Doe', job='Analista')

        assert result == 'Trabalho atualizado com sucesso'

    def test_update_user_not_found(self, service):
        result = service.update_user(name='John Doe', job='Analista')

        assert result == 'Usuário não encontrado'

    def test_get_user(self, service):
        service.add_user(name='John Doe', job='Tester')

        result = service.get_user(name='John Doe')

        assert result == 'Tester'

    def test_get_user_not_found(self, service):
        result = service.get_user(name='John Doe')

        assert result == 'Usuário não encontrado'

    def test_check_user_exists(self, service):
        service.add_user(name='John Doe', job='Tester')

        result = service.check_user_exists('John Doe')

        assert result.__str__() == 'name: John Doe, job: Tester'

    def test_check_user_exists_if_not_found(self, service):
        result = service.check_user_exists('John Doe')

        assert result == 'Usuário não encontrado'
