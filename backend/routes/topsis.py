from flask import Blueprint, jsonify, request
from db import db
from models import Alternative, Score, Criteria, TopsisResult
from services.topsis import calculate_weighted_matrix, topsis_full_process

topsis_bp = Blueprint("topsis", __name__)

def get_topsis_data(project_id):
    """Helper untuk ambil alternatif + kriteria lalu hitung TOPSIS"""
    alternatives = Alternative.query.filter_by(project_id=project_id).all()
    criteria = Criteria.query.filter_by(project_id=project_id).all()

    # urutan kriteria sesuai DB
    criteria_order = [
        {"criteria": c.name, "weight": c.weight, "type": c.type}
        for c in criteria
    ]

    alt_list = []
    for alt in alternatives:
        scores_data = []
        for score in alt.scores:
            scores_data.append({
                "criteria": score.criteria.name,
                "value": score.value
            })
        alt_list.append({
            "id": alt.id,
            "name": alt.name,
            "id_alt": getattr(alt, "id_alt", None),
            "scores": scores_data
        })

    ranking_result = topsis_full_process(alt_list, criteria_order)
    # ranking_result = sorted(ranking_result, key=lambda x: x["score"], reverse=True)
    # skipped = sorted(skipped, key=lambda x: x["name"], reverse=True)
    return ranking_result

def get_matriks_weighted(project_id):
    """Helper untuk ambil alternatif + kriteria lalu hitung matriks berbobot"""
    alternatives = Alternative.query.filter_by(project_id=project_id).all()
    criteria = Criteria.query.filter_by(project_id=project_id).all()

    # urutan kriteria sesuai DB
    criteria_order = [
        {"criteria": c.name, "weight": c.weight, "type": c.type}
        for c in criteria
    ]

    alt_list = []
    for alt in alternatives:
        scores_data = []
        for score in alt.scores:
            scores_data.append({
                "criteria": score.criteria.name,
                "value": score.value
            })
        alt_list.append({
            "id": alt.id,
            "name": alt.name,
            "id_alt": getattr(alt, "id_alt", None),
            "scores": scores_data
        })

    matrix_result, skipped = calculate_weighted_matrix(alt_list, criteria_order)
    
    return matrix_result, skipped


@topsis_bp.route("/<int:project_id>", methods=["GET"])
def topsis_ranking(project_id):
    """Hitung TOPSIS tanpa simpan ke DB"""
    result= get_topsis_data(project_id)

    ranking_result = result.get("ranking", [])
    skipped = result.get("skipped", [])

    return jsonify({
        "status": "success",
        "message": f"TOPSIS calculation completed",
        "total": len(ranking_result),
        "skipped": len(skipped),
        "data": ranking_result
    })


@topsis_bp.route("/<int:project_id>/save", methods=["POST"])
def save_topsis_ranking(project_id):
    """Hitung TOPSIS lalu simpan ke DB"""
    result = get_topsis_data(project_id)

    ranking_result = result.get("ranking", [])
    skipped = result.get("skipped", [])

    # hapus hasil lama
    TopsisResult.query.filter_by(project_id=project_id).delete()

    # simpan hasil baru
    for idx, r in enumerate(ranking_result, start=1):
        new_result = TopsisResult(
            project_id=project_id,
            alternative_id=r["id"],
            score=r["score"],
            rank=idx
        )
        db.session.add(new_result)

    db.session.commit()

    return jsonify({
        "status": "success",
        "message": "Ranking saved successfully",
        "total": len(ranking_result),
        "skipped": len(skipped),
    })

@topsis_bp.route("/<int:project_id>/results", methods=["GET"])
def get_saved_ranking(project_id):
    """Ambil hasil ranking yang sudah disimpan"""
    results = TopsisResult.query.filter_by(project_id=project_id).order_by(TopsisResult.rank).all()
    output = []
    for r in results:
        alt = Alternative.query.get(r.alternative_id)
        output.append({
            "id": r.id,
            "alternative_id": r.alternative_id,
            "alternative_name": alt.name if alt else "",
            "id_alt": getattr(alt, "id_alt", None) if alt else None,
            "score": r.score,
            "rank": r.rank
        })

    return jsonify({
        "status": "success",
        "message": f"Retrieved {len(output)} ranking results",
        "data": output
    })

