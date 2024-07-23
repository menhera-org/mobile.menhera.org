# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information

import os
import sys
import datetime

project = 'Menhera Mobile SIM'
html_title = project

year = datetime.datetime.now().year

copyright = f'{year} 一般社団法人生活情報基盤研究機構 中核プロジェクト推進ユニット'
author = '一般社団法人生活情報基盤研究機構 中核プロジェクト推進ユニット'

html_short_title = "Menhera Mobile"

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration


html_theme_options = {
    "banner_text": (
        "Menhera Mobile SIM は組織内で試験運用しているもので，現在他人の通信の用に供しているものではありません。"
    ),
    "banner_hiding": "temporary",
    "show_theme_credit": False,
    "source_url": "https://github.com/menhera-org/mobile.menhera.org",
    "dark_mode_code_blocks": True
}

extensions = [
]

templates_path = ['_templates']
exclude_patterns = []

language = 'ja'

# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

html_theme = 'piccolo_theme'
html_static_path = ['_static']

