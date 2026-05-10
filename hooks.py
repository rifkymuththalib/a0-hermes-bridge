"""Plugin lifecycle hooks for install and uninstall."""

def install(config: dict) -> dict:
    print("[Hermes Bridge] Plugin installed successfully.")
    return {"status": "installed"}

def uninstall(config: dict) -> dict:
    print("[Hermes Bridge] Plugin uninstalled.")
    return {"status": "uninstalled"}
