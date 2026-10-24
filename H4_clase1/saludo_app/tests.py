from django.test import TestCase


class SaludoHttpAdapterTests(TestCase):
    url = "/api/saludar/"

    def test_returns_greeting_for_valid_name(self):
        response = self.client.post(
            self.url,
            data='{"nombre":"Ana"}',
            content_type="application/json",
        )

        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json(), {"mensaje": "Hola Ana"})

    def test_rejects_missing_or_empty_name(self):
        for payload in ('{}', '{"nombre":"  "}'):
            with self.subTest(payload=payload):
                response = self.client.post(
                    self.url,
                    data=payload,
                    content_type="application/json",
                )

                self.assertEqual(response.status_code, 400)
                self.assertIn("error", response.json())

    def test_rejects_invalid_json(self):
        response = self.client.post(
            self.url,
            data="not-json",
            content_type="application/json",
        )

        self.assertEqual(response.status_code, 400)
        self.assertEqual(
            response.json(),
            {"error": "El cuerpo de la petición debe ser un JSON válido."},
        )

    def test_rejects_non_object_json(self):
        for payload in ('"Ana"', "null", "[]"):
            with self.subTest(payload=payload):
                response = self.client.post(
                    self.url,
                    data=payload,
                    content_type="application/json",
                )

                self.assertEqual(response.status_code, 400)
                self.assertEqual(
                    response.json(),
                    {"error": "El cuerpo JSON debe ser un objeto."},
                )

    def test_rejects_non_string_name(self):
        response = self.client.post(
            self.url,
            data='{"nombre":123}',
            content_type="application/json",
        )

        self.assertEqual(response.status_code, 400)
        self.assertEqual(
            response.json(),
            {"error": "El campo 'nombre' debe ser texto."},
        )
