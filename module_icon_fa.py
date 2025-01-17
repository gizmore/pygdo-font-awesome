from gdo.base.GDO_Module import GDO_Module
from gdo.base.GDT import GDT
from gdo.core.GDT_Enum import GDT_Enum
from gdo.icon_fa.IconFA import IconFA
from gdo.ui.IconProvider import IconProvider


class module_icon_fa(GDO_Module):

    def __init__(self):
        super().__init__()
        self._license = 'Font Awesome Free License'

    def gdo_init(self):
        IconProvider.register(IconFA)

    def gdo_licenses(self) -> list[str]:
        return [
            'node_modules/@fortawesome/fontawesome-free/LICENSE.txt',
        ]

    def gdo_module_config(self) -> list[GDT]:
        return [
            GDT_Enum('fa_style').choices({'fa': 'Normal', 'fab': 'Bold', 'far': 'FAR?', 'fas': 'Solid'}).not_null().initial('fas')
        ]

    def cfg_fa_style(self) -> str:
        return self.get_config_val('fa_style')

    def gdo_load_scripts(self, page):
        self.add_bower_css("@fortawesome/fontawesome-free/css/all.css")

