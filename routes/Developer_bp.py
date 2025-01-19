from flask import Blueprint
from controllers.DeveloperController import get_developers, get_developer, add_developer, update_developer, delete_developer, patch_developer

developer_bp = Blueprint('developer_bp', __name__)

developer_bp.route('/api/developers', methods=['GET'])(get_developers)
developer_bp.route('/api/developers/<int:developer_id>', methods=['GET'])(get_developer)
developer_bp.route('/api/developers', methods=['POST'])(add_developer)
developer_bp.route('/api/developers/<int:developer_id>', methods=['PUT'])(update_developer)
developer_bp.route('/api/developers/<int:developer_id>', methods=['PATCH'])(patch_developer)
developer_bp.route('/api/developers/<int:developer_id>', methods=['DELETE'])(delete_developer)
