from pathlib import Path

def generate():
    out = Path("app/src/main/res/xml/theme_resources.xml")
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(
'''<?xml version="1.0" encoding="utf-8"?>
<resources>
</resources>
''',
        encoding="utf-8"
    )
    print("✅ theme_resources.xml")
