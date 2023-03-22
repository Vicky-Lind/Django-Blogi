from django.db import models
from django.utils.translation import gettext_lazy as _

# This creates a class Postaus which holds all necessary data for a post
class Postaus(models.Model):
    otsikko = models.CharField(max_length=200)
    otsikko_lower = models.CharField(max_length=200, help_text="Exact same as normal title but in lowercase", null=True)
    ingressi = models.TextField(blank=True)
    teksti = models.TextField()
    kuva = models.ImageField(upload_to="blogi/kuvat", null=True, blank=True)
    luotu = models.DateTimeField(auto_now_add=True)

    # This changes the name of the class in the admin panel
    class Meta:
        verbose_name = _("postaus")
        verbose_name_plural = _("postaukset")

    def __str__(self):
        return self.otsikko

    def luo_ingressi(self):
        if self.ingressi:
            return self.ingressi
        # If there isn't an ingress, then show instead the 50 first-
        # characters of the text
        return self.teksti[:50] + "..."