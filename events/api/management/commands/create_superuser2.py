from django.contrib.auth.management.commands import createsuperuser
from django.core.management import CommandError


class Command(createsuperuser.Command):
    help = 'Crate a superuser, and allow password to be provided'

    def add_arguments(self, parser):
        super(Command, self).add_arguments(parser)
        parser.add_argument(
            '--preserve', dest='preserve', default=False, action='store_true',
            help='Exit normally if the user already exists.',
        )

    def handle(self, *args, **options):
        password = options.get('password')
        email = options.get('email')
        organization = options.get('organization')
        database = options.get('database')

        if password and not email:
            raise CommandError("--email is required if specifying --password")

        if email and options.get('preserve'):
            exists = self.UserModel._default_manager.db_manager(database).filter(email=email).exists()
            if exists:
                self.stdout.write("User exists, exiting normally due to --preserve")
                return

        super(Command, self).handle(*args, **options)

        if password and organization:
            user = self.UserModel._default_manager.db_manager(database).get(email=email)
            user.set_password(password)
            user.save()

