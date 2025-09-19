import numpy as np

def calculate_topsis(alternatives, criteria_order):
    """
    Menghitung ranking TOPSIS dari daftar alternatif.

    Parameters:
        alternatives: list of dict
            [
                {
                    "id": 1,
                    "name": "Pegawai 1",
                    "nip": "NOC01",
                    "scores": [
                        {"criteria": "Kehadiran", "value": 74},
                        {"criteria": "Kecepatan", "value": 70},
                        {"criteria": "Sakit", "value": 73},
                    ]
                },
                ...
            ]

        criteria_order: list of dict
            [
                {"criteria": "Kehadiran", "weight": 0.4, "type": "benefit"},
                {"criteria": "Kecepatan", "weight": 0.5, "type": "benefit"},
                {"criteria": "Sakit", "weight": 0.1, "type": "cost"}
            ]

    Returns:
        result: list of dict
            [
                {"id": 1, "name": "Pegawai 1", "nip": "NOC01", "score": 0.82},
                ...
            ]
    """

    if not alternatives or not criteria_order:
        return []

    # Ambil bobot, tipe, dan nama kriteria dari criteria_order
    weights = np.array([c["weight"] for c in criteria_order])
    types = [c["type"] for c in criteria_order]
    criteria_names = [c["criteria"] for c in criteria_order]

    # Susun matriks keputusan sesuai urutan criteria_order
    matrix = []
    for alt in alternatives:
        values = []
        for cname in criteria_names:
            val = next((s["value"] for s in alt["scores"] if s["criteria"] == cname), None)
            if val is None:
                raise ValueError(f"Nilai untuk kriteria '{cname}' tidak ditemukan di {alt['name']}")
            values.append(val)
        matrix.append(values)

    matrix = np.array(matrix, dtype=float)

    # Normalisasi matriks
    norm_matrix = matrix / np.sqrt((matrix**2).sum(axis=0))

    # Matriks berbobot
    weighted_matrix = norm_matrix * weights

    # Tentukan solusi ideal positif & negatif
    ideal_pos = np.array([
        max(weighted_matrix[:, i]) if t == "benefit" else min(weighted_matrix[:, i])
        for i, t in enumerate(types)
    ])
    ideal_neg = np.array([
        min(weighted_matrix[:, i]) if t == "benefit" else max(weighted_matrix[:, i])
        for i, t in enumerate(types)
    ])

    # Hitung jarak ke solusi ideal
    s_pos = np.sqrt(((weighted_matrix - ideal_pos) ** 2).sum(axis=1))
    s_neg = np.sqrt(((weighted_matrix - ideal_neg) ** 2).sum(axis=1))

    # Hitung skor preferensi TOPSIS
    scores = s_neg / (s_pos + s_neg)

    # Buat hasil akhir
    result = []
    for i, alt in enumerate(alternatives):
        result.append({
            "id": alt["id"],
            "name": alt["name"],
            "nip": alt.get("nip"),
            "score": float(scores[i])
        })

    # Urutkan berdasarkan skor (descending)
    result.sort(key=lambda x: x["score"], reverse=True)

    return result
