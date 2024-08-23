import scrapy
import re

import exporters


class HtmxSpider(scrapy.Spider):
    name = 'htmxspider'
    start_urls = ['https://htmx.org/examples/']

    custom_settings = {
        'FEED_EXPORTERS': {'markdown': exporters.MarkdownExporter},
        'FEED_FORMAT': 'markdown',
        'FEED_URI': 'htmx_examples.md',
        'FEED_EXPORT_ENCODING': 'utf-8',
        'FEEDS': {
            'htmx_examples.md': {
                'format': 'markdown',
                'overwrite': True
            }
        }
    }

    def parse(self, response, *args, **kwargs):
        for row in response.css('table tbody tr'):
            link = row.css('td:first-child a::attr(href)').get()
            if link:
                title = row.css('td:first-child a::text').get().strip()
                description = row.css('td:last-child::text').get().strip()
                yield scrapy.Request(response.urljoin(link), callback=self.parse_content_page, meta={'title': title, 'description': description})

    def parse_content_page(self, response):
        content = response.css('.content')

        # Use the title from the meta, fallback to h1 if not available
        title = response.meta.get('title') or content.css('h1::text').get()
        if title:
            title = title.strip()

        description = response.meta.get('description', '')

        # Extract all content up to the footer
        main_content = content.xpath(
            '*[not(self::footer) and not(contains(@class, "footer"))]').getall()
        main_content = ''.join(main_content)

        # Remove any remaining footer-like content
        main_content = re.sub(
            r'<div class="row".*?</div>\s*</div>\s*</div>', '', main_content, flags=re.DOTALL)

        yield {
            'url': response.url,
            'title': title,
            'description': description,
            'content': main_content.strip()
        }
