# Configuration file for the Sphinx documentation builder.

# -- Project information

project = 'FastAI'
copyright = '2023, FastAI contributors'
author = 'FastAI contributors'

release = '0.1'
version = '0.1.0'

# -- General configuration

extensions = [
    'sphinx.ext.duration',
    'sphinx.ext.doctest',
    'sphinx.ext.autodoc',
    'sphinx.ext.autosummary',
    'sphinx.ext.intersphinx',
    'sphinxext.opengraph'
]

intersphinx_mapping = {
    'python': ('https://docs.python.org/3/', None),
    'sphinx': ('https://www.sphinx-doc.org/en/master/', None),
}
intersphinx_disabled_domains = ['std']

templates_path = ['_templates']

# -- Options for HTML output

html_theme = 'sphinx_rtd_theme'

# -- Options for EPUB output
epub_show_urls = 'footnote'


# -- Options for Open Graph

ogp_site_url = "https://edx-docs.fastai.dev/vi/latest/"
ogp_image = "https://fastai.dev/static/img/fb-og-edx-docs-20230623.png"
ogp_description_length = 300
ogp_type = "article"
ogp_enable_meta_description = False

ogp_custom_meta_tags = [
    '<meta name="keywords" content="Dương Hữu Phúc, Duong Huu Phuc, Phuc H. Duong, Ton Duc Thang University, Open edX, Tutor" />',
    '<meta property="og:locale" content="vi" />',
    '<meta property="fb:app_id" content="858663771713993" />',
    '<meta property="og:description" content="This is series of articles that utilize Open edX as the primary platform to illustrate digital learning activities. Each article will cater to specific reader profiles, such as programmers, educators, learners, and education administrators, to ensure easy access to the content." />',
]
