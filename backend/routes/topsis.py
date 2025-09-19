from flask import Blueprint, jsonify, request
from db import db
from models import Alternative, Score, Criteria
from services.topsis import calculate_topsis

topsis_bp = Blueprint("topsis", __name__)

@topsis_bp.route("/<int:project_id>", methods=["GET", "POST"])
def topsis_ranking(project_id):
    save_to_db = request.args.get("save", "0") == "1"

    # Ambil semua alternatif dan skor untuk project
    alternatives = Alternative.query.filter_by(project_id=project_id).all()
    criteria = Criteria.query.filter_by(project_id=project_id).all()

    # Susun urutan kriteria sesuai DB
    criteria_order = [
        {
            "criteria": c.name,
            "weight": c.weight,
            "type": c.type
        }
        for c in criteria
    ]

    alt_list = []
    for alt in alternatives:
        scores_data = []
        for score in alt.scores:
            scores_data.append({
                "criteria": score.criteria.name,   # penting: dipakai di services/topsis.py
                "value": score.value
            })
        alt_list.append({
            "id": alt.id,
            "name": alt.name,
            "nip": getattr(alt, "nip", None),
            "scores": scores_data
        })

    # Hitung ranking TOPSIS
    ranking_result = calculate_topsis(alt_list, criteria_order)

    return jsonify(ranking_result)

    # # Simpan ke DB jika parameter save=1 (opsional)
    # if save_to_db and ranking_result:
    #     # Hapus ranking lama project (asumsi ada model Ranking)
    #     Ranking.query.filter_by(project_id=project_id).delete()
    #     for idx, alt in enumerate(ranking_result, start=1):
    #         new_rank = Ranking(
    #             project_id=project_id,
    #             alternative_id=alt["id"],
    #             score=alt["score"],
    #             rank=idx
    #         )
    #         db.session.add(new_rank)
    #     db.session.commit()

    return jsonify(ranking_result)
