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


# -- html favicon
html_favicon = 'https://fastai.dev/favicon.png'

# -- Options for Open Graph

ogp_type = "article"
ogp_site_url = "https://edx-docs.fastai.dev/vi/latest/"
ogp_image = "https://fastai.dev/static/img/fb-og-edx-docs-20230623.png"
ogp_description_length = 300

ogp_custom_meta_tags = [
    '<meta name="keywords" content="Dương Hữu Phúc, Duong Huu Phuc, Phuc H. Duong, Ton Duc Thang University, Open edX, Tutor" />',
    '<meta property="og:locale" content="vi" />',
    '<meta property="og:description" content=" Đây là chuỗi bài viết về việc sử dụng Open edX làm nền tảng chính để minh họa cho hoạt động dạy-học trên nền tảng số. Trong phần thứ nhất của chuỗi bài, chúng tôi sẽ trình bày cách thức cài đặt và triển khai nền tảng Open edX. Tiếp theo đó, trong phần hai, chúng tôi sẽ trình bày cách khai thác hiệu quả nền tảng Open edX. Chúng tôi sẽ thể hiện đối tượng người đọc trong mỗi bài viết để người dùng dễ tiếp cận các nội dung bài viết, chẳng hạn, lập trình viên, người dạy, người học, người quản lý giáo dục." />',
    '<meta property="fb:app_id" content="858663771713993" />',
]
