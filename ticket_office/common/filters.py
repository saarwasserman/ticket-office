from django.core.exceptions import FieldError

from rest_framework import filters


class IsUserFilterBackend(filters.BaseFilterBackend):
    """
    Filter that only allows users to see their own objects.
    """
    def filter_queryset(self, request, queryset, view):
        try:
            return queryset.filter(user=request.user)
        except FieldError as e:
            return queryset.all()