# DATA Matriks Weighted
@topsis_bp.route("/<int:project_id>/matrix-weight", methods=["GET"])
def get_decision_matrix(project_id):
    """Hitung matriks keputusan berbobot tanpa simpan ke DB"""
    result = get_topsis_data(project_id)

    matrix_weigted = result.get("matrix_weighted", [])
    skipped = result.get("skipped", [])


    return jsonify({
        "status": "success",
        "message": f"Weighted decision matrix calculation completed",
        "total": len(matrix_weigted),
        "skipped": len(skipped),
        "data": matrix_weigted
    })

#DATA Solusi Ideal
@topsis_bp.route("/<int:project_id>/ideal-solution", methods=["GET"])
def get_ideal_solution(project_id):
    """Hitung solusi ideal tanpa simpan ke DB"""
    result = get_topsis_data(project_id)

    ideal_solution = result.get("ideal_solution", [])
    skipped = result.get("skipped", [])


    return jsonify({
        "status": "success",
        "message": f"Ideal solution calculation completed",
        "total": len(ideal_solution),
        "skipped": len(skipped),
        "data": ideal_solution
    })

#DATA Matriks Normalized
@topsis_bp.route("/<int:project_id>/matrix-normalized", methods=["GET"])
def get_decision_matrix_normalized(project_id):
    """Hitung matriks keputusan ternormalisasi tanpa simpan ke DB"""
    result = get_topsis_data(project_id)

    matrix_normalized = result.get("matrix_normalized", [])
    skipped = result.get("skipped", [])


    return jsonify({
        "status": "success",
        "message": f"Normalized decision matrix calculation completed",
        "total": len(matrix_normalized),
        "skipped": len(skipped),
        "data": matrix_normalized
    })


# DATA Matriks Before Weight
@topsis_bp.route("/<int:project_id>/matrix-raw", methods=["GET"])
def get_decision_matrix_before_weight(project_id):
    """Hitung matriks keputusan sebelum berbobot tanpa simpan ke DB"""
    alternatives = Alternative.query.filter_by(project_id=project_id).all()
    criteria = Criteria.query.filter_by(project_id=project_id).all()

    # urutan kriteria sesuai DB
    criteria_order = [
        {"criteria": c.name, "weight": c.weight, "type": c.type}
        for c in criteria
    ]

    alt_list = []
    for alt in alternatives:
        scores_data = []
        for score in alt.scores:
            scores_data.append({
                "criteria": score.criteria.name,
                "value": score.value
            })
        alt_list.append({
            "id": alt.id,
            "name": alt.name,
            "id_alt": getattr(alt, "id_alt", None),
            "scores": scores_data
        })

    matrix_result = []
    skipped = []
    if not criteria_order:
        return jsonify({
            "status": "error",
            "message": "No criteria found for this project",
            "total": 0,
            "skipped": 0,
            "data": []
        }), 400

    # Buat matriks keputusan sebelum berbobot
    decision_matrix = []
    for alt in alt_list:
        row = { "nama": alt["name"], "id": alt["id_alt"]}
        scores_dict = {s["criteria"]: s["value"] for s in alt["scores"]}
        missing_criteria = False
        for c in criteria_order:
            if c["criteria"] in scores_dict:
                row[c["criteria"]] = scores_dict[c["criteria"]]
            else:
                row[c["criteria"]] = None
                missing_criteria = True
        if missing_criteria:
            skipped.append(alt)
        else:
            decision_matrix.append(row)

    return jsonify({
        "status": "success",
        "message": f"Decision matrix before weighting calculation completed",
        "total": len(decision_matrix),
        "skipped": len(skipped),
        "data": decision_matrix
    })

