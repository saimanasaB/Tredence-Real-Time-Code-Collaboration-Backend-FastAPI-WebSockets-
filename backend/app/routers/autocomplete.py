from fastapi import APIRouter

router = APIRouter(prefix="/autocomplete", tags=["Autocomplete"])

@router.post("")
def autocomplete(data: dict):
    code = data.get("code", "")
    cursor = data.get("cursorPosition", 0)

    # Very simple mock AI response
    if "import" in code:
        suggestion = "import os\nimport sys"
    else:
        suggestion = "# suggestion: print('Hello World')"

    return {"suggestion": suggestion}
