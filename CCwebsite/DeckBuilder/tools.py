import json
import os


def add_color(count_colors: dict, unit_name: str) -> None:
    '''
    Check if color needs to be counted for CC rules
    '''
    unit = unit_name.split('/')
    if len(unit) == 2 and unit[0] in count_colors:
        count_colors[unit[0]] += 1


def count_nonzero_colors(count_colors: dict) -> int:
    '''
    Counts number of units in deck for each color.
    '''
    cnt = 0
    for val in count_colors.values():
        if val > 0:
            cnt += 1
    return cnt


def is_proper_slot_idx(key: str, deck_switch: int) -> bool:
    '''
    Determines if proper slot of deck is chosen. Depends on deck_switch value and slot_id
    '''
    key_id = int(key.split("slot")[-1])
    return (deck_switch == 1 and key_id >= 13) or (deck_switch == 0 and key_id < 13)


def copy_session_information(context: dict, request) -> list:
    '''
    Moves session information to context dictionary and collects unit color information for future processing
    
    Return value is the list of 2 elements: 1) dict -> number of each color in deck
                                            2) int  -> number of distinct colors in deck
    '''
    count_colors = {"black": 0, "blue": 0, "green": 0, "white": 0}
    for key in request.session.keys():
        context[key] = request.session[key]
        if "slot" in key and is_proper_slot_idx(key, request.session["deck_switch"]):
            add_color(count_colors, context[key])
    ncolors_in_deck = count_nonzero_colors(count_colors)
    count_colors["crystal"] = -1
    return [count_colors, ncolors_in_deck]


def get_clickedbutton_name(request_dict: dict) -> str:
    '''
    Gets the name of the button which was pressed by user
    '''
    key_ids = [key for key in request_dict.keys() if key != 'csrfmiddlewaretoken']
    if len(key_ids) == 0:
        return None
    return key_ids[0].split(".")[0].split(";")


def process_unit_button(button_name: list, context: dict, request, color_info: list) -> None:
    '''
    Processes click on any unit button (button name contains "unit")
    '''
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


def process_slot_button(button_name: list, context: dict, request) -> None:
    '''
    Processes click on any slot button (button name contains "slot")
    '''
    # if is_proper_slot_idx("slot" + button_name[1], request.session["deck_switch"]):
    context["slot" + button_name[1]] = "empty.jpg"
    request.session["slot" + button_name[1]] = "empty.jpg"


def process_button_button(button_name: list, context: dict, request) -> None:
    '''
    Processes click on any button button (button name contains "button")
    '''
    color = button_name[1]
    color_matching = json.load(open("templates/static/jsons/color_matching.json", "r"))
    context["maket_name"] = color_matching[color][0]
    request.session["maket_name"] = color_matching[color][0]
    tree_layout = json.load(open(f"templates/static/jsons/{color_matching[color][1]}", "r"))
    context["tree_layout"] = tree_layout["tree_layout"]
    request.session["tree_layout"] = tree_layout["tree_layout"]


def process_switcher_button(button_name: list, context: dict, request) -> None:
    '''
    Processes click on switcher button (button name contains "switcher")
    '''
    if int(button_name[1]) == 1:
        switch_val = 0
    else:
        switch_val = 1
    context["deck_switch"] = switch_val
    request.session["deck_switch"] = switch_val


def process_deckbuilder_request(request):
    '''
    Processes and parses deckbuild webpage request
    '''
    context = json.load(open("templates/static/jsons/deckbuilder_state_default.json", "r"))
    if "deck_switch" not in request.session.keys():
        request.session["deck_switch"] = 0
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
