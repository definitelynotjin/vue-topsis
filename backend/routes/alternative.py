from flask import Blueprint, request, jsonify
from db import db
from models import Alternative

alt_bp = Blueprint("alternatives", __name__)

# GET alternatives by project_id
@alt_bp.route("/<int:project_id>", methods=["GET"])
def get_alternatives(project_id):
    alternatives = Alternative.query.filter_by(project_id=project_id).all()
    result = []
    for alt in alternatives:
        result.append({
            "id": alt.id,
            "name": alt.name,
            "id_alt": getattr(alt, "id_alt", None),
            # "rank": getattr(alt, "rank", None),
            "project_id": alt.project_id
        })
    return jsonify(result)


# POST add new alternative
@alt_bp.route("/", methods=["POST"])
def add_alternative():
    data = request.json
    project_id = data.get("project_id")
    name = data.get("name")
    id_alt = data.get("id_alt", "")

    if not project_id or not name:
        return jsonify({"error": "Project and Alternative name cannot be empty"}), 400

    # buat instance Alternative
    new_alt = Alternative(project_id=project_id, name=name, id_alt=id_alt)
    db.session.add(new_alt)
    db.session.commit()

    return jsonify({"message": "Alternative added succesfully"}, 201)

# UPDATE alternative
@alt_bp.route("/<int:alt_id>", methods=["PUT"])
def update_alternative(alt_id):
    data = request.json or {}
    name = data.get("name")
    id_alt = data.get("id_alt")

    alt = Alternative.query.get(alt_id)
    if not alt:
        return jsonify({"error": "Alternative not found"}), 404

    # Update hanya kalau field dikirim dan tidak kosong
    if name is not None and name != "":
        alt.name = name
    if id_alt is not None and id_alt != "":
        alt.id_alt = id_alt
    db.session.commit()

    return jsonify({"message": "Alternative updated successfully"})

# DELETE alternative
@alt_bp.route("/<int:alt_id>", methods=["DELETE"])
def delete_alternative(alt_id):
    alt = Alternative.query.get(alt_id)
    if not alt:
        return jsonify({"error": "Alternative not found"}), 404

    db.session.delete(alt)
    db.session.commit()

    return jsonify({"message": "Alternative deleted successfully"})
