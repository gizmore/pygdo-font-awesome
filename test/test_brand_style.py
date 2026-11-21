import unittest
from unittest.mock import patch

from gdo.base.Render import Mode
from gdo.icon_fa.IconFA import IconFA


class BrandStyleTest(unittest.TestCase):
    def test_brand_icons_use_brand_font(self):
        with patch('gdo.icon_fa.IconFA.t', return_value='icon'):
            for icon in ('youtube', 'whatsapp'):
                with self.subTest(icon=icon):
                    self.assertIn(f'fab fa-{icon}', IconFA.display_icon_html(icon, Mode.render_html))

    def test_other_icons_use_configured_style(self):
        with patch('gdo.icon_fa.IconFA.t', return_value='icon'), \
             patch('gdo.icon_fa.IconFA.module_config_var', return_value='fas') as config:
            self.assertIn('fas fa-user', IconFA.display_icon_html('user', Mode.render_html))
            config.assert_called_once_with('icon_fa', 'fa_style')
