import logging
import os
import random

from django.core.management.base import BaseCommand
from faker import Faker

from core.models import URL
from core.models import Box
from core.models import File
from core.models import Item
from users.models import User

logger = logging.getLogger(__name__)


class Command(BaseCommand):
    help = "Generate fake data for all models and link them together"

    def handle(self, *args, **kwargs):  # noqa: C901
        fake = Faker()

        user = User.objects.get(email=os.environ["DJANGO_SUPERUSER_EMAIL"])
        boxes = {
            "House": [
                {
                    "Kitchen Supplies": [
                        "Pots and Pans",
                        "Cutlery",
                        "Plates",
                        "Bowls",
                        "Measuring Cups",
                        "Mixing Bowls",
                        "Spatulas",
                        "Colander",
                        "Tupperware",
                        "Oven Mitts",
                    ]
                },
                {
                    "Living Room Decor": [
                        "Throw Pillows",
                        "Candles",
                        "Vases",
                        "Picture Frames",
                        "Blankets",
                        "Table Lamps",
                        "Rugs",
                        "Wall Art",
                        "Coasters",
                        "Curtains",
                    ]
                },
                {
                    "Bedroom Linens": [
                        "Bed Sheets",
                        "Pillowcases",
                        "Comforters",
                        "Blankets",
                        "Mattress Protectors",
                        "Duvet Covers",
                        "Throw Pillows",
                        "Bed Skirts",
                        "Quilts",
                        "Shams",
                    ]
                },
                {
                    "Bathroom Essentials": [
                        "Towels",
                        "Washcloths",
                        "Shower Curtain",
                        "Bath Mat",
                        "Soap Dispenser",
                        "Toothbrush Holder",
                        "Toilet Brush",
                        "Plunger",
                        "Shampoo",
                        "Conditioner",
                    ]
                },
                {
                    "Pantry Goods": [
                        "Canned Beans",
                        "Pasta",
                        "Rice",
                        "Cereal",
                        "Flour",
                        "Sugar",
                        "Cooking Oil",
                        "Spices",
                        "Snacks",
                        "Soup Cans",
                    ]
                },
                {
                    "Toys": [
                        "Action Figures",
                        "Dolls",
                        "Building Blocks",
                        "Board Games",
                        "Puzzles",
                        "Toy Cars",
                        "Stuffed Animals",
                        "Play-Doh",
                        "Yo-Yos",
                        "Jump Ropes",
                    ]
                },
                {
                    "Books": [
                        "Novels",
                        "Cookbooks",
                        "Children's Books",
                        "Comics",
                        "Magazines",
                        "Biographies",
                        "Travel Guides",
                        "Dictionaries",
                        "Encyclopedias",
                        "Journals",
                    ]
                },
                {
                    "Seasonal Decorations": [
                        "Christmas Lights",
                        "Halloween Pumpkins",
                        "Easter Eggs",
                        "Wreaths",
                        "Garlands",
                        "Ornaments",
                        "Table Centerpieces",
                        "Window Clings",
                        "Flags",
                        "Candles",
                    ]
                },
                {
                    "Cleaning Supplies": [
                        "All-Purpose Cleaner",
                        "Sponges",
                        "Scrub Brushes",
                        "Mop",
                        "Broom",
                        "Dustpan",
                        "Glass Cleaner",
                        "Paper Towels",
                        "Disinfectant Wipes",
                        "Rubber Gloves",
                    ]
                },
                {
                    "Shoes": [
                        "Sneakers",
                        "Sandals",
                        "Boots",
                        "Dress Shoes",
                        "Slippers",
                        "Flip Flops",
                        "Running Shoes",
                        "Heels",
                        "Loafers",
                        "Rain Boots",
                    ]
                },
            ],
            "Shed": [
                {
                    "Garden Tools": [
                        "Shovel",
                        "Rake",
                        "Hoe",
                        "Trowel",
                        "Pruners",
                        "Loppers",
                        "Wheelbarrow",
                        "Garden Fork",
                        "Hand Cultivator",
                        "Garden Gloves",
                    ]
                },
                {
                    "Fertilizers": [
                        "Compost",
                        "Bone Meal",
                        "Blood Meal",
                        "Fish Emulsion",
                        "Lawn Fertilizer",
                        "Rose Food",
                        "Vegetable Fertilizer",
                        "Pellet Fertilizer",
                        "Liquid Fertilizer",
                        "Slow Release Fertilizer",
                    ]
                },
                {
                    "Seeds": [
                        "Tomato Seeds",
                        "Carrot Seeds",
                        "Lettuce Seeds",
                        "Sunflower Seeds",
                        "Pumpkin Seeds",
                        "Pea Seeds",
                        "Bean Seeds",
                        "Radish Seeds",
                        "Cucumber Seeds",
                        "Pepper Seeds",
                    ]
                },
                {
                    "Outdoor Lights": [
                        "String Lights",
                        "Solar Path Lights",
                        "Lanterns",
                        "Flood Lights",
                        "Spotlights",
                        "Motion Sensor Lights",
                        "Wall Sconces",
                        "Deck Lights",
                        "Step Lights",
                        "Garden Torches",
                    ]
                },
                {
                    "Pots and Planters": [
                        "Clay Pots",
                        "Plastic Pots",
                        "Hanging Baskets",
                        "Window Boxes",
                        "Raised Beds",
                        "Self-Watering Pots",
                        "Ceramic Planters",
                        "Metal Buckets",
                        "Wooden Crates",
                        "Grow Bags",
                    ]
                },
                {
                    "Hoses": [
                        "Garden Hose",
                        "Soaker Hose",
                        "Expandable Hose",
                        "Hose Reel",
                        "Spray Nozzle",
                        "Hose Splitter",
                        "Hose Repair Kit",
                        "Hose Guide",
                        "Hose Hanger",
                        "Drip Hose",
                    ]
                },
                {
                    "Lawn Equipment": [
                        "Lawn Mower",
                        "Edger",
                        "Weed Whacker",
                        "Leaf Blower",
                        "Aerator",
                        "Grass Seed Spreader",
                        "Lawn Roller",
                        "Sprinkler",
                        "Hedge Trimmer",
                        "Lawn Rake",
                    ]
                },
                {
                    "Paint Supplies": [
                        "Paint Brushes",
                        "Paint Rollers",
                        "Drop Cloths",
                        "Painter's Tape",
                        "Paint Trays",
                        "Paint Stir Sticks",
                        "Sandpaper",
                        "Putty Knife",
                        "Paint Scraper",
                        "Paint Can Opener",
                    ]
                },
                {
                    "Extension Cords": [
                        "Outdoor Extension Cord",
                        "Indoor Extension Cord",
                        "Power Strip",
                        "Cord Reel",
                        "Surge Protector",
                        "Heavy Duty Cord",
                        "Light Duty Cord",
                        "Multi-Outlet Adapter",
                        "Cord Cover",
                        "Cord Organizer",
                    ]
                },
                {
                    "Work Gloves": [
                        "Leather Gloves",
                        "Rubber Gloves",
                        "Cotton Gloves",
                        "Cut Resistant Gloves",
                        "Gardening Gloves",
                        "Welding Gloves",
                        "Winter Gloves",
                        "Disposable Gloves",
                        "Mechanic Gloves",
                        "Grip Gloves",
                    ]
                },
            ],
            "Garage": [
                {
                    "Car Care": [
                        "Car Wax",
                        "Car Wash Soap",
                        "Microfiber Towels",
                        "Tire Cleaner",
                        "Glass Cleaner",
                        "Air Freshener",
                        "Wheel Brush",
                        "Polish",
                        "Chamois",
                        "Detailing Spray",
                    ]
                },
                {
                    "Power Tools": [
                        "Drill",
                        "Circular Saw",
                        "Jigsaw",
                        "Angle Grinder",
                        "Impact Driver",
                        "Rotary Tool",
                        "Sander",
                        "Heat Gun",
                        "Reciprocating Saw",
                        "Cordless Screwdriver",
                    ]
                },
                {
                    "Hand Tools": [
                        "Hammer",
                        "Screwdriver Set",
                        "Pliers",
                        "Wrench Set",
                        "Tape Measure",
                        "Utility Knife",
                        "Level",
                        "Allen Wrenches",
                        "Handsaw",
                        "Chisel Set",
                    ]
                },
                {
                    "Sports Equipment": [
                        "Basketball",
                        "Soccer Ball",
                        "Tennis Racket",
                        "Baseball Glove",
                        "Football",
                        "Golf Clubs",
                        "Baseball Bat",
                        "Hockey Stick",
                        "Volleyball",
                        "Jump Rope",
                    ]
                },
                {
                    "Camping Gear": [
                        "Tent",
                        "Sleeping Bag",
                        "Camping Stove",
                        "Lantern",
                        "Camping Chair",
                        "Cooler",
                        "Backpack",
                        "First Aid Kit",
                        "Water Bottle",
                        "Camping Table",
                    ]
                },
                {
                    "Bicycles": [
                        "Mountain Bike",
                        "Road Bike",
                        "Bike Helmet",
                        "Bike Pump",
                        "Bike Lock",
                        "Bike Lights",
                        "Bike Bell",
                        "Bike Tools",
                        "Spare Tube",
                        "Water Bottle Cage",
                    ]
                },
                {
                    "Hardware": [
                        "Nails",
                        "Screws",
                        "Bolts",
                        "Washers",
                        "Anchors",
                        "Hooks",
                        "Brackets",
                        "Picture Hangers",
                        "Wall Plugs",
                        "Wire",
                    ]
                },
                {
                    "Spare Parts": [
                        "Spare Tire",
                        "Oil Filter",
                        "Air Filter",
                        "Spark Plugs",
                        "Brake Pads",
                        "Windshield Wipers",
                        "Fuses",
                        "Light Bulbs",
                        "Belts",
                        "Hoses",
                    ]
                },
                {
                    "Winter Gear": [
                        "Snow Shovel",
                        "Ice Scraper",
                        "Snow Boots",
                        "Winter Gloves",
                        "Sled",
                        "Snow Brush",
                        "Heated Blanket",
                        "Hand Warmers",
                        "Snow Chains",
                        "Winter Hat",
                    ]
                },
                {
                    "Coolers": [
                        "Large Cooler",
                        "Small Cooler",
                        "Ice Packs",
                        "Cooler Wheels",
                        "Cooler Divider",
                        "Cooler Basket",
                        "Cooler Drain Plug",
                        "Cooler Seat",
                        "Soft Cooler",
                        "Electric Cooler",
                    ]
                },
            ],
            "Basement": [
                {
                    "Holiday Decorations": [
                        "Christmas Tree",
                        "Halloween Costumes",
                        "Easter Basket",
                        "String Lights",
                        "Ornaments",
                        "Wreaths",
                        "Tablecloths",
                        "Candles",
                        "Pumpkin Decor",
                        "Gift Wrap",
                    ]
                },
                {
                    "Old Clothes": [
                        "Winter Coats",
                        "Sweaters",
                        "Jeans",
                        "T-Shirts",
                        "Scarves",
                        "Hats",
                        "Gloves",
                        "Shoes",
                        "Dresses",
                        "Jackets",
                    ]
                },
                {
                    "Photo Albums": [
                        "Family Album",
                        "Vacation Album",
                        "Wedding Album",
                        "Baby Album",
                        "Graduation Album",
                        "Travel Album",
                        "Holiday Album",
                        "Birthday Album",
                        "Anniversary Album",
                        "Pet Album",
                    ]
                },
                {
                    "Heirlooms": [
                        "China Set",
                        "Silverware",
                        "Jewelry Box",
                        "Old Letters",
                        "Antique Clock",
                        "Porcelain Figurines",
                        "Quilt",
                        "Pocket Watch",
                        "Crystal Vase",
                        "Photo Frame",
                    ]
                },
                {
                    "Board Games": [
                        "Monopoly",
                        "Scrabble",
                        "Chess",
                        "Checkers",
                        "Risk",
                        "Clue",
                        "Candy Land",
                        "Life",
                        "Uno",
                        "Jenga",
                    ]
                },
                {
                    "Suitcases": [
                        "Large Suitcase",
                        "Carry-On",
                        "Duffel Bag",
                        "Garment Bag",
                        "Backpack",
                        "Rolling Suitcase",
                        "Travel Tote",
                        "Kids Suitcase",
                        "Laptop Bag",
                        "Packing Cubes",
                    ]
                },
                {
                    "Electronics": [
                        "Old Laptop",
                        "VCR",
                        "DVD Player",
                        "Game Console",
                        "Speakers",
                        "Remote Controls",
                        "Cables",
                        "Chargers",
                        "Headphones",
                        "Camera",
                    ]
                },
                {
                    "Craft Supplies": [
                        "Yarn",
                        "Knitting Needles",
                        "Paints",
                        "Brushes",
                        "Glue Gun",
                        "Scissors",
                        "Paper",
                        "Markers",
                        "Beads",
                        "Fabric",
                    ]
                },
                {
                    "Extra Furniture": [
                        "Folding Chair",
                        "Card Table",
                        "Bookshelf",
                        "Lamp",
                        "Ottoman",
                        "Side Table",
                        "Desk",
                        "Stool",
                        "Bed Frame",
                        "Dresser",
                    ]
                },
                {
                    "Old Toys": [
                        "Stuffed Bear",
                        "Toy Train",
                        "Dollhouse",
                        "Action Figure",
                        "Puzzle",
                        "Toy Car",
                        "Building Blocks",
                        "Yo-Yo",
                        "Marbles",
                        "Slinky",
                    ]
                },
            ],
            "Office": [
                {
                    "Stationery": [
                        "Pens",
                        "Pencils",
                        "Notepads",
                        "Sticky Notes",
                        "Paper Clips",
                        "Stapler",
                        "Envelopes",
                        "Folders",
                        "Highlighters",
                        "Binder Clips",
                    ]
                },
                {
                    "Printer Supplies": [
                        "Printer Paper",
                        "Ink Cartridges",
                        "Toner",
                        "Photo Paper",
                        "USB Cable",
                        "Drum Unit",
                        "Maintenance Kit",
                        "Print Head",
                        "Label Sheets",
                        "Cleaning Sheets",
                    ]
                },
                {
                    "Cables": [
                        "HDMI Cable",
                        "USB Cable",
                        "Ethernet Cable",
                        "Power Cord",
                        "VGA Cable",
                        "Audio Cable",
                        "Extension Cord",
                        "Lightning Cable",
                        "Micro USB Cable",
                        "DisplayPort Cable",
                    ]
                },
                {
                    "Archived Files": [
                        "Tax Returns",
                        "Receipts",
                        "Contracts",
                        "Invoices",
                        "Bank Statements",
                        "Insurance Papers",
                        "Medical Records",
                        "Wills",
                        "Leases",
                        "Employment Records",
                    ]
                },
                {
                    "Books": [
                        "Reference Book",
                        "Manual",
                        "Textbook",
                        "Novel",
                        "Biography",
                        "Encyclopedia",
                        "Dictionary",
                        "Guidebook",
                        "Workbook",
                        "Magazine",
                    ]
                },
                {
                    "Office Decor": [
                        "Desk Plant",
                        "Picture Frame",
                        "Desk Organizer",
                        "Wall Art",
                        "Clock",
                        "Lamp",
                        "Mouse Pad",
                        "Coasters",
                        "Calendar",
                        "Bookend",
                    ]
                },
                {
                    "Tech Gadgets": [
                        "Tablet",
                        "Smartphone",
                        "Smartwatch",
                        "Bluetooth Speaker",
                        "Webcam",
                        "USB Hub",
                        "External Hard Drive",
                        "Flash Drive",
                        "Wireless Mouse",
                        "Wireless Keyboard",
                    ]
                },
                {
                    "Reference Materials": [
                        "Style Guide",
                        "User Manual",
                        "Product Catalog",
                        "White Paper",
                        "Research Paper",
                        "Brochure",
                        "Pamphlet",
                        "Instruction Sheet",
                        "Blueprint",
                        "Specification Sheet",
                    ]
                },
                {
                    "Notebooks": [
                        "Spiral Notebook",
                        "Composition Book",
                        "Graph Paper Notebook",
                        "Journal",
                        "Sketchbook",
                        "Legal Pad",
                        "Pocket Notebook",
                        "Lab Notebook",
                        "Travel Journal",
                        "Bullet Journal",
                    ]
                },
                {
                    "Chargers": [
                        "Phone Charger",
                        "Laptop Charger",
                        "Tablet Charger",
                        "USB Charger",
                        "Wireless Charger",
                        "Car Charger",
                        "Power Bank",
                        "Charging Dock",
                        "Smartwatch Charger",
                        "Camera Charger",
                    ]
                },
            ],
        }
        for parent_name, children in boxes.items():
            parent_box, _ = Box.objects.get_or_create(
                name=parent_name,
                defaults={
                    "description": fake.text(max_nb_chars=200),
                    "is_active": True,
                    "is_deleted": False,
                    "created_by": user,
                },
            )
            for child in children:
                for child_name, items in child.items():
                    child_box, _ = Box.objects.get_or_create(
                        name=child_name,
                        parent=parent_box,
                        defaults={
                            "description": fake.text(max_nb_chars=200),
                            "is_active": True,
                            "is_deleted": False,
                            "created_by": user,
                        },
                    )
                    for item_name in items:
                        Item.objects.get_or_create(
                            name=item_name,
                            box=child_box,
                            defaults={
                                "description": fake.text(max_nb_chars=100),
                                "is_active": True,
                                "is_deleted": False,
                                "created_by": user,
                                "quantity": random.randint(1, 10),  # noqa: S311
                            },
                        )
                    # create box under child box
                    for x in range(1, 4):
                        Box.objects.get_or_create(
                            name=f"{child_name} Box {x}",
                            parent=child_box,
                            defaults={
                                "description": fake.text(max_nb_chars=200),
                                "is_active": True,
                                "is_deleted": False,
                                "created_by": user,
                            },
                        )

            # create 3 items for each parent box
            for x in range(1, 4):
                Item.objects.get_or_create(
                    name=f"{parent_name} Item {x}",
                    box=parent_box,
                    defaults={
                        "description": fake.text(max_nb_chars=100),
                        "is_active": True,
                        "is_deleted": False,
                        "created_by": user,
                        "quantity": random.randint(1, 10),  # noqa: S311
                    },
                )
        # Create files for each box
        # Create files for each item
        items = Item.objects.all()
        for item in items:
            for _ in range(random.randint(1, 3)):  # noqa: S311
                File.objects.create(
                    name=f"{item.name} File {fake.uuid4()}",
                    item=item,
                    file=fake.file_name(category="text"),
                    is_active=True,
                    is_deleted=False,
                    created_by=user,
                )
        # Create URLs for each item
        items = Item.objects.all()
        for item in items:
            for _ in range(random.randint(1, 3)):  # noqa: S311
                URL.objects.create(
                    name=f"{item.name} URL {fake.uuid4()}",
                    item=item,
                    url=fake.url(),
                    is_active=True,
                    is_deleted=False,
                    created_by=user,
                )
        logger.info("Fake data generated successfully.")
        self.stdout.write(self.style.SUCCESS("Fake data generated successfully."))
        logger.info("You can now view the generated data in the admin panel.")
        self.stdout.write(self.style.SUCCESS("You can now view the generated data in the admin panel."))
        logger.info("Use the Django admin interface to explore the generated data.")
        self.stdout.write(self.style.SUCCESS("Use the Django admin interface to explore the generated data."))
