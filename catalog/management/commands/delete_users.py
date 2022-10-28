from django.contrib.auth.models import User
from django.core.management.base import BaseCommand


class Command(BaseCommand):
    help = 'Delete users'

    def add_arguments(self, parser):
        parser.add_argument('user_id', nargs='+', type=int, help='User ID')

    def handle(self, *args, **kwargs):
        users_ids = kwargs['user_id']

        for user_id in users_ids:
            try:
                user = User.objects.get(pk=user_id, is_superuser=False)
                user.delete()
                self.stdout.write(u'Пользователь"%s (%s)" удален успешно!' % (user.username, user_id))
            except User.DoesNotExist:
                self.stdout.write(u'Пользователь с id "%s" не существует.' % user_id)
