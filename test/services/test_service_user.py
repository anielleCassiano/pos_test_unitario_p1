from src.services.service_user import ServiceUser


class TestServiceUser:

    def test_add_user_success(self):
        service = ServiceUser()

        nilson = service.add_user(name='Nilson', job='Tester')
        assert nilson == 'Usuário adicionado'

    def test_add_user_already_exists(self):
        service = ServiceUser()

        tester = service.add_user(name='Nilson', job='Tester')
        assert tester == 'Usuário adicionado'

        tester_1 = service.add_user(name='Nilson', job='Analista')
        assert tester_1 == 'Nome adicionado já existe'

    def test_add_user_differ_types(self):
        service = ServiceUser()

        tester = service.add_user(name=1, job=1)

        assert tester == 'Usuário não adicionado'

        tester = service.add_user(name='Name', job=1)

        assert tester == 'Usuário não adicionado'

        tester = service.add_user(name=1, job='Tester')

        assert tester == 'Usuário não adicionado'

    def test_add_user_eq_none(self):
        service = ServiceUser()

        result = service.add_user(name=None, job=None)

        assert result == 'Usuário não adicionado'

        result = service.add_user(name=None, job='Tester')

        assert result == 'Usuário não adicionado'

        result = service.add_user(name='Name', job=None)

        assert result == 'Usuário não adicionado'

    def test_delete_user_success(self):
        service = ServiceUser()

        service.add_user(name='Test', job='Tester')

        result = service.delete_user(name='Test')

        assert result == 'Usuário removido com sucesso'

    def test_delete_user_not_found(self):
        service = ServiceUser()

        result = service.delete_user(name='Test')

        assert result == 'Usuário não encontrado'

    def test_update_user_success(self):
        service = ServiceUser()

        service.add_user(name='Test', job='Tester')
        service.add_user(name='Test2', job='Tester2')

        result = service.update_user(name='Test', job='Analista')

        assert result == 'Job atualizado com sucesso'

        assert len(service.list()) == 2

    def test_get_user_success(self):
        service = ServiceUser()

        service.add_user(name='Test', job='Tester')

        result = service.get_user(job='Tester')

        assert result == 'Test'
