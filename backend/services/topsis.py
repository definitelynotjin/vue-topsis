import numpy as np

def calculate_topsis(alternatives, criteria_order):
    if not alternatives:
        return []

    results = []
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
                # jika tidak ada, tandai missing
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

    if not clean_alternatives:
        return [], skipped  # semua data kosong

    # lanjutkan hitung dengan clean_alternatives
    matrix = np.array([alt["row"] for alt in clean_alternatives], dtype=float)
    weights = np.array([c["weight"] for c in criteria_order], dtype=float)
    types = [c["type"] for c in criteria_order]

    # normalisasi
    norm_matrix = matrix / np.sqrt((matrix**2).sum(axis=0))

    # bobot
    weighted_matrix = norm_matrix * weights

    # ideal pos & neg
    ideal_pos = np.array([
        max(weighted_matrix[:, i]) if t == "benefit" else min(weighted_matrix[:, i])
        for i, t in enumerate(types)
    ])
    ideal_neg = np.array([
        min(weighted_matrix[:, i]) if t == "benefit" else max(weighted_matrix[:, i])
        for i, t in enumerate(types)
    ])

    # jarak ke ideal
    s_pos = np.sqrt(((weighted_matrix - ideal_pos) ** 2).sum(axis=1))
    s_neg = np.sqrt(((weighted_matrix - ideal_neg) ** 2).sum(axis=1))

    scores = s_neg / (s_pos + s_neg)

    for i, alt in enumerate(clean_alternatives):
        results.append({
            "id": alt["id"],
            "name": alt["name"],
            "id_alt": alt["id_alt"],
            "score": float(scores[i]),
    })
    
    # Urutkan berdasarkan skor (descending)
    sorted_results = sorted(results, key=lambda x: x["score"], reverse=True)

    # Tambahkan ranking
    for rank, item in enumerate(sorted_results, start=1):
        item["rank"] = rank

    return results, skipped


def calculate_weighted_matrix(alternatives, criteria_order):
    """
    Menghasilkan matriks berbobot untuk alternatif yang lengkap saja.
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

    if not clean_alternatives:
        return [], skipped

    # Buat matrix
    matrix = np.array([alt["row"] for alt in clean_alternatives], dtype=float)
    weights = np.array([c["weight"] for c in criteria_order], dtype=float)

    # Normalisasi
    norm_matrix = matrix / np.sqrt((matrix**2).sum(axis=0))

    # Matriks berbobot
    weighted_matrix = norm_matrix * weights

    # Kembalikan dengan identitas alternatif
    results = []
    for i, alt in enumerate(clean_alternatives):
        # buat dictionary criteria → nilai
        weighted_scores = {
            c["criteria"]: float(weighted_matrix[i][j])
            for j, c in enumerate(criteria_order)
        }

        results.append({
            "id": alt["id"],
            "name": alt["name"],
            "id_alt": alt["id_alt"],
            "weighted_scores": weighted_scores
        })


    return results, skipped

