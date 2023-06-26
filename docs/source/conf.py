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

ogp_custom_meta_tags = [
    '<meta name="keywords" content="Dương Hữu Phúc, Duong Huu Phuc, Phuc H. Duong, Ton Duc Thang University" />',
    '<meta property="og:title" content="Homepage | Dương Hữu Phúc [Phuc H. Duong]" />',
    '<meta property="og:type" content="website" />',
    '<meta property="og:url" content="https://www.duonghuuphuc.com/" />',
    '<meta property="og:locale" content="en_VN" />',
    '<meta property="og:logo" content="https://www.duonghuuphuc.com/favicon.png" size="256x25" />',
    '<meta property="og:image" content="https://fastai.dev/static/img/fb-og-edx-docs-20230623.png" />',
    '<meta property="og:description" content="Phuc Duong is currently a lecturer and researcher at the Faculty of IT, TDTU (Vietnam), and at the R&D of NewAI Vietnam to research and develop AI solutions." />',
    '<meta property="fb:app_id" content="858663771713993" />'
]
