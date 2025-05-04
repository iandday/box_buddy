def site_vars(request):
    return {
        "site_title": "Box Buddy",
        "sidebar_view_links": [
            {"view_name": "location_list", "icon": "fa-compass", "text": "Locations"},
            {"view_name": "box_list", "icon": "fa-boxes-stacked", "text": "Boxes"},
        ],
    }
