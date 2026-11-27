"""Build the Pages artifact from an explicit public file list."""
from pathlib import Path
import hashlib
import html
import shutil
from markdown_it import MarkdownIt

ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / '_site'
PROTOTYPE = Path('axyourbody-prototype/20261126-정정훈-AXYOURBODY프로토타입.html')
DOCUMENTS = [Path('worksheet.md')] + sorted(
    p.relative_to(ROOT) for p in (ROOT / 'axyourbody-prototype').rglob('*.md')
)
DOCUMENT_SET = set(DOCUMENTS)
STYLE = '''body{margin:0;background:#f5f4ef;color:#26332b;font:17px/1.8 system-ui,sans-serif}
main{max-width:900px;margin:auto;padding:48px 24px 100px}a{color:#216447;text-underline-offset:3px}
h1,h2,h3{line-height:1.4}h1{font-size:clamp(28px,5vw,40px)}h2{margin-top:48px;font-size:24px}
table{border-collapse:collapse;width:100%;font-size:15px}th,td{padding:12px;border:1px solid #cbd1c8;text-align:left;vertical-align:top}
.table-wrap{overflow-x:auto}pre{padding:16px;background:#e8ece5;overflow-x:auto}code{overflow-wrap:anywhere}
blockquote{margin:24px 0;border-left:3px solid #6f8d77;padding:8px 20px}a:focus-visible{outline:3px solid #208457;outline-offset:4px}
nav{display:flex;gap:24px;flex-wrap:wrap}p,li{overflow-wrap:anywhere}'''


def render(markdown, title, prefix='', source=Path('README.md')):
    import posixpath
    from urllib.parse import urlsplit, urlunsplit, unquote
    parser = MarkdownIt('commonmark', {'html': False}).enable('table')
    tokens = parser.parse(markdown)
    for block in tokens:
        for token in block.children or []:
            if token.type != 'link_open':
                continue
            href = token.attrGet('href')
            url = urlsplit(href)
            if url.scheme or url.netloc or not url.path:
                continue
            path = Path(posixpath.normpath(str(source.parent / unquote(url.path))))
            if path in DOCUMENT_SET:
                token.attrSet('href', urlunsplit(('', '', url.path[:-3] + '.html', url.query, url.fragment)))
            elif path == Path('README.md'):
                token.attrSet('href', prefix + 'process.html')
    content = parser.renderer.render(tokens, parser.options, {})
    content = content.replace('<table>', '<div class="table-wrap"><table>').replace('</table>', '</table></div>')
    return ('<!doctype html><html lang="ko"><meta charset="utf-8">'
            '<meta name="viewport" content="width=device-width, initial-scale=1">'
            f'<title>{html.escape(title)}</title><style>{STYLE}</style><main>'
            f'<nav><a href="{prefix}index.html">프로토타입 체험</a>'
            f'<a href="{prefix}process.html">작업 과정</a>'
            f'<a href="{prefix}tasks/index.html">과업 소개</a>'
            f'<a href="{prefix}README.md">README 원문</a></nav>'
            f'{content}</main></html>')


if __name__ == '__main__':
    if OUT.exists():
        shutil.rmtree(OUT)
    OUT.mkdir()
    shutil.copyfile(ROOT / PROTOTYPE, OUT / 'index.html')
    # Keep the README's direct prototype link valid as well.
    (OUT / PROTOTYPE).parent.mkdir(parents=True, exist_ok=True)
    shutil.copyfile(ROOT / PROTOTYPE, OUT / PROTOTYPE)
    shutil.copytree(ROOT / 'tasks', OUT / 'tasks')
    # GitHub Pages caches static assets. Change their URLs with their content.
    asset_versions = {
        name: hashlib.sha256((OUT / 'tasks' / name).read_bytes()).hexdigest()[:12]
        for name in ('style.css',)
    }
    for page in (OUT / 'tasks').glob('*.html'):
        content = page.read_text()
        for name, version in asset_versions.items():
            content = content.replace(f'"{name}"', f'"{name}?v={version}"')
        page.write_text(content)
    readme = (ROOT / 'README.md').read_text()
    (OUT / 'README.md').write_text(readme)
    (OUT / 'process.html').write_text(render(readme, 'AX YOUR BODY · 스킬과 에이전트 작업 과정'))
    for name in DOCUMENTS:
        source = ROOT / name
        target = (OUT / name).with_suffix('.html')
        target.parent.mkdir(parents=True, exist_ok=True)
        # Render referenced documents at their linked paths for public reading.
        prefix = '../' * (len(Path(name).parts) - 1)
        target.write_text(render(source.read_text(), source.stem, prefix, name))
    (OUT / '.nojekyll').touch()
    digest = hashlib.sha256((OUT / 'index.html').read_bytes()).hexdigest()
    assert (ROOT / PROTOTYPE).read_bytes() == (OUT / 'index.html').read_bytes()
    print(f'Pages artifact: {OUT}; index SHA-256: {digest}')
