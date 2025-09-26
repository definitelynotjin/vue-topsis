from flask import Blueprint, request, jsonify
from db import db
from models import Criteria

criteria_bp = Blueprint("criteria", __name__)

# GET criteria by project_id
@criteria_bp.route("/<int:project_id>", methods=["GET"])
def get_criteria(project_id):
    criteria_list = Criteria.query.filter_by(project_id=project_id).all()
    result = []
    for c in criteria_list:
        result.append({
            "id": c.id,
            "name": c.name,
            "weight": c.weight,
            "type": c.type,
            "project_id": c.project_id
        })
    return jsonify(result)

#GET all criteria
# @criteria_bp.route("/", methods=["GET"])
# def get_all_criteria():
#     criteria_list = Criteria.query.all()
#     result = [
#         {
#             "id": c.id,
#             "name": c.name,
#             "weight": c.weight,
#             "type": c.type,
#             "project_id": c.project_id
#         }
#         for c in criteria_list
#     ]
#     return jsonify(result)

# POST add new criteria
@criteria_bp.route("/", methods=["POST"])
def add_criteria():
    data = request.json
    project_id = data.get("project_id")
    name = data.get("name")
    weight = data.get("weight")
    type_ = data.get("type")  # benefit / cost

    if not project_id or not name or weight is None or type_ not in ["benefit", "cost"]:
        return jsonify({"error": "Criteria is Invalid"}), 400

    new_criteria = Criteria(
        project_id=project_id,
        name=name,
        weight=weight,
        type=type_
    )
    db.session.add(new_criteria)
    db.session.commit()

    return jsonify({ 
        "id": new_criteria.id,
        "name": new_criteria.name,
        "weight": new_criteria.weight,
        "type": new_criteria.type,
        "project_id": new_criteria.project_id
    }), 201

