# Book Information Aggregator

A Python application that extracts and aggregates bibliographic information from multiple online sources, providing comprehensive book metadata from Amazon and Google Books API.

## Overview

This project automates the process of gathering book information by scraping data from Amazon's product pages and querying the Google Books API. The system then intelligently aggregates this information to create complete book records with standardized data fields.

### Key Features

- **Multi-source data extraction**: Retrieves book information from both Amazon.fr and Google Books API
- **Intelligent data aggregation**: Merges information from different sources while handling conflicts and duplicates
- **Fuzzy matching**: Uses string similarity algorithms to identify equivalent data across sources
- **Comprehensive metadata**: Captures detailed bibliographic information including physical characteristics
- **ISBN support**: Handles both ISBN-10 and ISBN-13 formats

## Project Structure

- `main_fonction.py`: Main entry point for the application
- `scrapping_fonction.py`: Amazon web scraping functionality
- `Google_books.py`: Google Books API integration
- `aggregation.py`: Data aggregation and conflict resolution logic
- `amazon_extraction.py`: Specialized Amazon data extraction
- `fiche_test.py`: Test data and examples
- `versionfinale_1.py`: Final version implementation

## Installation

### Prerequisites

- Python 3.7 or higher
- Internet connection for web scraping and API access

### Required Libraries

```bash
pip install beautifulsoup4 pandas urllib3 fuzzywuzzy datetime
```

## Usage

### Basic Usage

Run the main application:

```bash
python main_fonction.py
```

Enter an ISBN when prompted (either 10 or 13 digits). The application will:

1. Extract data from Amazon
2. Query Google Books API
3. Aggregate the information
4. Display the complete book record

### Example

```
Donner le code ISBN: 9782211124485
```

The system will return a comprehensive dictionary containing all available book information.

## Data Structure

The application standardizes book information into the following data structure:

| Field Name | Description | Data Type |
|------------|-------------|-----------|
| isbn10 | ISBN-10 identifier | string |
| isbn13 | ISBN-13 identifier | string |
| titre | Main title | string |
| sousTitre | Subtitle | string |
| auteurs | List of authors | list |
| fonctions | Author roles/functions | list |
| editeur | Publisher | string |
| date | Publication date | string |
| image | Local image path | string |
| genre | Book genre/category | string |
| nbPages | Number of pages | integer |
| poids | Weight in grams | float |
| prix | Price in euros | float |
| format | Physical dimensions | string |
| collection | Collection name | string |
| numeroCollection | Collection number | integer |
| serie | Series name | string |
| numeroSerie | Series number | integer |
| reliure | Binding type (hardcover/paperback) | string |
| consultation | Data retrieval date | string |
| creation | Record creation date | string |

## Data Sources

### Amazon
- Product pages on amazon.fr
- Extracts pricing, physical characteristics, and publication details
- Handles both direct ISBN lookups and search results

### Google Books API
- Official Google Books API v1
- Provides bibliographic metadata and publication information
- Reliable source for ISBNs, titles, authors, and publishers

## Aggregation Logic

The system uses intelligent aggregation rules to merge data from multiple sources:

- **Conflict resolution**: Prioritizes more complete or accurate information
- **Fuzzy matching**: Identifies similar strings that may represent the same data
- **Data validation**: Ensures consistency across different field types
- **Deduplication**: Removes redundant information while preserving unique details

## Testing

Test the application with these verified ISBNs:

| Title | ISBN-10 | ISBN-13 |
|-------|---------|---------|
| L'Odyssée | 2211124485 | 978-2-211-12448-5 |
| L'Écume des jours | 2756021638 | 978-2-7560-2163-8 |

## Error Handling

The application includes error handling for:
- Network connectivity issues
- Invalid ISBN formats
- Missing or incomplete data from sources
- Rate limiting and timeout scenarios

## Contributing

When contributing to this project, please ensure that:
- New features maintain compatibility with existing data structures
- Web scraping respects robots.txt and rate limiting guidelines
- API usage follows Google Books terms of service
- Code includes appropriate error handling and logging

## License

This project is intended for educational and research purposes. Users are responsible for complying with the terms of service of data sources and applicable copyright laws.
