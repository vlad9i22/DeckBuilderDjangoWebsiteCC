import json
import os
import sys
sys.path.insert(1, os.path.abspath('DeckBuilder'))
import tools


def test_sort_1():
    context = json.load(open("templates/static/jsons/deckbuilder_state_default.json", "r"))
    context2 = json.load(open("templates/static/jsons/deckbuilder_state_default.json", "r"))
    tools.sort_deck(context)
    for key in context2:
        assert context2[key] == context[key]
    assert len(context) == len(context2)


def test_sort_2():
    context = json.load(open("templates/static/jsons/deckbuilder_state_default.json", "r"))
    context["slot1"] = "black/bane.png"
    context["slot3"] = "black/lich_spawner.png"
    context2 = json.load(open("templates/static/jsons/deckbuilder_state_default.json", "r"))
    context2["slot1"] = "black/bane.png"
    context2["slot12"] = "black/lich_spawner.png"
    tools.sort_deck(context)
    for key in context2:
        assert context2[key] == context[key]
    assert len(context) == len(context2)


def test_sort_3():
    context = json.load(open("templates/static/jsons/deckbuilder_state_default.json", "r"))
    context["slot1"] = "black/bane.png"
    context["slot3"] = "black/lich_spawner.png"
    context["slot12"] = "blue/conductor.png"
    context["slot15"] = "black/bane.png"
    context2 = json.load(open("templates/static/jsons/deckbuilder_state_default.json", "r"))
    context2["slot1"] = "black/bane.png"
    context2["slot12"] = "black/lich_spawner.png"
    context2["slot2"] = "blue/conductor.png"
    context2["slot15"] = "black/bane.png"
    tools.sort_deck(context)
    for key in context2:
        assert context2[key] == context[key]
    assert len(context) == len(context2)


def test_sort_4():
    context = json.load(open("templates/static/jsons/deckbuilder_state_default.json", "r"))
    context["slot1"] = "black/bane.png"
    context["slot3"] = "black/lich_spawner.png"
    context["slot12"] = "blue/conductor.png"
    context["slot15"] = "black/bane.png"
    context2 = json.load(open("templates/static/jsons/deckbuilder_state_default.json", "r"))
    context2["slot1"] = "black/bane.png"
    context2["slot3"] = "black/lich_spawner.png"
    context2["slot12"] = "blue/conductor.png"
    context2["slot13"] = "black/bane.png"
    context["deck_switch"] = 1
    context2["deck_switch"] = 1
    tools.sort_deck(context)
    for key in context2:
        assert context2[key] == context[key]
    assert len(context) == len(context2)


def test_process_unit_1():
    context = json.load(open("templates/static/jsons/deckbuilder_state_default.json", "r"))
    button_name = ["unit", "black/bane"]
    colors = [{"crystal": 3,
               "black": 1,
               "blue": 2},
              3]
    tools.process_unit_button(button_name, context, colors)
    assert context["slot1"] == "black/bane.png"


def test_process_unit_2():
    context = json.load(open("templates/static/jsons/deckbuilder_state_default.json", "r"))
    button_name = ["unit", "black/bane"]
    colors = [{"crystal": 3,
               "green": 1,
               "blue": 2,
               "black": 0,
               "white": 0}, 2]
    tools.process_unit_button(button_name, context, colors)
    assert context["slot1"] == "empty.jpg"


def test_process_slot_1():
    context = json.load(open("templates/static/jsons/deckbuilder_state_default.json", "r"))
    button_name = ["chosenslot", "1"]
    tools.process_slot_button(button_name, context)
    assert context["slot1"] == "empty.jpg"


def test_process_slot_2():
    context = json.load(open("templates/static/jsons/deckbuilder_state_default.json", "r"))
    context["slot1"] = "black/bane"
    button_name = ["chosenslot", "1"]
    tools.process_slot_button(button_name, context)
    assert context["slot1"] == "empty.jpg"


def test_process_slot_3():
    context = json.load(open("templates/static/jsons/deckbuilder_state_default.json", "r"))
    context["slot1"] = "black/bane"
    context["slot2"] = "black/bane_spawner"
    button_name = ["chosenslot", "1"]
    tools.process_slot_button(button_name, context)
    assert context["slot1"] == "empty.jpg"
    assert context["slot2"] == "black/bane_spawner"


def test_process_clean_1():
    context = json.load(open("templates/static/jsons/deckbuilder_state_default.json", "r"))
    context["slot1"] = "black/bane"
    context["slot20"] = "black/bane_spawner"
    context["slot10"] = "black/bane_spawner"
    context["slot18"] = "black/bane_spawner"
    tools.process_clean_button(context)
    for i in range(1, 25):
        assert context["slot" + str(i)] == "empty.jpg"


def test_count_colors_1():
    colors = {"crystal": 3,
              "green": 1,
              "blue": 2,
              "black": 0,
              "white": 0}
    assert tools.count_nonzero_colors(colors) == 3


def test_count_colors_2():
    colors = {"crystal": 0,
              "green": 0,
              "blue": 0,
              "black": 0,
              "white": 0}
    assert tools.count_nonzero_colors(colors) == 0
