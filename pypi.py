from quick_pypi.deploy import *

auto_deploy(
    cwd=os.path.dirname(os.path.realpath(__file__)),
    name="social-content",
    long_name="Social Content Analysis",
    description="Social Content Analysis",
    long_description="A toolkit to parse and analyze contents from social media like Weibo and Twitter ",
    src_root="src",
    dists_root=f"dists",
    pypi_token='../pypi_upload_token.txt',
    test=False,
    version="0.0.1a0",
    project_url="http://github.com/dhchenx/social-content",
    author_name="Donghua Chen",
    author_email="douglaschan@126.com",
    requires="jieba;ner-kit", # use ; for multiple requires
    license='MIT',
    license_filename='LICENSE',
    keywords="social network, social content, text analysis, weibo, twitter",
    github_username="dhchenx",
    readme_path="README.md",
   # console_scripts=""
)

