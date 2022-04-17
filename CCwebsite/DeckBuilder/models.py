from django.db import models

# Create your models here.
class DeckStructure(models.Model):
    slot1 = models.CharField('Slot1_name', max_length=30)
    slot2 = models.CharField('Slot2_name', max_length=30)
    slot3 = models.CharField('Slot3_name', max_length=30)
    slot4 = models.CharField('Slot4_name', max_length=30)
    slot5 = models.CharField('Slot5_name', max_length=30)
    slot6 = models.CharField('Slot6_name', max_length=30)
    slot7 = models.CharField('Slot7_name', max_length=30)
    slot8 = models.CharField('Slot8_name', max_length=30)
    slot9 = models.CharField('Slot9_name', max_length=30)
    slot10 = models.CharField('Slot10_name', max_length=30)
    slot11 = models.CharField('Slot11_name', max_length=30)
    slot12 = models.CharField('Slot12_name', max_length=30)
    slot13 = models.CharField('Slot13_name', max_length=30)
    slot14 = models.CharField('Slot14_name', max_length=30)
    slot15 = models.CharField('Slot15_name', max_length=30)
    slot16 = models.CharField('Slot16_name', max_length=30)
    slot17 = models.CharField('Slot17_name', max_length=30)
    slot18 = models.CharField('Slot18_name', max_length=30)
    slot19 = models.CharField('Slot19_name', max_length=30)
    slot20 = models.CharField('Slot20_name', max_length=30)
    slot21 = models.CharField('Slot21_name', max_length=30)
    slot22 = models.CharField('Slot22_name', max_length=30)
    slot23 = models.CharField('Slot23_name', max_length=30)
    slot24 = models.CharField('Slot24_name', max_length=30)
    maket_name = models.CharField('Maket_name', max_length=30)
    
    def __str__(self):
        return "DeckStructure"


class SimpleModel(models.Model):
    path = models.CharField(max_length=30)
    
    def __str__(self) -> str:
        return "HI"
    