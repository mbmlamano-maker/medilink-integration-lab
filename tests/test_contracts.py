import unittest

from medilink_contract import build_summary


class ContractTests(unittest.TestCase):
    def setUp(self):
        self.patient = {"patient_id": "P-1001", "name": "Maria Santos"}
        self.appointments = [{"appointment_id": "A-1", "department": "Cardiology"}]

    def test_summary_preserves_required_public_contract(self):
        result = build_summary(self.patient, self.appointments)
        self.assertEqual(set(result), {"patient", "appointments", "clinic_status"})
        self.assertIn("clinic_status", result)

    def test_summary_values_are_preserved(self):
        result = build_summary(self.patient, self.appointments)
        self.assertEqual(result["patient"], self.patient)
        self.assertEqual(result["appointments"], self.appointments)

    def test_default_clinic_status_is_active(self):
        self.assertEqual(build_summary(self.patient, [])["clinic_status"], "ACTIVE")

    def test_clinic_status_is_normalized(self):
        result = build_summary(self.patient, [], " maintenance ")
        self.assertEqual(result["clinic_status"], "MAINTENANCE")

    def test_output_does_not_alias_inputs(self):
        result = build_summary(self.patient, self.appointments)
        self.assertIsNot(result["patient"], self.patient)
        self.assertIsNot(result["appointments"], self.appointments)

    def test_rejects_non_dict_patient(self):
        with self.assertRaises(ValueError):
            build_summary("not-a-dict", [])

    def test_rejects_missing_or_blank_patient_id(self):
        with self.assertRaises(ValueError):
            build_summary({"name": "No ID"}, [])
        with self.assertRaises(ValueError):
            build_summary({"patient_id": "   "}, [])

    def test_rejects_non_list_appointments(self):
        with self.assertRaises(ValueError):
            build_summary(self.patient, "nope")

    def test_rejects_blank_or_non_string_status(self):
        with self.assertRaises(ValueError):
            build_summary(self.patient, [], "   ")
        with self.assertRaises(ValueError):
            build_summary(self.patient, [], 123)


if __name__ == "__main__":
    unittest.main()
