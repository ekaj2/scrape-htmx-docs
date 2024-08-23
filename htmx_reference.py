import scrapy
import re
import exporters


class HtmxSpider(scrapy.Spider):
    name = 'htmxspider'
    start_urls = ['https://htmx.org/reference/']

    custom_settings = {
        'FEED_EXPORTERS': {'markdown': exporters.MarkdownExporter},
        'FEED_FORMAT': 'markdown',
        'FEED_URI': 'htmx_reference.md',
        'FEED_EXPORT_ENCODING': 'utf-8',
        'FEEDS': {
            'htmx_reference.md': {
                'format': 'markdown',
                'overwrite': True
            }
        }
    }

    def parse(self, response, *args, **kwargs):
        for info_table in response.css('.info-table'):
            for row in info_table.css('tbody tr'):
                attribute_cell = row.css('td:first-child')
                link = attribute_cell.css('a::attr(href)').get()
                if link:
                    title = attribute_cell.xpath('string(.)').get().strip()
                    yield scrapy.Request(response.urljoin(link), callback=self.parse_content_page, meta={'title': title})

    def parse_content_page(self, response):
        content = response.css('.content')

        # Use the title from the link, fallback to h1 if not available
        title = response.meta.get('title') or content.css('h1::text').get()
        if title:
            title = title.strip()

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
            'content': main_content.strip()
        }
