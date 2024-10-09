from os import getenv
from asyncio import sleep, get_event_loop
from pyppeteer import launch
from dotenv import load_dotenv

load_dotenv()

url = r"META-AP01.cloudmetadados.com.br"
user = r"3911_06"
login = r"cloudmetadados\3911_06"
password = 'Bauer2024'

async def launch_browser(download_path):
    browser = await launch(
        headless=False,
        executablePath=getenv('CHROME_PATH'),
        defaultViewport=None
    )
    page = await browser.newPage()
    await set_download_behavior(page, download_path)

    return browser, page

async def set_download_behavior(page, download_path):
    client = await page.target.createCDPSession()
    await client.send('Page.setDownloadBehavior', {
        'behavior': 'allow',
        'downloadPath': download_path
    })

async def fill_login_form(page, username, password):
    await page.waitForSelector('#DomainUserName')
    await page.waitForSelector('#UserPass')
    await page.waitForSelector('#btnSignIn')

    await page.type('#DomainUserName', username)
    await page.type('#UserPass', password)
    await page.click('#btnSignIn')

async def perform_js_click(page):
    js_code = '''
    const rh = document.getElementsByClassName("tswa_boss");
    const onMouseUpFunc = rh[3].getAttribute('onmouseup');
    rh[4].setAttribute('onclick', onMouseUpFunc);
    rh[4].click();
    '''
    await page.evaluate(js_code)

async def download_program():
    download_path = getenv('DOWNLOAD_PATH')

    browser, page = await launch_browser(download_path)

    await page.goto("https://saas.cloudmetadados.com.br/RDWeb/Pages/pt-BR/default.aspx")

    await fill_login_form(page, login, password)

    await sleep(0.5)

    await perform_js_click(page)

    await sleep(1)

    await browser.close()
    return True;

get_event_loop().run_until_complete(download_program())
