import json
import os

def process_deckbuilder_request(request):
    context = json.load(open("templates/static/jsons/deckbuilder_state_default.json", "r"))
    for key in request.session.keys():
        context[key] = request.session[key]
    new_action = request.GET.dict()
    
    key_ids = [key for key in new_action.keys() if key != 'csrfmiddlewaretoken']
    
    if len(key_ids) == 0:
        # No new changes
        return context
    
    button_name = key_ids[0].split(".")[0].split(";")
    if button_name[0] == "unit":
        unit_type, unit_name = button_name[1].split("/")
        unit_type = unit_type.lower()
        unit_name = unit_name.lower()
        for i in range(1, 25):
            if context["slot" + str(i)] == "empty.jpg":
                context["slot" + str(i)] = os.path.join(unit_type, unit_name) + ".png"
                request.session["slot" + str(i)] = os.path.join(unit_type, unit_name) + ".png"
                break
    elif button_name[0] == "ChosenSlot":
        context["slot" + button_name[1]] = "empty.jpg"
        request.session["slot" + button_name[1]] = "empty.jpg"
    elif button_name[0] == "Button":
        color = button_name[1].lower()
        color_matching = json.load(open("templates/static/jsons/color_matching.json", "r"))
        context["maket_name"] = color_matching[color][0]
        request.session["maket_name"] = color_matching[color][0]
        tree_layout = json.load(open(f"templates/static/jsons/{color_matching[color][1]}", "r"))
        context["tree_layout"] = tree_layout["tree_layout"]
        request.session["tree_layout"] = tree_layout["tree_layout"]

    return context