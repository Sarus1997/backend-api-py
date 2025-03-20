import yaml
from flask import Blueprint
from app.router.product.get_data import get_data
from app.router.product.get_product import get_product
from app.router.product.post_data import add_data
from app.router.product.put_data import update_data
from app.router.product.delete_data import delete_data

from app.router.users.get_user import get_user


api_blueprint = Blueprint("api", __name__)

#* โหลดการกำหนดค่าจาก config.yaml ด้วยการเข้ารหัสที่ระบุ
with open("config.yaml", "r", encoding="utf-8") as config_file:
    config = yaml.safe_load(config_file)

#* Register individual route modules
#* GET
if config["api_status"]["product"]:
    api_blueprint.add_url_rule("/get_data", view_func=get_data, methods=["GET"])
    api_blueprint.add_url_rule("/get_product", view_func=get_product, methods=["GET"])

#* POST
if config["api_status"]["product"]:
    api_blueprint.add_url_rule("/post_data", view_func=add_data, methods=["POST"])

#* PUT
if config["api_status"]["product"]:
    api_blueprint.add_url_rule("/update_data", view_func=update_data, methods=["PUT"])

#* DELETE
if config["api_status"]["product"]:
    api_blueprint.add_url_rule("/delete_data", view_func=delete_data, methods=["DELETE"])

#* USER
if config["api_status"]["users"]:
    api_blueprint.add_url_rule("/get_user", view_func=get_user, methods=["GET"])
