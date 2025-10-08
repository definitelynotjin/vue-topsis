import numpy as np


# ============================================================
# 1️⃣ Matriks Keputusan (Decision Matrix)
# ============================================================
def build_decision_matrix(alternatives, criteria_order):
    """
    Menghasilkan matriks keputusan awal (nilai mentah) berdasarkan alternatif dan urutan kriteria.
    """
    clean_alternatives = []
    skipped = []

    for alt in alternatives:
        criteria_map = {s["criteria"]: s["value"] for s in alt["scores"]}
        row = []
        missing = False
        for c in criteria_order:
            if c["criteria"] in criteria_map:
                row.append(criteria_map[c["criteria"]])
            else:
                missing = True
                break
        if missing:
            skipped.append({
                "id": alt["id"],
                "name": alt["name"],
                "id_alt": alt.get("id_alt"),
                "reason": "Missing criteria scores"
            })
            continue
        clean_alternatives.append({
            "id": alt["id"],
            "name": alt["name"],
            "id_alt": alt.get("id_alt"),
            "row": row
        })

    matrix = np.array([alt["row"] for alt in clean_alternatives], dtype=float)
    return matrix, clean_alternatives, skipped


# ============================================================
# 2️⃣ Normalisasi Matriks
# ============================================================
def calculate_normalized_matrix(matrix):
    """
    Normalisasi matriks keputusan.
    """
    if matrix.size == 0:
        return np.array([])
    norm_matrix = matrix / np.sqrt((matrix**2).sum(axis=0))
    return norm_matrix


# ============================================================
# 3️⃣ Matriks Berbobot
# ============================================================
def calculate_weighted_matrix(norm_matrix, criteria_order):
    """
    Menghasilkan matriks berbobot dari matriks ternormalisasi.
    """
    weights = np.array([c["weight"] for c in criteria_order], dtype=float)
    weighted_matrix = norm_matrix * weights
    return weighted_matrix


# ============================================================
# 4️⃣ Perhitungan TOPSIS (jarak, skor, ranking)
# ============================================================
def calculate_topsis_result(weighted_matrix, clean_alternatives, criteria_order):
    """
    Hitung jarak ke solusi ideal, skor, dan ranking akhir.
    """
    types = [c["type"] for c in criteria_order]

    # Ideal positif dan negatif
    ideal_pos = np.array([
        max(weighted_matrix[:, i]) if t == "benefit" else min(weighted_matrix[:, i])
        for i, t in enumerate(types)
    ])
    ideal_neg = np.array([
        min(weighted_matrix[:, i]) if t == "benefit" else max(weighted_matrix[:, i])
        for i, t in enumerate(types)
    ])

    # Jarak ke ideal positif & negatif
    s_pos = np.sqrt(((weighted_matrix - ideal_pos) ** 2).sum(axis=1))
    s_neg = np.sqrt(((weighted_matrix - ideal_neg) ** 2).sum(axis=1))

    # Skor preferensi
    scores = s_neg / (s_pos + s_neg)

    # Susun hasil akhir
    results = []
    for i, alt in enumerate(clean_alternatives):
        results.append({
            "id": alt["id"],
            "name": alt["name"],
            "id_alt": alt["id_alt"],
            "score": float(scores[i]),
        })

    # Urutkan dan beri ranking
    sorted_results = sorted(results, key=lambda x: x["score"], reverse=True)
    for rank, item in enumerate(sorted_results, start=1):
        item["rank"] = rank

    return sorted_results, {
        "ideal_positive": ideal_pos.tolist(),
        "ideal_negative": ideal_neg.tolist(),
        "distance_pos": s_pos.tolist(),
        "distance_neg": s_neg.tolist()
    }


# ============================================================
# 🧩 Fungsi Utama (gabungkan semua langkah)
# ============================================================
def topsis_full_process(alternatives, criteria_order):
    """
    Menjalankan semua langkah TOPSIS dan mengembalikan hasil tiap tahap.
    """
    matrix, clean_alternatives, skipped = build_decision_matrix(alternatives, criteria_order)
    norm_matrix = calculate_normalized_matrix(matrix)
    weighted_matrix = calculate_weighted_matrix(norm_matrix, criteria_order)
    ranking, details = calculate_topsis_result(weighted_matrix, clean_alternatives, criteria_order)

    # Format hasil per tahap agar mudah dikirim ke frontend
    result = {
        "matrix_raw": [
            {"nama": alt["name"], **{c["criteria"]: v for c, v in zip(criteria_order, alt["row"])}}
            for alt in clean_alternatives
        ],
        "matrix_normalized": [
            {"nama": alt["name"], **{c["criteria"]: float(norm_matrix[i][j]) for j, c in enumerate(criteria_order)}}
            for i, alt in enumerate(clean_alternatives)
        ],
        "matrix_weighted": [
            {"nama": alt["name"], **{c["criteria"]: float(weighted_matrix[i][j]) for j, c in enumerate(criteria_order)}}
            for i, alt in enumerate(clean_alternatives)
        ],
        # Ideal solution hanya berisi nilai ideal positif & negatif per kriteria
        "ideal_solution": [
            {
                "criteria": c["criteria"],
                "ideal_positive": float(details["ideal_positive"][i]),
                "ideal_negative": float(details["ideal_negative"][i])
            }
            for i, c in enumerate(criteria_order)
        ],
        # Tambahkan jarak per alternatif di sini
        "distance": [
            {
                "nama": alt["name"],
                "distance_pos": float(details["distance_pos"][i]),
                "distance_neg": float(details["distance_neg"][i])
            }
            for i, alt in enumerate(clean_alternatives)
        ],
        "ranking": ranking,
        "skipped": skipped,
        "total": len(clean_alternatives)
    }

    return result
