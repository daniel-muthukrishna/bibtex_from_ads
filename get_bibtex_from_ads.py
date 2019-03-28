import urllib.request
import re


def get_bibtex_from_ads_url(url, bibtag=None):
    """ Get bibtex entry from ads link. Return bibtex as text

    Parameters
    ----------
    url : str
        url of abstract on ADS. E.g.: http://adsabs.harvard.edu/abs/2019arXiv190302557M
    bibtag : str
        Optional Argument. If specified it replaces the name of the bibtex entry article with this name.
        If bibtag='default', then it uses the defualt bibtag given on the ADS.
        Otherwise, the bibtex entry is named AuthorYear[Firstword of title][Lastword of title]
    """

    _, _, domain, _, bibcode = url.split('/')
    bibtex_url = 'http://' + domain + '/cgi-bin/nph-bib_query?bibcode=' + bibcode + '&data_type-&data_type=BIBTEX&db_key=PRE&nocookieset=1'

    with urllib.request.urlopen(bibtex_url) as response:
       html = str(response.read())

    bibtex_entry = re.sub(r'.*@', '@', html)
    if not bibtag:
        author = bibtex_entry.split('author = {{')[1].split('}')[0]
        year = bibtex_entry.split('year = ')[1].split(',')[0]
        titlelist = bibtex_entry.split('title = "{')[1].split('}')[0].split()
        bibtag = author + year + titlelist[0] + titlelist[-1]

    if bibtag != 'default':
        bibtag_default = bibtex_entry.split('{')[1].split(',')[0]
        bibtex_entry = bibtex_entry.replace(bibtag_default, bibtag, 1)
    bibtex_entry = bibtex_entry.replace('\\n', '\n')
    bibtex_entry = bibtex_entry.replace('\\t', '')
    bibtex_entry = bibtex_entry.rstrip('\'')

    return bibtex_entry


def create_bib_file(urls, names=None):
    entries = []
    for i, url in enumerate(urls):
        if names:
            bibtex_entry = get_bibtex_from_ads_url(url, names[i])
        else:
            bibtex_entry = get_bibtex_from_ads_url(url)
        entries.append(bibtex_entry)

    with open('references.bib', 'w') as f:
        for bibtex_entry in entries:
            f.write(bibtex_entry)


