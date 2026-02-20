import os

from gdo.base.Application import Application
from gdo.base.ModuleLoader import ModuleLoader
from gdo.base.Util import Files
from gdo.icon_fa import module_icon_fa
from gdo.icon_fa.IconFA import IconFA
from gdo.ui.IconUTF8 import IconUTF8
from gdotest.TestUtil import GDOTestCase, install_module


class FontAwesomeTestCase(GDOTestCase):

    async def asyncSetUp(self):
        await super().asyncSetUp()
        Application.init(os.path.dirname(__file__ + "/../../../../"))
        loader = ModuleLoader.instance()
        loader.load_modules_db(True)
        install_module('icon_fa')
        loader.init_modules(True, True)
        Application.init_cli()
        loader.init_cli()

    async def test_01_all_covered(self):
        miss = []
        for key, ico in IconUTF8.MAP().items():
            if not IconFA.MAP().get(key):
                miss.append(key)
        self.assertEqual(0, len(miss), f"FA Icons missing: {miss}")

    async def test_02_all_valid(self):
        miss = []
        all_js_path = module_icon_fa.instance().file_path('node_modules/@fortawesome/fontawesome-free/js/all.js')
        all_js = Files.get_contents(all_js_path)
        for key in IconFA.MAP().values():
            search = f'"{key}"'
            if search not in all_js:
                miss.append(key)
        self.assertEqual(0, len(miss), f"FA Icons not existing: {miss}")

    async def test_03_non_extra(self):
        miss = []
        for key in IconFA.MAP().keys():
            if key not in IconUTF8.MAP().keys():
                miss.append(key)
        self.assertEqual(0, len(miss), f"FA Icons not known to GDO: {miss}")
