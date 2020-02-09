class Http:
    def __init__(self, session):
        self.session = session

    async def download(self, url: str):
        async with self.session.get(url, timeout=10) as res:
            if res.status == 200:
                return await res.read()
            else:
                return None

    async def get_headers(self, url: str):
        async with self.session.head(url, timeout=10) as res:
            if res.status == 200:
                return res.headers
