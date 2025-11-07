import json
from django.core.management.base import BaseCommand
from django.urls import get_resolver, URLPattern, URLResolver


class Command(BaseCommand):
    help = "Show all URL patterns in the project"

    def add_arguments(self, parser):
        parser.add_argument("--json", action="store_true", help="Eksport do JSON")

    def handle(self, *args, **options):
        resolver = get_resolver()
        urls = []

        def list_urls(patterns, prefix=""):
            for pattern in patterns:
                if isinstance(pattern, URLPattern):
                    urls.append(
                        {
                            "path": prefix + str(pattern.pattern),
                            "name": pattern.name or "",
                            "view": f"{pattern.callback.__module__}.{pattern.callback.__name__}",
                        }
                    )
                elif isinstance(pattern, URLResolver):
                    list_urls(pattern.url_patterns, prefix + str(pattern.pattern))

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
