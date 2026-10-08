import json

from medilink_contract import build_summary

patient = {"patient_id": "P-1001", "name": "Maria Santos"}
appointments = [
    {"appointment_id": "A-1", "date": "2026-10-12", "department": "Cardiology"},
    {"appointment_id": "A-2", "date": "2026-10-19", "department": "Laboratory"},
]

summary = build_summary(patient, appointments, "maintenance")
print(json.dumps(summary, indent=2))
