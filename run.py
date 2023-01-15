import os
from dotenv import load_dotenv
load_dotenv()
from src.app import app

app_mode = os.getenv('MODE')


if __name__ == '__main__':
    if(app_mode == "dev"):
        app.run(debug=True)
    else:
        from waitress import serve
        serve(app, host="0.0.0.0", port=8080)