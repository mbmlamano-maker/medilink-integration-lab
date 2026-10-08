def build_summary(patient: dict, appointments: list[dict], clinic_status: str = "ACTIVE") -> dict:
    if not isinstance(patient, dict):
        raise ValueError("patient must be a dictionary")
    if "patient_id" not in patient or not str(patient["patient_id"]).strip():
        raise ValueError("patient must contain a non-empty patient_id")
    if not isinstance(appointments, list):
        raise ValueError("appointments must be a list")
    if not isinstance(clinic_status, str) or not clinic_status.strip():
        raise ValueError("clinic_status must be a non-empty string")

    return {
        "patient": dict(patient),
        "appointments": list(appointments),
        "clinic_status": clinic_status.strip().upper(),
    }
