from django.http import JsonResponse
from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework import status

class SomaView(viewsets.ViewSet):
    def create(self, request):
        try:
            numeros = request.data.get('numeros', [])

            if not isinstance(numeros, list) or not all(isinstance(num, int) for num in numeros):
                return Response({'erro': 'Somente formatos inteiros são aceitos.'})

            resultado = sum(numeros)

            return Response({'resultado': resultado})
        except Exception as e:
            return Response({'erro': str(e)})

    def list(self, request):
        return Response({'message': 'Use POST para enviar a requisição. Requisições aceitas somente em formato JSON.'})




class AritimeticaView(viewsets.ViewSet):
    def create(self, request):
        try:
            numeros = request.data.get('numeros', [])

            if not isinstance(numeros, list) or not all(isinstance(num, int) for num in numeros):
                return Response({'erro': 'Somente formatos inteiros são aceitos.'})

            if len(numeros) == 0:
                return Response({'erro': 'O vetor não pode estar vazio.'})

            media = sum(numeros) / len(numeros)

            return Response({'media': float(media)})

        except Exception as e:
            return Response({'erro': str(e)})

    def list(self, request):
        return Response({'message': 'Use POST para enviar a requisição. Requisições aceitas somente em formato JSON.'})
