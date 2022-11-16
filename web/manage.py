from flask.cli import FlaskGroup
from web.app.server import app

cli = FlaskGroup(app)

if __name__ == "__main__":
    cli()