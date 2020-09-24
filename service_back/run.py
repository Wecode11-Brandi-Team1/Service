from flask_script import Manager

from app          import create_app


app = create_app()
manager = Manager(app)

@manager.command
def run():
    app.run(
        host='10.251.1.174', 
        port=5000,
        debug=True)

if __name__ == '__main__':
    manager.run()