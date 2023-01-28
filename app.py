import os
import sys
from dotenv import load_dotenv

load_dotenv(os.path.join(os.path.dirname(__file__), ".env"))

from flask import Flask
from application.database import session

def init_webhooks(base_url):
    # Update inbound traffic via APIs to use the public-facing ngrok URL
    pass

def create_app():
    app = Flask(__name__)
    # Initialize our ngrok settings into Flask
    app.config.from_mapping(
        BASE_URL="http://localhost:5000",
        USE_NGROK=os.environ.get("USE_NGROK", "False") == "True" and os.environ.get("WERKZEUG_RUN_MAIN") != "true"
    )

    if app.config.get("ENV") == "development" and app.config["USE_NGROK"]:
        # pyngrok will only be installed, and should only ever be initialized, in a dev environment
        from pyngrok import ngrok

        # Get the dev server port (defaults to 5000 for Flask, can be overridden with `--port`
        # when starting the server
        port = sys.argv[sys.argv.index("--port") + 1] if "--port" in sys.argv else 5000

        # Open a ngrok tunnel to the dev server
        public_url = ngrok.connect(port).public_url
        print(" * ngrok tunnel \"{}\" -> \"http://127.0.0.1:{}\"".format(public_url, port))

        # Update any base URLs or webhooks to use the public ngrok URL
        app.config["BASE_URL"] = public_url
        init_webhooks(public_url)

    # Initialize SQLAlchemy
    app.session = session

    # ... Initialize Blueprints and the rest of our app

    from application.views import Users
    # AttributeError: 'function' object has no attribute 'register'
    app.register_blueprint(Users, url_prefix="/users")

    return app




if __name__ == "__main__":
    app = create_app()
    app.run(debug=True)