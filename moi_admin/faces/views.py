from rest_framework.views import APIView
from rest_framework.response import Response
from faces.models import Face


class ListFaces(APIView):
    """
    View to list all faces in the system.
    """

    def get(self, request, format=None):
        """
        Return a list of all faces.
        """
        faces = {face.name: face.encoding for face in Face.objects.all()}
        return Response(faces)
