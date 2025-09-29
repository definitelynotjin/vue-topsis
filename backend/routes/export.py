from flask import Blueprint, send_file
from db import db
from models import Alternative, Criteria
import openpyxl
from io import BytesIO

export_bp = Blueprint("export", __name__)

@export_bp.route("/export/<int:project_id>", methods=["GET"])
def export_alternatives(project_id):
    # Ambil kriteria untuk menentukan header kolom
    criteria_list = Criteria.query.filter_by(project_id=project_id).all()
    criteria_names = [c.name for c in criteria_list]

    # Ambil alternatif + skor
    alternatives = Alternative.query.filter_by(project_id=project_id).all()

    # Buat workbook Excel
    wb = openpyxl.Workbook()
    ws = wb.active
    ws.title = "Alternatives"

    # Header
    headers = ["Nama"] + ["ID"] + ["Nama Project"] + criteria_names
    ws.append(headers)

    # Isi data
    for alt in alternatives:
        row = [alt.name]
        row.append(getattr(alt, "id_alt", ""))  # Menambahkan ID
        row.append(alt.project.name)

        # urutkan skor sesuai criteria_names
        scores_by_criteria = {s.criteria.name: s.value for s in alt.scores}
        for cname in criteria_names:
            row.append(scores_by_criteria.get(cname, ""))

        ws.append(row)

    # Simpan ke buffer
    output = BytesIO()
    wb.save(output)
    output.seek(0)

    return send_file(
        output,
        as_attachment=True,
        download_name=f"alternatives_project_{project_id}.xlsx",
        mimetype="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
    )
