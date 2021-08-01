from django.db import models
from django.urls import reverse


class MenuSections(models.Model):
    name = models.CharField("Section's name", max_length=200)
    image = models.ImageField(upload_to='images/menu_sections')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Раздел меню"
        verbose_name_plural = "Разделы меню"
        ordering = [ "name"]

    def get_absolute_url(self):
        return reverse('menu_section', kwargs={'menu_section_id': self.pk})


class Rubrics(models.Model):
    name = models.CharField("Rubric's name", max_length=200)
    image = models.ImageField(upload_to='images/rubrics')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Вид кухни"
        verbose_name_plural = "Виды кухни"
        ordering = ["name"]

    def get_absolute_url(self):
        return reverse('rubric', kwargs={'rubric_id': self.pk})

class Restaurants(models.Model):
    name = models.CharField("Restaurant's name", max_length=200)
    rubric_id = models.ForeignKey(Rubrics, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='images/restaurants')

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('restaurant', kwargs={'restaurant_id': self.pk})

    class Meta:
        verbose_name = "Ресторан"
        verbose_name_plural = "Рестораны"
        ordering = ["name"]


class Dishes(models.Model):
    name = models.CharField("Название", max_length=200)
    description = models.TextField("Описание")
    price = models.DecimalField("Цена", max_digits=9, decimal_places=2)
    image = models.ImageField(upload_to='static/dishes')
    rubric_id = models.ForeignKey(Rubrics, on_delete=models.CASCADE)
    restaurant_id = models.ForeignKey(Restaurants, on_delete=models.CASCADE)
    menu_section_id = models.ForeignKey(MenuSections, on_delete=models.CASCADE)
    created_at = models.DateTimeField("Дата создания", auto_now_add=True)
    updated_at = models.DateTimeField("Дата редактирования", auto_now=True)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('dish', kwargs={'dish_id': self.pk})

    class Meta:
        verbose_name = "Блюдо"
        verbose_name_plural = "Блюда"
        ordering = ['created_at', "name"]

