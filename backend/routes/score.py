from flask import Blueprint, request, jsonify
from db import db
from models import Score, Criteria

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
