import pytest
from pathlib import Path


def html_files():
    repo = Path(__file__).resolve().parents[1]
    files = [f for f in repo.glob('*.html') if f.name != 'header.html']
    blog_index = repo / 'blog' / 'index.html'
    if blog_index.exists():
        files.append(blog_index)
    return files

@pytest.mark.parametrize('path', html_files())
def test_file_contains_html_tags(path):
    content = path.read_text(encoding='utf-8', errors='ignore').lower()
    assert '<html' in content and '</html>' in content, f"{path} missing html tags"
