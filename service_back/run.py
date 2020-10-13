from flask_script import Manager

from app          import create_app

app     = create_app()
manager = Manager(app)

@manager.command
def run():
    app.run(
        host='192.168.7.5', 
        port=5000,
        debug=True)

if __name__ == '__main__':
    manager.run()