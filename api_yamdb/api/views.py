from django.db.models import Avg
from rest_framework import viewsets
from rest_framework.generics import get_object_or_404
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from reviews.filters import TitleFilter
from reviews.models import Category, Genre, Review, Title
from api.permissions import IsAdminOrAuthorOrReadOnly, IsAdminOrReadOnly

from api.mixins import ListCreateDestroyViewSet
from api.serializers import (
    CategorySerializer,
    CommentSerializer,
    GenreSerializer,
    ReviewSerializer,
    TitleSerializer,
    TitleWriteSerializer,
)


class GenreViewSet(ListCreateDestroyViewSet):
    serializer_class = GenreSerializer
    queryset = Genre.objects.all()
    permission_classes = (IsAdminOrReadOnly,)


class CategoryViewSet(ListCreateDestroyViewSet):
    serializer_class = CategorySerializer
    queryset = Category.objects.all()
    permission_classes = (IsAdminOrReadOnly,)


class ReviewViewSet(viewsets.ModelViewSet):
    serializer_class = ReviewSerializer
    permission_classes = [IsAuthenticatedOrReadOnly, IsAdminOrAuthorOrReadOnly]

    def get_queryset(self):
        title = get_object_or_404(Title, id=self.kwargs.get("title_id"))
        return title.reviews.all()

    def perform_create(self, serializer):
        title = get_object_or_404(Title, id=self.kwargs.get("title_id"))
        serializer.save(author=self.request.user, title=title)

    def perform_update(self, serializer):
        serializer.save()


class CommentViewSet(viewsets.ModelViewSet):
    serializer_class = CommentSerializer
    permission_classes = [IsAuthenticatedOrReadOnly, IsAdminOrAuthorOrReadOnly]

    def get_queryset(self):
        review = get_object_or_404(Review, id=self.kwargs.get("review_id"))
        return review.comments.all()

    def perform_create(self, serializer):
        review = get_object_or_404(Review, id=self.kwargs.get("review_id"))
        serializer.save(author=self.request.user, review=review)


class TitleViewSet(viewsets.ModelViewSet):
    permission_classes = (IsAdminOrReadOnly,)
    serializer_class = TitleSerializer
    queryset = Title.objects.annotate(rating=Avg("reviews__score")).order_by("id")
    filterset_class = TitleFilter
    ordering_fields = ["name"]

    # def perform_create(self, serializer):
    #     category = get_object_or_404(
    #         Category, slug=self.request.data.get('category')
    #     )
    #     genre = Genre.objects.filter(
    #         slug__in=self.request.data.get('genre')
    #     )
    #     serializer.save(category=category, genre=genre)

    # def perform_update(self, serializer):
    #     serializer.save()
    #     category = get_object_or_404(
    #         Category, slug=self.request.data.getlist('category')
    #     )
    #     genre = Genre.objects.filter(
    #         slug__in=self.request.data.getlist('genre')
    #     )
    #     serializer.save(category=category, genre=genre)

    def get_serializer_class(self):
        if self.request.method == "GET":
            return TitleSerializer
        return TitleWriteSerializer
