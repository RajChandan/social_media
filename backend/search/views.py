import requests
from django.conf import settings
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated

class SearchView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self,request):
        query = request.GET.get("q","").strip()
        if not query:
            return Response({"error":"no query to search"})

        es_url = "http://localhost:9200/posts/_search"
        payload = {
            "query" : {
                "multi_match" : {
                    "query" : query,
                    "fields" : ["content","author.username"]
                }
            }
        }

        try:
            response = requests.get(es_url,json=payload)
            data = response.json()
            return Response(data,status = response.status_code)
        except requests.exceptions.RequestException as e:
            return Response({"error":str(e)},status=500)


