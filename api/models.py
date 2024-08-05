from django.db import models

# Create your models here.


class Certificate(models.Model):
    number = models.CharField(max_length=355, null=True, blank=True)
    verification_code = models.CharField(max_length=355, null=True, blank=True)

    frm = models.CharField(max_length=355, null=True, blank=True)
    to = models.CharField(max_length=355, null=True, blank=True)

    name_address_of_exporter = models.CharField(max_length=355, null=True, blank=True)
    name_address_of_importer = models.CharField(max_length=355, null=True, blank=True)
    distinguishing_marks = models.CharField(max_length=355, null=True, blank=True)
    declared_point_of_entry = models.CharField(max_length=355, null=True, blank=True)

    total_nm_of_packages = models.CharField(max_length=355, null=True, blank=True)
    total_quantity = models.CharField(max_length=355, null=True, blank=True)
    import_permit_no = models.CharField(max_length=355, null=True, blank=True)
    declared_means_of_conveyance = models.CharField(max_length=355, null=True, blank=True)
    declared_means_of_conveyance_left = models.CharField(max_length=355, null=True, blank=True)
    end_use_purpose = models.CharField(max_length=355, null=True, blank=True)

    additional_declaration = models.CharField(max_length=355, null=True, blank=True)


    name_and_signature_of_authorized_officer = models.CharField(max_length=355, null=True, blank=True)
    date_of_inspection = models.CharField(max_length=355, null=True, blank=True)
    date_of_issue = models.CharField(max_length=355, null=True, blank=True)
    place_of_issue = models.CharField(max_length=355, null=True, blank=True)


    concentration_rate = models.CharField(max_length=355, null=True, blank=True)
    treatment = models.CharField(max_length=355, null=True, blank=True)
    treatment_date = models.CharField(max_length=355, null=True, blank=True)
    duration_and_temperature = models.CharField(max_length=355, null=True, blank=True)
    chemicals = models.CharField(max_length=355, null=True, blank=True)


    font_size_1 = models.CharField(max_length=355, null=True, blank=True)
    font_size_2 = models.CharField(max_length=355, null=True, blank=True)


    data = models.JSONField(null=True, blank=True)
    extra_data = models.JSONField(null=True, blank=True)

    def __str__(self):
        return self.number

