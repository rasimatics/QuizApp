from quizapp import create_app
from flask_migrate import MigrateCommand
from flask_script import Manager



# add manager(migrate command script)
manager = Manager(create_app())
manager.add_command('db',MigrateCommand)


if __name__ == '__main__':
    manager.run()
