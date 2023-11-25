from flask import Blueprint

bp_train = Blueprint('train', __name__)


@bp_train.route('/train', methods=["POST"])
def get_vegetation():
    return {'message': 'Application is training'}

