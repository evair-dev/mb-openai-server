from flask import Blueprint

bp_chat = Blueprint('chat', __name__)


@bp_chat.route('/chat', methods=["POST"])
def get_vegetation():
    return {'message': 'Application is chatting'}