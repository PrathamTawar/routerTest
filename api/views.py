from rest_framework import viewsets
from rest_framework.response import Response

class testViewSet(viewsets.ViewSet):
    def list(self, request):
        data = {
            'message': 'Hello World'
        }
        return Response(data)
    
    def retrieve(self, request, pk = None):
        
        return Response(f"this is {pk}")
    
    def destroy(self, request, pk = None):
        
        return Response(f"deleted {pk}")