from django_filters.rest_framework import DjangoFilterBackend

from rest_framework import  status, viewsets, permissions
from rest_framework.response import Response
from rest_framework.decorators import action
from rest_framework.permissions import IsAuthenticated

from .models import Poem, Favorite
from .filters import PoemFilter
from .permissions import IsOwner
from .serializers import PoemModelSerializer, FavoriteSerializer, SummarySerializer
from .summarizer import invoke 

class PoemViewSet(viewsets.ModelViewSet):
    queryset = Poem.objects.filter(is_deleted=False)
    serializer_class = PoemModelSerializer 
    permission_classes = [permissions.IsAuthenticatedOrReadOnly, IsOwner]
    filter_backends = [DjangoFilterBackend]
    filterset_class = PoemFilter

    def perform_create(self, serializer):
        serializer.save(created_by=self.request.user)

    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()
        self.perform_destroy(instance)
        return Response(status=status.HTTP_204_NO_CONTENT)
    
    def perform_destroy(self, instance):
        instance.is_deleted=True
        instance.save(update_fields=['is_deleted'])

    @action(
        detail=True,
        methods=['post'],
        permission_classes=[IsAuthenticated]
    )
    
    def favorite(self, request, pk=None):
        queryset = self.get_queryset()

        try:
            poem = queryset.get(pk=pk)
        except Poem.DoesNotExist:
            return Response({'status': 'Poem not found or has been deleted'}, status=status.HTTP_404_NOT_FOUND) 
        favorite, created = Favorite.objects.get_or_create(user=request.user, poem=poem)
        if created:
            return Response({'status': 'Poem marked as favorite'}, status=status.HTTP_201_CREATED)
        return Response({'status': 'Poem already marked as favorite'}, status=status.HTTP_200_OK)

    @action(detail=True, methods=['post'], permission_classes=[IsAuthenticated])
    def unfavorite(self, request, pk=None):
        poem = self.get_object()
        try:
            favorite = Favorite.objects.get(user=request.user, poem=poem)
            favorite.delete()
            return Response({'status': 'poem unmarked as favorite'}, status=status.HTTP_204_NO_CONTENT)
        except Favorite.DoesNotExist:
            return Response({'status': 'Poem was not marked as favorite'}, status=status.HTTP_400_BAD_REQUEST)
        
    @action(detail=False, methods=['get'], permission_classes=[IsAuthenticated])
    def list_favorites(self, request):
        favorites = Favorite.objects.filter(user=request.user) 
        serializer = FavoriteSerializer(many=True) 
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    @action(detail=False, methods=['get'])
    def summarize(self, request, pk=None):
        queryset = self.get_queryset()
        poems = queryset.values('id', 'poems')

        if not poems:
            return Response({'error': 'No poems found'}, status=status.HTTP_404_NOT_FOUND)

        summaries = []
        
        for poem in poems:
            poem_id = poem['id']
            poem_text = poem['poems']

            try:
                # Call the summarizer function for each poem
                summary = invoke(poem_text)
                summaries.append({'id': poem_id, 'summary': summary})
            except Exception as e:
                summaries.append({'id': poem_id, 'error': str(e)})

        return Response({'summaries': summaries}, status=status.HTTP_200_OK)
    
    def get_permissions(self):
        if self.action == 'list':
            return [permissions.AllowAny()]
        return super().get_permissions()
        