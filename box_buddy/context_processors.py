def site_vars(request):
    return {
        "site_title": "Box Buddy",
        "logo": "static/images/logo.png",
        "sidebar_data_links": [
            {"view_name": "box_list", "icon": "fa-cubes", "text": "Boxes"},
            {"view_name": "item_list", "icon": "fa-list", "text": "Items"},
        ],
        "sidebar_app_links": [
            {"view_name": "settings", "icon": "fa-gear", "text": "Settings"},
            {"view_name": "account_logout", "icon": "fa-sign-out", "text": "Logout"},
        ],
    }
