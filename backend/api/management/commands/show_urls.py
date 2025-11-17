import json
import re

from django.core.management.base import BaseCommand
from django.urls import URLPattern, URLResolver, get_resolver


class Command(BaseCommand):
    help = "Show all URL patterns in the project"

    def add_arguments(self, parser):
        parser.add_argument("--json", action="store_true", help="Eksport do JSON")

    def normalize_path(self, path):
        path = re.sub(r"[\^\$]", "", path)
        path = re.sub(r"\(\?P<pk>[^)]+\)", "<id>", path)
        path = re.sub(r"\(\?P<format>[^)]+\)", "<format>", path)
        path = re.sub(r"\(\?P<path>[^)]+\)", "<path>", path)
        path = re.sub(r"\\.", ".", path)  # remove blackslash before dot
        path = re.sub(r"/+", "/", path)  # change double // to single /
        path = re.sub(r"\(\?P<app_label>[^)]+\)", "<app_label>", path)
        path = re.sub(r"\(\?P<url>[^)]+\)", "<url>", path)
        path = re.sub(r"<drf_format_suffix:format>", "", path)
        path = re.sub(r"\.<format>/?", "", path)
        return path

    def handle(self, *args, **options):
        resolver = get_resolver()
        urls = []

        def list_urls(patterns, prefix=""):
            for pattern in patterns:
                if isinstance(pattern, URLPattern):
                    normalized = self.normalize_path(str(pattern.pattern))
                    urls.append(
                        {
                            "path": prefix + normalized,
                            "name": pattern.name or "",
                            "view": f"{pattern.callback.__module__}.{pattern.callback.__name__}",
                        }
                    )
                elif isinstance(pattern, URLResolver):
                    list_urls(
                        pattern.url_patterns,
                        prefix + self.normalize_path(str(pattern.pattern)),
                    )

        list_urls(resolver.url_patterns)

        if options["json"]:
            print("Expporting URL patterns to JSON:")
            self.stdout.write(json.dumps(urls, indent=2))
        else:
            print(f"{self.style.SUCCESS('->All URL patterns in the project<-')}")
            for u in urls:
                self.stdout.write(
                    f"{'\033[94m'}{u['path']}{'\033[0m'} | name: {u['name']} | view: {u['view']}"
                )
