from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from head_teacher_app import models, serializers


class RoomListCreateAPIView(APIView):
    """
    Handles GET (list all rooms) and POST (create a new room).
    """

    def get(self, request):
        rooms = models.Room.objects.all()
        serializer = serializers.RoomSerializer(rooms, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request):
        serializer = serializers.RoomSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class RoomDetailAPIView(APIView):
    """
    Handles GET, PUT, PATCH, and DELETE for a single room.
    """

    def get_object(self, pk):
        try:
            return models.Room.objects.get(pk=pk)
        except models.Room.DoesNotExist:
            return None

    def get(self, request, pk):
        room = self.get_object(pk)

        if room is None:
            return Response({"error": "Room not found"}, status=status.HTTP_404_NOT_FOUND)

        serializer = serializers.RoomSerializer(room)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def put(self, request, pk):
        room = self.get_object(pk)

        if room is None:
            return Response({"error": "Room not found"}, status=status.HTTP_404_NOT_FOUND)

        serializer = serializers.RoomSerializer(room, data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def patch(self, request, pk):
        room = self.get_object(pk)

        if room is None:
            return Response({"error": "Room not found"}, status=status.HTTP_404_NOT_FOUND)

        serializer = serializers.RoomSerializer(room, data=request.data, partial=True)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        room = self.get_object(pk)

        if room is None:
            return Response({"error": "Room not found"}, status=status.HTTP_404_NOT_FOUND)

        room.delete()
        return Response({"message": "Room deleted successfully"}, status=status.HTTP_204_NO_CONTENT)
