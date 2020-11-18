from django.db.models import QuerySet
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from rest_framework.request import Request
from rest_framework.response import Response

from stefan.api.serializers import VoteSerializer
from stefan.models import Vote


class AllVotesViewset(viewsets.ViewSet):
    serializer_class = VoteSerializer

    def list(self, request: Request) -> Response:
        votes = Vote.objects.all()
        serializer = self.serializer_class(instance=votes, many=True)

        return Response(serializer.data)

    def create(self, request):
        pass

# class VoteViewset(viewsets.ModelViewSet):
#     serializer_class = WatchlistEntrySerializer
#     permission_classes = [IsAuthenticated]
#     http_method_names = ['put']
#     lookup_field = 'ticker'
#
#     def get_queryset(self) -> QuerySet:
#         return WatchlistEntry.objects.filter(user=self.request.user).all()
#
#     def update(self, request: Request, *args: Any, **kwargs: Any) -> Response:
#         ticker = kwargs.get('ticker', None)
#         response_content = None
#         if ticker:
#             existing_watchlist_entry = WatchlistEntry.objects.filter(ticker=ticker).first()
#             if not existing_watchlist_entry:
#                 new_watchlist_entry = WatchlistEntry(
#                     user=request.user,
#                     ticker=ticker
#                 )
#                 new_watchlist_entry.save()
#                 serializer = self.get_serializer(new_watchlist_entry)
#                 response_content = serializer.data
#                 status = 200
#             else:
#                 existing_watchlist_entry.delete()
#                 status = 204
#         else:
#             status = 400
#
#         return Response(response_content, status=status)