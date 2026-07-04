from playwright.async_api import async_playwright
from bs4 import BeautifulSoup

async def search_web(query: str) -> str:
    """Searches the web for a given query and returns a summary of the results. 
    Use this tool when you need current information from the internet.
    
    Args:
        query: The search query string.
    """
    url = f"https://duckduckgo.com/html/?q={query}"
    
    async with async_playwright() as p:
        browser = await p.chromium.launch(headless=True)
        page = await browser.new_page()
        try:
            await page.goto(url, timeout=10000)
            content = await page.content()
            soup = BeautifulSoup(content, 'html.parser')
            
            results = []
            for a in soup.find_all('a', class_='result__snippet'):
                results.append(a.text.strip())
                
            if not results:
                return "No useful search results found."
                
            return "\n".join(results[:5])
        except Exception as e:
            return f"Failed to search web: {str(e)}"
        finally:
            await browser.close()

async def read_url_content(url: str) -> str:
    """Reads the text content of a specific URL. 
    Use this tool when you need to extract detailed information from a specific website.
    
    Args:
        url: The full URL to read.
    """
    async with async_playwright() as p:
        browser = await p.chromium.launch(headless=True)
        page = await browser.new_page()
        try:
            await page.goto(url, timeout=15000)
            content = await page.content()
            soup = BeautifulSoup(content, 'html.parser')
            
            # Remove scripts and styles
            for script in soup(["script", "style"]):
                script.extract()
                
            text = soup.get_text(separator=' ', strip=True)
            # truncate to avoid massive tokens
            return text[:10000] 
        except Exception as e:
            return f"Failed to read URL: {str(e)}"
        finally:
            await browser.close()
