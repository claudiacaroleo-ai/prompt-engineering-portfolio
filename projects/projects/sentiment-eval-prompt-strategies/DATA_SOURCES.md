# Data sources

## Primary source

I use the “Sephora Products and Skincare Reviews” dataset available on Kaggle, created by Nady Inky:
https://www.kaggle.com/datasets/nadyinky/sephora-products-and-skincare-reviews

According to the dataset description, the data was collected via a Python-based scraper in March 2023 and includes:
- detailed information about more than 8,000 beauty products sold on the Sephora online store (e.g. product and brand names, prices, ingredients, ratings, and product features)
- approximately 1 million user reviews across more than 2,000 skincare products, including review text, user attributes, and review ratings

## License

The dataset is released under the Creative Commons Attribution 4.0 International (CC BY 4.0) license.

## Scope of use

For this project, I work with a small, balanced subset of the dataset:
- 100 English-language reviews in total
- 50 positive reviews and 50 negative reviews, selected using rating-based thresholds

This limited sample is sufficient for controlled prompt evaluation while keeping the experiment lightweight, transparent, and reproducible.
