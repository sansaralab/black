from .models import Complaint, PersonSummary, Category
from django.core.exceptions import ObjectDoesNotExist
from django.db import transaction
from typing import List


@transaction.atomic
def make_complaint(identity: str, content: str, category: str):
    identity = prepare_identity(identity)
    cat, cat_created = Category.objects.get_or_create(title=category)
    complaint = Complaint.objects.create(identity=identity, content=content, category=cat)
    try:
        person = PersonSummary.objects.get(identity=identity)
    except ObjectDoesNotExist:
        person = PersonSummary.objects.create(identity=identity, complaints=[])
    person.complaints.append(complaint.id)
    person.complaints_count += 1
    person.save()


def search_categories(template: str) -> List[str]:
    categories = Category.objects.filter(title__istartswith=template).values("title")[:30]
    return [cat['title'] for cat in categories]


def search_complaints(identity: str, frame: int = 1) -> List[Complaint]:
    window = 30
    try:
        person = PersonSummary.objects.get(identity=identity)
        complaints = Complaint.objects.filter(pk__in=person.complaints).order_by('-likes', '-create_date')[window * (frame-1):window*frame]
    except ObjectDoesNotExist:
        return []

    return complaints


def prepare_identity(identity: str) -> str:
    return identity
