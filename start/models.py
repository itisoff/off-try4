from django.db import models

class Detail(models.Model):
    TYPE = (
        ('Shopping Bag', 'Shopping Bag'),
        ('Card', 'Card'),
        ('Box', 'Box'),
    )
    PURPOSE = (
        ('Corporate Gifts', 'Corporate Gifts'),
        ('HR', 'HR'),
        ('Packaging', 'Packaging'),
    )
    BUDGET = (
        ('Budget Friendly', 'Budget Friendly'),
        ('Best Rated', 'Best Rated'),
        ('Moderately Priced', 'Moderately Priced'),
        ('Good Quality', 'Good Quality'),
        ('Exotic', 'Exotic'),

    )
    type = models.CharField(max_length=200, blank = False, choices = TYPE)
    purpose = models.CharField(max_length=200, blank = False, choices = PURPOSE)
    quantity = models.IntegerField(default = 1, blank = False)
    length = models.IntegerField(default=0, blank = False)
    width = models.IntegerField(default=0, blank = False)
    depth = models.IntegerField(default=0, blank = False)
    budget = models.CharField(max_length=200, blank = False, choices = BUDGET)
    price1 = models.DecimalField(decimal_places=2, max_digits=10, blank = False)
    price2 = models.DecimalField(decimal_places=2, max_digits=10, blank = False, default=0)


    def __str__(self):
        return (self.type + " + " + self.purpose + " + " + self.budget)
     
class Pricing(models.Model):
    # TYPE = (
    #     ('Shopping Bag', 'Shopping Bag'),
    #     ('Card', 'Card'),
    #     ('Box', 'Box'),
    # )
    # PURPOSE = (
    #     ('Corporate Gifts', 'Corporate Gifts'),
    #     ('HR', 'HR'),
    #     ('Packaging', 'Packaging'),
    # )
    # BUDGET = (
    #     ('Budget Friendly', 'Budget Friendly'),
    #     ('Best Rated', 'Best Rated'),
    #     ('Moderately Priced', 'Moderately Priced'),
    #     ('Good Quality', 'Good Quality'),
    #     ('Exotic', 'Exotic'),

    # )
    type = models.CharField(max_length=200, blank = False)
    purpose = models.CharField(max_length=200, blank = False)
    budget = models.CharField(max_length=200, blank = False)

    def __str__(self):
        return (self.type + " + " + self.purpose + " + " + self.budget)

class Details_of_Entry(models.Model):
    email = models.EmailField(blank=True)
    phone = models.CharField(max_length=42)

    def __str__(self):
        return self.email

