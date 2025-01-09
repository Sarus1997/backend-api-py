from flask import Blueprint
from app.router.get_data import get_data
from app.router.post_data import add_data
from app.router.put_data import update_data
from app.router.delete_data import delete_data

api_blueprint = Blueprint("api", __name__)

#* Register individual route modules
api_blueprint.add_url_rule("/get_data", view_func=get_data, methods=["GET"])
api_blueprint.add_url_rule("/post_data", view_func=add_data, methods=["POST"])
api_blueprint.add_url_rule("/update_data", view_func=update_data, methods=["PUT"])
api_blueprint.add_url_rule("/delete_data", view_func=delete_data, methods=["DELETE"])
