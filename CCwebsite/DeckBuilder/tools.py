import json
import os
from copy import copy
from turtle import color

def add_color(count_colors, unit_name):
    unit = unit_name.split('/')
    if len(unit) == 2 and unit[0] in count_colors:
        count_colors[unit[0]] += 1


def count_nonzero_colors(count_colors):
    cnt = 0
    for val in count_colors.values():
        if val > 0:
            cnt += 1
    return cnt


def is_proper_slot_idx(key, deck_switch):
    key_id = int(key.split("slot")[-1])
    return (deck_switch == 1 and key_id >= 13) or (deck_switch == 0 and key_id < 13)
    

def copy_session_information(context, request):
    count_colors = {"black": 0, "blue": 0, "green": 0, "white": 0}
    for key in request.session.keys():
        context[key] = request.session[key]
        if "slot" in key and is_proper_slot_idx(key, request.session["deck_switch"]):
            add_color(count_colors, context[key])
    ncolors_in_deck = count_nonzero_colors(count_colors)
    count_colors["crystal"] = -1
    return [count_colors, ncolors_in_deck]


def get_clickedbutton_name(request_dict):
    key_ids = [key for key in request_dict.keys() if key != 'csrfmiddlewaretoken']
    if len(key_ids) == 0:
        return None
    return key_ids[0].split(".")[0].split(";")


def process_unit_button(button_name, context, request, color_info):
    unit_type, unit_name = button_name[1].split("/")
    color_dict, ncolors = color_info
    if ncolors >= 2 and color_dict[unit_type] == 0:             # Max available number of colors already
        return    
    if context["deck_switch"]:
        lb, rb = 13, 25
    else:
        lb, rb = 1, 13
    for i in range(lb, rb):
        if context["slot" + str(i)] == "empty.jpg":
            context["slot" + str(i)] = os.path.join(unit_type, unit_name) + ".png"
            request.session["slot" + str(i)] = os.path.join(unit_type, unit_name) + ".png"
            break


def process_slot_button(button_name, context, request):
    #if is_proper_slot_idx("slot" + button_name[1], request.session["deck_switch"]):
    context["slot" + button_name[1]] = "empty.jpg"
    request.session["slot" + button_name[1]] = "empty.jpg"


def process_button_button(button_name, context, request):
    color = button_name[1]
    color_matching = json.load(open("templates/static/jsons/color_matching.json", "r"))
    context["maket_name"] = color_matching[color][0]
    request.session["maket_name"] = color_matching[color][0]
    tree_layout = json.load(open(f"templates/static/jsons/{color_matching[color][1]}", "r"))
    context["tree_layout"] = tree_layout["tree_layout"]
    request.session["tree_layout"] = tree_layout["tree_layout"]


def process_switcher_button(button_name, context, request):
    if int(button_name[1]) == 1:
        switch_val = 0
    else:
        switch_val = 1
    context["deck_switch"] = switch_val
    request.session["deck_switch"] = switch_val


def process_deckbuilder_request(request):
    context = json.load(open("templates/static/jsons/deckbuilder_state_default.json", "r"))
    color_info = copy_session_information(context, request)
    button_name = get_clickedbutton_name(request.GET.dict())
    if button_name is None:    # No changes provided
        return context
    if button_name[0] == "unit":
        process_unit_button(button_name, context, request, color_info)
    elif button_name[0] == "chosenslot":
        process_slot_button(button_name, context, request)
    elif button_name[0] == "button":
        process_button_button(button_name, context, request)
    elif button_name[0] == "switcher":
        process_switcher_button(button_name, context, request)
    return context
