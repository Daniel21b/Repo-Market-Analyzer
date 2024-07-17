from app import app
from app.routes import initialize_routes

initialize_routes(app)

if __name__ == '__main__':
    app.run(debug=True)