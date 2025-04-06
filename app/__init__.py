import json
import os
from flask import Flask

def create_app():
    app = Flask(__name__)

    # Kontrola existence souboru config.json
    config_file_path = "./config.json"
    if not os.path.exists(config_file_path):
        raise FileNotFoundError(f"Konfigurační soubor {config_file_path} nebyl nalezen.")

    try:
        with open(config_file_path, "r") as config_file:
            config_data = json.load(config_file)

            if "secret_key" not in config_data:
                raise KeyError("'secret_key' není definován v konfiguračním souboru.")

            secret_key = config_data["secret_key"]

            # Kontrola, zda je secret_key typu str
            if not isinstance(secret_key, str):
                raise TypeError(f"'secret_key' musí být typu str, zadaná hodnota: {type(secret_key).__name__}")

            app.secret_key = secret_key

    except json.JSONDecodeError:
        raise ValueError(f"Konfigurační soubor {config_file_path} není ve správném formátu JSON.")
    except KeyError as e:
        raise KeyError(f"Chybí povinný klíč v konfiguračním souboru: {e}")
    except TypeError as e:
        raise TypeError(f"Chyba typu: {e}")
    except Exception as e:
        raise Exception(f"Nastala chyba při načítání konfiguračního souboru: {e}")

    from .controllers import main
    app.register_blueprint(main)

    return app
