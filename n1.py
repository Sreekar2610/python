import requests
from bs4 import BeautifulSoup
import pandas as pd
import time

def scrape_flipkart_reviews(url, num_pages=1300):
    reviews_data = []
    
    for page_num in range(1, num_pages+1):
        page_url = f"{url}&page={page_num}"
        response = requests.get(page_url)
        
        if response.status_code == 200:
            soup = BeautifulSoup(response.content, 'html.parser')
            reviews = soup.find_all('div', {'class': '_27M-vq'})
            
            for review in reviews:
                rating = review.find('div', {'class': '_3LWZlK'}).text.strip()
                username = review.find('p', {'class': '_2sc7ZR _2V5EHH'}).text.strip()
                review_date = review.find('p', {'class': '_2mcZGG'}).text.strip()
                review_text = review.find('div', {'class': 't-ZTKy'}).text.strip()
                
                reviews_data.append({
                    'User': username,
                    'Date': review_date,
                    'Rating': rating,
                    'Review': review_text
                })

            # Add a delay to avoid overwhelming the server
            time.sleep(2)
        else:
            print(f"Failed to retrieve page {page_num}.")
    
    return reviews_data

# Example URL (without the page number)
url = 'https://www.flipkart.com/samsung-galaxy-s21-fe-5g-snapdragon-888-olive-256-gb/product-reviews/itmb3a0b1e650a0e?pid=MOBGSXD7TZZTJQXE&lid=LSTMOBGSXD7TZZTJQXESJMZ8F&sortOrder=MOST_HELPFUL&certifiedBuyer=false&aid=overall&page=1'

# Scrape reviews
reviews_data = scrape_flipkart_reviews(url, num_pages=1000)

# Convert data to DataFrame
df = pd.DataFrame(reviews_data)

# Save DataFrame to Excel
df.to_excel('samsung.xlsx', index=False)

print("Reviews saved to 'samsung.xlsx'")
