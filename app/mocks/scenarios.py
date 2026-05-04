from app.models.schemas import Entity

# Mock scenarios matched by keywords in the user message.
# Geometry uses WKT format with lat/lon (WGS84) coordinates.
# Coordinate order: latitude longitude (e.g. POINT (32.0853 34.7818))

SCENARIOS = [
    {
        "keywords": ["איפה", "מיקום"],
        "response": (
            "מטרה X נמצאת בנקודה:\n"
            "**נ.צ:** 32.0853, 34.7818\n\n"
            "**סטטוס:** פעיל\n"
            "**סוג:** מטרה קרקעית"
        ),
        "entities": [
            Entity(
                layer="targets",
                entity_id="target-001",
                geometry="POINT (32.0853 34.7818)",
            )
        ],
    },
    {
        "keywords": ["קרוב", "קרובים", "ליד"],
        "response": (
            "כוחות לפי קרבה למטרה X:\n\n"
            "1. **כוח א** — מרחק 300 מטר\n"
            "2. **כוח ב** — מרחק 450 מטר\n"
            "3. **כוח ג** — מרחק 700 מטר"
        ),
        "entities": [
            Entity(
                layer="forces",
                entity_id="force-001",
                geometry="POINT (32.0880 34.7830)",
            ),
            Entity(
                layer="forces",
                entity_id="force-002",
                geometry="POINT (32.0865 34.7800)",
            ),
            Entity(
                layer="forces",
                entity_id="force-003",
                geometry="POINT (32.0820 34.7850)",
            ),
        ],
    },
    {
        "keywords": ["רשימה", "כוחות", "גזרה"],
        "response": (
            "כוחות בגזרה:\n\n"
            "- **כוח א** — 32.0880, 34.7830\n"
            "- **כוח ב** — 32.0865, 34.7800\n"
            "- **כוח ג** — 32.0820, 34.7850"
        ),
        "entities": [
            Entity(
                layer="forces",
                entity_id="force-001",
                geometry="POINT (32.0880 34.7830)",
            ),
            Entity(
                layer="forces",
                entity_id="force-002",
                geometry="POINT (32.0865 34.7800)",
            ),
            Entity(
                layer="forces",
                entity_id="force-003",
                geometry="POINT (32.0820 34.7850)",
            ),
        ],
    },
    {
        "keywords": ["סטטוס", "מצב"],
        "response": (
            "**סטטוס מטרה X:** פעיל\n\n"
            "**זמן עדכון אחרון:** 10:32\n"
            "**הערות:** ללא שינוי חריג"
        ),
        "entities": [
            Entity(
                layer="targets",
                entity_id="target-001",
                geometry="POINT (32.0853 34.7818)",
            )
        ],
    },
    {
        "keywords": ["מנחת", "נחיתה"],
        "response": (
            "**המנחת המומלץ:** מנחת אלפא — מרחק 1.2 ק״מ\n\n"
            "**התאמה:**\n"
            "- פעילות: יום ולילה\n"
            "- סטטוס: פעיל\n"
            "- סוג כלי: מסוקים\n\n"
            "**חלופות:**\n"
            "- מנחת בראבו — 2.5 ק״מ (יום בלבד)"
        ),
        "entities": [
            Entity(
                layer="landing-pads",
                entity_id="pad-alpha",
                geometry="POINT (32.0910 34.7750)",
            ),
            Entity(
                layer="landing-pads",
                entity_id="pad-bravo",
                geometry="POINT (32.0950 34.7700)",
            ),
        ],
    },
    {
        "keywords": ["אזור", "פוליגון", "גבול"],
        "response": "האזור המבוקש מסומן על גבי המפה.",
        "entities": [
            Entity(
                layer="areas",
                entity_id="area-001",
                geometry=(
                    "POLYGON ("
                    "(32.0800 34.7700, "
                    "32.0900 34.7700, "
                    "32.0900 34.7850, "
                    "32.0800 34.7850, "
                    "32.0800 34.7700)"
                    ")"
                ),
            )
        ],
    },
    {
        "keywords": ["מסלול", "דרך", "קו"],
        "response": "המסלול המבוקש מסומן על גבי המפה.",
        "entities": [
            Entity(
                layer="routes",
                entity_id="route-001",
                geometry=(
                    "LINESTRING "
                    "(32.0800 34.7700, "
                    "32.0850 34.7750, "
                    "32.0900 34.7820)"
                ),
            )
        ],
    },
]

DEFAULT_SCENARIO = {
    "response": "This is a mock response.",
    "needs_clarification": False,
    "entities": [
        Entity(
            layer="mock-layer",
            entity_id="mock-entity-1",
            geometry="POINT (32.0853 34.7818)",
        )
    ],
}


def match_scenario(message: str) -> dict:
    for scenario in SCENARIOS:
        if any(keyword in message for keyword in scenario["keywords"]):
            return scenario
    return DEFAULT_SCENARIO
