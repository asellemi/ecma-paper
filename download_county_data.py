
import requests

link = 'https://www2.census.gov/programs-surveys/saipe/datasets/{}/{}-state-and-county/est{}all.{}'

for year in range(1990, 2020):
    file_format = 'xls' if year > 2002 else 'dat'
    final_link = link.format(year, year, str(year)[2:4], file_format)
    r = requests.get(final_link, allow_redirects=True)
    open(f'est{year}all.{file_format}', 'wb').write(r.content)