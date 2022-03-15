from django.db import models
from django.contrib.auth import get_user_model


User = get_user_model()


class Title(models.Model):
    pass


class Review(models.Model):
    """Модель ревью работ"""
    text = models.TextField()
    title = models.CharField(max_length=100)
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name="reviews")
    score = models.IntegerField()
    pub_date = models.DateTimeField(auto_now_add=True)

    class Meta:
        constraints = [models.UniqueConstraint(fields=("title",), name="unique_title")]

    def __str__(self):
        return self.text


class Comment(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name="comments")
    review = models.ForeignKey(
        Review, on_delete=models.CASCADE, related_name="comments"
    )
    text = models.TextField()
    pub_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.text
