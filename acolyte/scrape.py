import async_timeout
import urllib.parse
import aiohttp

async def download(loop, url, parameters={}):
    # A semi-generic download function, might need some tweaking later on
    async with aiohttp.ClientSession(loop=loop) as session:
        with async_timeout.timeout(10):
            async with session.get(url, params=parameters) as resp:
                return await resp.read()

async def latex_get(loop, equation):
    s = urllib.parse.quote_plus(equation)
    url = "https://chart.googleapis.com/chart?"
    parameters = {
        "cht":"tx", 
        "chl": equation,
        "chf": "bg,s,36393E",
        "chco": "EEEEEE"
    }
    return await download(loop, url, parameters)

