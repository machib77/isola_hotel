from django.contrib.sitemaps import Sitemap


class StaticSitemap(Sitemap):
    def items(self):
        # Define the list of URLs you want to include in the sitemap
        return [
            "/",
            "/contacto/",
            "/habitaciones/",
            "/habitaciones/de_lujo/",
            "/habitaciones/grupal/",
            "/habitaciones/triple/",
            "/habitaciones/doble/",
            "/habitaciones/simple/",
            "/gastronomia/",
            "/experiencias/",
            "/imagenes/",
            "/videos/",
        ]  # Add more URLs as needed

    def location(self, item):
        # Return the URL for each item
        return item

    def changefreq(self, item):
        # You can set the change frequency for each URL (optional)
        return "monthly"

    def priority(self, item):
        # You can set the priority for each URL (optional)
        return 0.5
