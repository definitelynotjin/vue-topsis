from flask import Blueprint, request, jsonify
from db import db
from models import Score, Alternative

score_bp = Blueprint("score", __name__)

# GET scores by alternative_id
@score_bp.route("/<int:alt_id>", methods=["GET"])
def get_scores(alt_id):
    scores = Score.query.filter_by(alternative_id=alt_id).all()
    result = []
    for s in scores:
        result.append({
            "id": s.id,
            "criteria": s.criteria.name,  # pakai relationship
            "value": s.value
        })
    return jsonify(result)

# GET scores by project_id + criteria_id
@score_bp.route("/project/<int:project_id>/criteria/<int:criteria_id>", methods=["GET"])
def get_scores_by_criteria(project_id, criteria_id):
    scores = (
        db.session.query(Alternative, Score.value)
        .outerjoin(Score, (Score.alternative_id == Alternative.id) & (Score.criteria_id == criteria_id))  
        .filter(Alternative.project_id == project_id)
        .all()
    )

    result = []
    for alt, value in scores:
        result.append({
            "alt_id": alt.id,
            "name": alt.name,
            "value": value if value is not None else None  # show None if not yet scored
        })

    return jsonify(result)

# POST add new score
@score_bp.route("/", methods=["POST"])
def add_score():
    data = request.json
    alternative_id = data.get("alternative_id")
    criteria_id = data.get("criteria_id")
    value = data.get("value")

    if not alternative_id or not criteria_id or value is None:
        return jsonify({"error": "Score is Invalid"}), 400

    new_score = Score(
        alternative_id=alternative_id,
        criteria_id=criteria_id,
        value=value
    )
    db.session.add(new_score)
    db.session.commit()

    return jsonify({"message": "Score added sucessfully"}, 201)

# UPDATE a score
@score_bp.route("/<int:score_id>", methods=["PUT", "PATCH"])
def edit_score(score_id):
    data = request.json
    value = data.get("value")

    if value is None:
        return jsonify({"error": "Value is required"}), 400

    score = Score.query.get(score_id)
    if not score:
        return jsonify({"error": "Score not found"}), 404

    score.value = value
    db.session.commit()

    return jsonify({"message": "Score updated successfully"})
