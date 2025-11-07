import os
import re


def get_latest_api_version():
    versions_path = os.path.join(os.path.dirname(__file__), "..", "versions")
    versions = [
        d
        for d in os.listdir(versions_path)
        if os.path.isdir(os.path.join(versions_path, d)) and d.startswith("v")
    ]
    if not versions:
        return "v1"

    versions.sort(key=lambda v: int(re.search(r"\d+", v).group()), reverse=True)
    return versions[0]
