import os


def get_latest_api_version():
    versions_path = os.path.join(os.path.dirname(__file__), "..")
    versions = [
        d
        for d in os.listdir(versions_path)
        if os.path.isdir(os.path.join(versions_path, d)) and d.startswith("v")
    ]
    return sorted(versions, reverse=True)[0] if versions else "v1"
