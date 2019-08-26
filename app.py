from flask_graphql import GraphQLView
from flask import Flask
from models import db_session, Base, engine
from schema import schema

app = Flask(__name__)

# Db configs

#  Schema Objects

#  Routes

app.add_url_rule('/graphql', view_func=GraphQLView.as_view('graphql', schema=schema, graphiql=True, context={"session": db_session}))

@app.route('/')
def index():
    return "Go to /graphql"

@app.teardown_appcontext
def shutdown_session(exception=None):
    db_session.remove()

if __name__ == '__main__':
    Base.metadata.create_all(bind=engine)
    app.debug=True
    app.run("0.0.0.0", port=5000)
