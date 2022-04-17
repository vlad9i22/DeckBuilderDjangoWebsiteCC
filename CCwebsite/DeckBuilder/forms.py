from .models import DeckStructure, SimpleModel
from django.forms import ModelForm
import json

class DeckBuilderForm(ModelForm):
    class Meta:
        model = DeckStructure
        fields = ["slot1"]
        #fields = ["maket_name", "slot1", "slot2", "slot3", "slot4", "slot5", "slot6", "slot7", "slot8", "slot9", "slot10", "slot11", "slot12", "slot13", "slot14", "slot15", "slot16", "slot17", "slot18", "slot19", "slot20", "slot21", "slot22", "slot23", "slot24"]
        
        
    def fill_fields_standart(self):
        context = json.load(open("templates/static/base_template_standart.json", "r"))
        self.maket_name = context["maket_name"]
        self.slot1 = context["slot1"]
        self.slot2 = context["slot2"]
        self.slot3 = context["slot3"]
        self.slot4 = context["slot4"]
        self.slot5 = context["slot5"]
        self.slot6 = context["slot6"]
        self.slot7 = context["slot7"]
        self.slot8 = context["slot8"]
        self.slot9 = context["slot9"]
        self.slot10 = context["slot10"]
        self.slot11 = context["slot11"]
        self.slot12 = context["slot12"]
        self.slot13 = context["slot13"]
        self.slot14 = context["slot14"]
        self.slot15 = context["slot15"]
        self.slot16 = context["slot16"]
        self.slot17 = context["slot17"]
        self.slot18 = context["slot18"]
        self.slot19 = context["slot19"]
        self.slot20 = context["slot20"]
        self.slot21 = context["slot21"]
        self.slot22 = context["slot22"]
        self.slot23 = context["slot23"]
        self.slot24 = context["slot24"]
        self.tree_layout = context["tree_layout"]
        

class SimpleModelForm(ModelForm):
    class Meta:
        model = SimpleModel
        fields = ["path"]