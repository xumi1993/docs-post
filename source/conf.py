# Configuration file for the Sphinx documentation builder.
#
# This file only contains a selection of the most common options. For a full
# list see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Path setup --------------------------------------------------------------

# If extensions (or modules to document with autodoc) are in another directory,
# add these directories to sys.path here. If the directory is relative to the
# documentation root, use os.path.abspath to make it absolute, like shown here.
#
# import os
# import sys
# sys.path.insert(0, os.path.abspath('.'))


# -- Project information -----------------------------------------------------

project = 'Oh My Memo'
copyright = '2022, Mijian Xu'
author = 'Mijian Xu'
github_user = "xumi1993"
github_repo = "docs-post"
github_url = "docs.xumijian.me"

# -- General configuration ---------------------------------------------------

# Add any Sphinx extension module names here, as strings. They can be
# extensions coming with Sphinx (named 'sphinx.ext.*') or your custom
# ones.
extensions = ['sphinx.ext.githubpages',
              "sphinx.ext.intersphinx",
              "sphinx_cjkspace.cjkspace",
              "sphinx_copybutton",
              "sphinx_design",
              "myst_nb",
              "sphinx.ext.mathjax",
              "sphinx.ext.todo",
              "sphinx.ext.viewcode",
]

# Add any paths that contain templates here, relative to this directory.
templates_path = ['_templates']

# The language for content autogenerated by Sphinx. Refer to documentation
# for a list of supported languages.
#
# This is also used if you do content translation via gettext catalogs.
# Usually you set "language" from the command line for these cases.
language = 'zh_CN'

# List of patterns, relative to source directory, that match files and
# directories to ignore when looking for source files.
# This pattern also affects html_static_path and html_extra_path.
exclude_patterns = []

myst_enable_extensions = [
    "colon_fence",
    "deflist",
]

# -- Options for HTML output -------------------------------------------------

# The theme to use for HTML and HTML Help pages.  See the documentation for
# a list of builtin themes.
#
html_theme = 'furo'
html_theme_options = {
    "sidebar_hide_name": False,
}

# Add any paths that contain custom static files (such as style sheets) here,
# relative to this directory. They are copied after the builtin static files,
# so a file named "default.css" will overwrite the builtin "default.css".
html_static_path = ['_static']

# options for sphinx-copybutton
# https://sphinx-copybutton.readthedocs.io
copybutton_prompt_text = r">>> |\.\.\. |\$ |In \[\d*\]: | {2,5}\.\.\.: | {5,8}: "
copybutton_prompt_is_regexp = True
copybutton_only_copy_prompt_lines = True
copybutton_remove_prompts = True

# options for myst-nb
jupyter_execute_notebooks = "cache"

html_extra_path = []
html_last_updated_fmt = "%Y 年 %m 月 %d 日"
html_title = project
html_css_files = ["custom.css"]


html_context = {
    "favicon": "favicon.ico",
    "display_github": True,
    "github_user": github_user,
    "github_repo": github_repo,
    "github_version": "main",
    "conf_py_path": "/source/",
    "theme_vcs_pageview_mode": "blob",
    "menu_links": [
        (   '<i class="fa fa-home"></i> 个人主页',
            "https://xumijian.me/",
        ),
        (
            '<i class="fa fa-github fa-fw"></i> 网站源码',
            github_url,
        ),
        (
            '<i class="fa fa-edit fa-fw"></i> 个人博客',
            "https://blog.xumijian.me/",
        ),
        (
            '<i class="fa fa-comments fa-fw"></i> 参与讨论',
            f"{github_url}/discussions",
        ),
    ],
}