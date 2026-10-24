import json
from django.http import JsonResponse
from django.views import View
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt

from saludo_app.application.use_cases import SaludarUseCase

@method_decorator(csrf_exempt, name='dispatch')
class SaludoHttpAdapter(View):
    use_case = SaludarUseCase()

    def post(self, request, *args, **kwargs):
        try:
            body = json.loads(request.body)
        except json.JSONDecodeError:
            return JsonResponse({"error": "El cuerpo de la petición debe ser un JSON válido."}, status=400)

        if not isinstance(body, dict):
            return JsonResponse({"error": "El cuerpo JSON debe ser un objeto."}, status=400)

        nombre = body.get("nombre", "")
        if not isinstance(nombre, str):
            return JsonResponse({"error": "El campo 'nombre' debe ser texto."}, status=400)

        try:
            mensaje = self.use_case.ejecutar(nombre=nombre)
        except ValueError as error:
            return JsonResponse({"error": str(error)}, status=400)

        return JsonResponse({"mensaje": mensaje}, status=200)