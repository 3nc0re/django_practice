from django.shortcuts import render
from app.models import Producer, Substance, Medicine, OrgTypes, Jurisdictions, Organization, MedicineOrganization

def add_medicine(request):
    if request.method == "POST":
        name = request.POST.get("name")
        producer = request.POST.get("producer")
        expiration_date = request.POST.get("expiration_date")
        substance_class = request.POST.get("substance_class")
        is_generic = request.POST.get("is_generic")
        price = request.POST.get("price")
        form = request.POST.get("form")
        producer_obj = Producer.objects.get(name=producer)
        substance_obj = Substance.objects.get(type_name=substance_class)
        Medicine.objects.create(name=name, producer=producer_obj, expiration_date=expiration_date,
                                substance_class=substance_obj, is_generic=is_generic, price=price, form=form)
    return render(request, "add_medicine.html", {"producers": Producer.objects.all(),
                                                 "substances": Substance.objects.all()})

def universal(request):
    return render(request, "universal.html")

def add_organization(request):
    if request.method == "POST":
        company_name = request.POST.get("company_name")
        company_address = request.POST.get("company_address")
        jurisdiction = request.POST.get("jurisdiction")
        organization_type = request.POST.get("organization_type")
        contact_person = request.POST.get("contact_person")
        jurisdiction_obj = Jurisdictions.objects.get(name=jurisdiction)
        organization_type_obj = OrgTypes.objects.get(org_name=organization_type)
        Organization.objects.create(company_name=company_name, company_address=company_address,
                                    jurisdiction=jurisdiction_obj, organization_type=organization_type_obj,
                                    contact_person=contact_person)
    return render(request, "add_organization.html", {"jurisdictions": Jurisdictions.objects.all(),
                                                      "organization_types": OrgTypes.objects.all()})



def display_medicine_for_organization(request):
    if request.method == "POST":
        organization = request.POST.get("organization")
        organization_obj = Organization.objects.get(company_name=organization)
        medicine_organization = MedicineOrganization.objects.filter(organization=organization_obj)
        medicines = [medicine.medicine for medicine in medicine_organization]

        return render(request, "display_medicine_for_organization.html", {"medicines": medicines})

    return render(request, "display_medicine_for_organization.html")

def display_organizations_for_medicine(request):
    if request.method == "POST":
        medicine = request.POST.get("medicine")
        medicine_obj = Medicine.objects.get(name=medicine)
        medicine_organization = MedicineOrganization.objects.filter(medicine=medicine_obj)
        organizations = []
        for organization in medicine_organization:
            organizations.append(organization.organization)
