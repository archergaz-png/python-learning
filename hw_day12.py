from pathlib import Path
import re

from reportlab.lib.pagesizes import A4
from reportlab.lib.units import cm
from reportlab.platypus import SimpleDocTemplate

from build_pdf import add_page_number, make_styles, md_to_flowables

root = Path(__file__).resolve().parent
source = (root / 'homework_day12.md').read_text(encoding='utf-8')
source = re.sub(r'\[([^\]]+)\]\((https?://[^)]+)\)', r'\1 (\2)', source)
output = root / 'output/pdf/homework_day12.pdf'
output.parent.mkdir(parents=True, exist_ok=True)
mock = type('DocumentContext', (), {'_toc_entries': []})()
story = md_to_flowables(source, make_styles(), mock)
doc = SimpleDocTemplate(str(output), pagesize=A4, leftMargin=2*cm, rightMargin=2*cm, topMargin=2*cm, bottomMargin=2*cm, title='Практическое задание после дня 12')
doc.build(story, onFirstPage=add_page_number, onLaterPages=add_page_number)
print(output)