if __name__ == '__main__':
    list_of_urls_and_names = [
        ('http://adsabs.harvard.edu/abs/2010A&A...523A...7G', 'SNIa_1'),
        ('http://adsabs.harvard.edu/abs/2013ApJ...764...48K', 'SNIa_2'),
        ('http://adsabs.harvard.edu/abs/2018PASP..130k4504P', 'SNIa_3'),

        ('http://adsabs.harvard.edu/abs/2017hsn..book..375J', 'SNIax_1'),

        ('http://adsabs.harvard.edu/abs/2010PASP..122.1415K', 'SNII_1'),
        ('http://adsabs.harvard.edu/abs/2018PASP..130k4504P', 'SNII_2'),
        ('http://adsabs.harvard.edu/abs/2018ApJS..236....6G', 'SNII_3'),
        ('http://adsabs.harvard.edu/abs/2017ApJ...849...70V', 'SNII_4'),

        ('http://adsabs.harvard.edu/abs/2010PASP..122.1415K', 'SNIbc_1'),
        ('http://adsabs.harvard.edu/abs/2018PASP..130k4504P', 'SNIbc_2'),
        ('http://adsabs.harvard.edu/abs/2018ApJS..236....6G', 'SNIbc_3'),
        ('http://adsabs.harvard.edu/abs/2017ApJ...849...70V', 'SNIbc_4'),

        ('http://adsabs.harvard.edu/abs/2018ApJS..236....6G', 'SLSN_1'),
        ('http://adsabs.harvard.edu/abs/2017ApJ...850...55N', 'SLSN_2'),
        ('http://adsabs.harvard.edu/abs/2009arXiv0911.0680K', 'SLSN_3'),

        ('http://adsabs.harvard.edu/abs/2018ApJS..236....6G', 'TDE_1'),
        ('http://adsabs.harvard.edu/abs/2018arXiv180108221M', 'TDE_2'),
        ('http://adsabs.harvard.edu/abs/1988Natur.333..523R', 'TDE_3'),

        ('http://adsabs.harvard.edu/abs/2017Natur.551...80K', 'KN_1'),

        ('http://adsabs.harvard.edu/abs/2010SPIE.7738E..1OC', 'AGN_1'),
        ('http://adsabs.harvard.edu/abs/2010ApJ...721.1014M', 'AGN_2'),

        ('http://adsabs.harvard.edu/abs/2010SPIE.7738E..1OC', 'RRL_1'),
        ('http://adsabs.harvard.edu/abs/2010ApJ...708..717S', 'RRL_2'),

        ('http://adsabs.harvard.edu/abs/2010SPIE.7738E..1OC', 'Mdwarfs_1'),
        ('http://adsabs.harvard.edu/abs/2011PhDT.......144H', 'Mdwarfs_2'),
        ('http://adsabs.harvard.edu/abs/2014ApJ...797..122D', 'Mdwarfs_3'),

        ('https://adsabs.harvard.edu/abs/2005ApJ...628..426P', 'EB_1'),
        ('https://adsabs.harvard.edu/abs/2016ApJS..227...29P', 'EB_2'),
        ('https://adsabs.harvard.edu/abs/2018ApJS..237...26H', 'EB_3'),

        ('http://adsabs.harvard.edu/abs/2011MNRAS.418..114I', 'Mira_1'),

        ('http://adsabs.harvard.edu/abs/1986ApJ...304....1P', 'microlens_single_pylima_1'),
        ('http://adsabs.harvard.edu/abs/2000ApJ...542..785G', 'microlens_single_pylima_2'),
        ('http://adsabs.harvard.edu/abs/2012RAA....12..947M', 'microlens_single_pylima_3'),

        ('https://adsabs.harvard.edu/abs/2000ApJ...541..587D', 'microslens_single_genlens_1'),
        ('https://adsabs.harvard.edu/abs/2012ApJS..201...21D', 'microslens_single_genlens_2'),

        ('https://adsabs.harvard.edu/abs/1997ApJ...488...55D', 'microlense_binary_1'),
        ('https://adsabs.harvard.edu/abs/2008ApJ...686..785N', 'microlense_binary_2'),

        ('http://adsabs.harvard.edu/abs/2018ApJS..236....6G', 'ILOT_1'),
        ('http://adsabs.harvard.edu/abs/2017ApJ...849...70V', 'ILOT_2'),

        ('http://adsabs.harvard.edu/abs/2018ApJS..236....6G', 'CART_1'),
        ('http://adsabs.harvard.edu/abs/2017ApJ...849...70V', 'CART_2'),
        ('http://adsabs.harvard.edu/abs/2012ApJ...755..161K', 'CART_3'),

        ('http://adsabs.harvard.edu/abs/2018ApJS..236....6G', 'PISN_1'),
        ('http://adsabs.harvard.edu/abs/2017ApJ...849...70V', 'PISN_2'),
        ('http://adsabs.harvard.edu/abs/2011ApJ...734..102K', 'PISN_3'),

        ('http://adsabs.harvard.edu/abs/2014PhRvD..89l4003B', 'microlens_string_1'),
        ('http://adsabs.harvard.edu/abs/2015IJMPD..2430010C', 'microlens_string_2'),
        ('http://adsabs.harvard.edu/abs/2018JCAP...05..002C', 'microlens_string_3'),

        ('http://adsabs.harvard.edu/abs/2018AJ....155....1G', 'photoz_1'),

        ('http://adsabs.harvard.edu/abs/2016SPIE.9910E..13D', 'obs_library_1'),
        ('http://adsabs.harvard.edu/abs/2016SPIE.9911E..25', 'obs_library_2')
        ]

    list_of_urls = [i[0] for i in list_of_urls_and_names]
    list_of_names = [i[1] for i in list_of_urls_and_names]

    create_bib_file(urls=list_of_urls, names=list_of_names)

