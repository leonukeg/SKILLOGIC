import reflex as rx

config = rx.Config(
    app_name="SKILLOGIC",
    # TailwindV4 removed: project uses vanilla CSS per architecture spec.
    # SitemapPlugin: SEO best practices.
    # RadixThemesPlugin: explicit (suppresses deprecation warning from Radix components).
    plugins=[
        rx.plugins.SitemapPlugin(),
        rx.plugins.RadixThemesPlugin(theme=rx.theme(appearance="dark", accent_color="purple", radius="large")),
    ],
)