import tldextract
from bs4 import BeautifulSoup
from urllib.request import urlopen
from src.dto.res.seo_auditor_res_dto import SeoAuditorResponseDto


class AuditorService:
    url: str
    rules: list[str]

    def analysis(self) -> SeoAuditorResponseDto:
        res = SeoAuditorResponseDto(condition_passed=True, failed_condition=[])
        extracted = tldextract.extract(self.url)
        domain = extracted.domain
        with urlopen(self.url) as response:
            soup = BeautifulSoup(response, 'html.parser')
        # Check are there at least 5 internal links and 1 external links
        if "linking" in self.rules:
            links = soup.find_all("a")
            internal_links = 0
            external_links = 0
            for link in links:
                href = link['href']
                extracted_linkings = tldextract.extract(href)
                linking_domain = extracted_linkings.domain
                if domain in linking_domain:
                    internal_links += 1
                else:
                    external_links += 1
            if internal_links <= 5 or external_links <= 1:
                res.condition_passed = False
                res.failed_condition.append("linking")
        # Check if images got alt text
        if "img-alt-text" in self.rules:
            for div in soup.find_all('div', 'thumbnail'):
                no_alt_image = div.find('img', alt=False)
                if no_alt_image:
                    res.condition_passed = False
                    res.failed_condition.append("img-alt-text")
        return res


# Locally test service
if __name__ == '__main__':
    service = AuditorService(url="https://www.alibaba.com",
                             rules=["linking", "img-alt-text"])
    print(service.analysis().condition_passed)
