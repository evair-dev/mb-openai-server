from flask import Flask, request
from flask_cors import CORS

from src.chat.infrastructure.controller import bp_chat
from src.train.infrastructure.controller import bp_train


def create_app(config_class):
    app_base = Flask(__name__)
    app_base.config.from_object(config_class)

    CORS(app_base, resources={r'*': {'origins': '*'}})

    # modules
    app_base.register_blueprint(bp_chat,  url_prefix='/v1')
    app_base.register_blueprint(bp_train,  url_prefix='/v1')

    @app_base.before_request
    def log_request_info():
        app_base.logger.info(f'\n\nRequest: {request.method}, {request.scheme}, {request.full_path}')
        app_base.logger.info(f'\nData: {request.data}\n')

    @app_base.route('/', methods=["GET"])
    def health_check():
        return {'message': 'Application is healthy'}

    return app_base



