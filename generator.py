import asyncio
from pyppeteer import launch
import sys
import os
from datetime import date
from bs4 import BeautifulSoup

today = date.today()
_date = today.strftime("%d/%m/%Y") # dd/mm/YYYY

def modify_html(verseObj):
    file = os.path.join(os.getcwd(),'design','index.html')
    html = open(file,'r',encoding='utf-8')
    soup = BeautifulSoup(html.read(),features='lxml')

    soup.find(id='date').string = _date

    soup.find(id='eV').string = verseObj['text'][0]
    soup.find(id='hV').string = verseObj['text'][1]
    soup.find(id='tV').string = verseObj['text'][2]

    soup.find(id='eR').string = verseObj['book'][0]
    soup.find(id='hR').string = verseObj['book'][1]
    soup.find(id='tR').string = verseObj['book'][2]

    soup.find(id='nums').string = str(verseObj['chapter']) + ' : ' + str(verseObj['verse'])
    html.close()

    html = open(file,'w',encoding='utf-8')
    html.write(soup.prettify())
    html.close()


def convert_to_image(verseObj):

    _HTML = os.path.join(os.getcwd(),'design','index.html')
    file_name = ((verseObj['book'][0]).replace(' ','')) + str(verseObj['chapter']) + '_' + str(verseObj['verse'])
    _OUTFILE = os.path.join(os.getcwd(),'output',file_name+'.png')
    sourcepath = 'file://' + _HTML

    async def generate_png():
        browser = await launch()
        page = await browser.newPage()
        await page.goto(sourcepath)
        await page.evaluateHandle('document.fonts.ready')
        await page.setViewport({ 'width': 1000, 'height': 1000 })
        await page.screenshot({'path': _OUTFILE, 'fullPage': True})
        await browser.close()


    asyncio.get_event_loop().run_until_complete(generate_png())


