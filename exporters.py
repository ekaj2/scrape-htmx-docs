from scrapy.exporters import BaseItemExporter
import re


class MarkdownExporter(BaseItemExporter):
    def __init__(self, file, **kwargs):
        super().__init__(**kwargs)
        self.file = file

    def export_item(self, item):
        self.file.write(f"# {item['title']}\n\n".encode('utf-8'))
        self.file.write(f"URL: {item['url']}\n\n".encode('utf-8'))

        content = item['content']
        # Convert only specific HTML elements to Markdown
        content = re.sub(r'<h3.*?>(.*?)</h3>', r'### \1', content)
        content = re.sub(r'<p>(.*?)</p>', r'\1\n\n', content, flags=re.DOTALL)
        content = re.sub(r'<ul.*?>(.*?)</ul>',
                         self.format_list, content, flags=re.DOTALL)

        self.file.write(f"{content}\n\n".encode('utf-8'))
        self.file.write("---\n\n".encode('utf-8'))

    def format_list(self, match):
        list_content = match.group(1)
        list_items = re.findall(r'<li.*?>(.*?)</li>', list_content, re.DOTALL)
        return '\n'.join(f"- {item.strip()}" for item in list_items) + '\n\n'
