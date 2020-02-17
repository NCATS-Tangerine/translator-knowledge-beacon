import connexion

from swagger_server import encoder
from flask import redirect
from beacon_controller import config

def handle_error(e):
    return redirect(config['basepath'])

def main(name:str):
    """
    Usage in swagger_server/main.py:

        from beacon_controller import run
        if __name__ == '__main__':
            run(__name__)
    """
    app = connexion.App(name, specification_dir='./swagger/', server=config['server'])

    app.app.json_encoder = encoder.JSONEncoder
    app.app.json_encoder.include_nulls = config['include_nulls']

    app.add_api(
        'swagger.yaml',
        base_path=config['basepath'],
        swagger_url='/',
        arguments={'title': config['title']}
    )

    if config['redirect_404'] and isinstance(config['basepath'], str):
        app.add_error_handler(404, lambda e: redirect(config['basepath']))

    app.run(port=config['port'])
