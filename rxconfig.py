import reflex as rx
import os

config = rx.Config(
    app_name="SKILLOGIC",
    api_url=os.environ.get("API_URL", "http://localhost:8000"),
    # TailwindV4 removed: project uses vanilla CSS per architecture spec.
    # SitemapPlugin: SEO best practices.
    # RadixThemesPlugin: explicit (suppresses deprecation warning from Radix components).
    plugins=[
        rx.plugins.SitemapPlugin(),
        rx.plugins.RadixThemesPlugin(),
    ],
)