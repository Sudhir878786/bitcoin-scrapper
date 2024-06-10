# api/coinmarketcap.py
import requests
import pandas as pd
import logging

logger = logging.getLogger(__name__)

class CoinMarketCap:
    BASE_URL = "https://pro-api.coinmarketcap.com/v1/cryptocurrency/quotes/latest"
    API_KEY = "b6fb2074-22c7-4064-af51-9e078da45ffc"  # Replace with your actual API key

    @staticmethod
    def get_coin_data(coin):
        try:
            headers = {
                'Accepts': 'application/json',
                'X-CMC_PRO_API_KEY': CoinMarketCap.API_KEY,
            }
            parameters = {
                'symbol': coin,
                'convert': 'USD'
            }
            response = requests.get(CoinMarketCap.BASE_URL, headers=headers, params=parameters)
            data = response.json()
            
            if response.status_code != 200:
                logger.error(f"Failed to fetch data for {coin}, status code: {response.status_code}")
                logger.error(f"Error message: {data.get('status', {}).get('error_message', 'No error message')}")
                return None
            
            coin_data = data['data'][coin]
            usd_data = coin_data['quote']['USD']

            result = {
                "name": coin_data["name"],
                "symbol": coin_data["symbol"],
                "price": usd_data["price"],
                "price_change": usd_data["percent_change_24h"],
                "market_cap": usd_data["market_cap"],
                "market_cap_rank": coin_data["cmc_rank"],
                "volume": usd_data["volume_24h"],
                "volume_change": usd_data["volume_change_24h"],
                "circulating_supply": coin_data["circulating_supply"],
                "total_supply": coin_data["total_supply"],
                "diluted_market_cap": usd_data.get("fully_diluted_market_cap"),
                "contracts": coin_data.get("platform", {}).get("token_address"),
                "official_links": ", ".join(coin_data.get("urls", {}).get("website", [])),
                "social_twitter": ", ".join(coin_data.get("urls", {}).get("twitter", [])),
                "social_telegram": ", ".join(coin_data.get("urls", {}).get("telegram", []))
            }
            return result

        except Exception as e:
            logger.error(f"Error in get_coin_data for {coin}: {str(e)}")
            return None