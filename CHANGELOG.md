# Changelog

## [v1.1.0] - Added Product Search
- New `/products/search?keyword=` endpoint for searching products by keyword.
- Filters product list based on partial match.

## [v1.0.0] - Initial Release
- `/health` endpoint to check service status.
- `/products` endpoint to list all available products.

## [v2.0.0] - Enhanced Product Search
- Added query parameters: `min_price`, `max_price` to /products/search
- Error handling for invalid ranges and no match cases
