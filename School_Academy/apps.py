from django.apps import AppConfig


class SchoolAcademyConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'School_Academy'

    def ready(self):
        import School_Academy.signals