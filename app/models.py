from django.conf import settings
from django.db import models
from django.utils import timezone


class Producer(models.Model):
    name = models.CharField(max_length=100)
    address = models.CharField(max_length=400)

    def __str__(self):
        return f"{self.name}: located in {self.address}"

class Substance(models.Model):
    type_name = models.CharField(max_length=100)
    laws_specifics = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.type_name} {self.laws_specifics}"


class Medicine(models.Model):
    name = models.CharField(max_length=150)
    producer = models.ForeignKey(Producer, on_delete=models.CASCADE)
    expiration_date = models.DateField()
    substance_class = models.ForeignKey(Substance, on_delete=models.CASCADE)
    is_generic = models.CharField(max_length=100)
    price = models.CharField(max_length=100)
    form = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.name}, producer: {str(self.producer)}, \
                 class: {self.substance_class}, \
                 expires: {self.expiration_date}, {self.is_generic}"


class OrgTypes(models.Model):
    org_name = models.CharField(max_length=100)
    org_description = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.org_name}: {self.org_description}"


class Jurisdictions(models.Model):
    name = models.CharField(max_length=100)
    phone_code = models.CharField(max_length=100)


class Organization(models.Model):
    company_name = models.CharField(max_length=100)
    company_address = models.CharField(max_length=100)
    jurisdiction = models.ForeignKey(Jurisdictions, on_delete=models.CASCADE)
    organization_type = models.ForeignKey(OrgTypes, on_delete=models.CASCADE)
    contact_person = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.company_name} {self.organization_type} at {self.company_address}"

class MedicineOrganization(models.Model):
    medicine = models.ForeignKey(Medicine, on_delete=models.CASCADE)
    organization = models.ForeignKey(Organization, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.medicine} - {self.organization}"





