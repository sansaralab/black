from .models import Complaint, PersonSummary, Category
from django.core.exceptions import ObjectDoesNotExist
from typing import List


def make_complaint(identity: str, content: str, category: str):
    cat, cat_created = Category.objects.get_or_create(title=category)
    complaint = Complaint.objects.create(identity=identity, content=content, category=cat)
    try:
        person = PersonSummary.objects.get(identity=identity)
    except ObjectDoesNotExist:
        person = PersonSummary.objects.create(identity=identity, complaints=[])
    person.complaints.append(complaint.id)
    person.save()


def search_categories(template: str) -> List[str]:
    categories = Category.objects.filter(title__istartswith=template).values("title")[:30]
    return [cat['title'] for cat in categories]


def search_complaints(identity: str, frame: int = 1) -> List[Complaint]:
    window = 30
    person = PersonSummary.objects.get(identity=identity)
    return Complaint.objects.filter(pk__in=person.complaints)[window * (frame-1):window*frame]


def prepare_identity(identity: str) -> str:
    return identity
