from utils.extract import scrape_main
from utils.transform import transform_data
from utils.load import save_to_csv, save_to_google_sheets
from utils.load import load_to_postgresql

def main():
    base_url = 'https://fashion-studio.dicoding.dev/'
    all_products = []

    # Halaman utama (tanpa /page)
    print(f"Scraping main page: {base_url}")
    try:
        products = scrape_main(base_url)
        all_products.extend(products)
    except Exception as e:
        print(f"❌ Failed to scrape main page: {e}")

    # Halaman 2 sampai 50
    for page in range(2, 51):
        url = f"{base_url}page{page}"
        print(f"Scraping page {page}: {url}")
        try:
            products = scrape_main(url)
            all_products.extend(products)
        except Exception as e:
            print(f"❌ Failed to scrape page {page}: {e}")

    transformed_data = transform_data(all_products)
    save_to_csv(transformed_data)
    load_to_postgresql(transformed_data)


    # Simpan ke Google Sheets
    save_to_google_sheets(
        transformed_data,
        '1mLOfJQLEqDFm6cNw8xbIRNORV5i_Ap4rrgo4wp_4O98',
        'Sheet1!A2'
    )


if __name__ == '__main__':
    main()
