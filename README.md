### Key Dependencies

The notebook utilizes the following Python libraries:

*   **pandas**: For data manipulation and analysis.
    
*   **matplotlib.pyplot**: For creating visualizations.
    
*   **re**: A built-in module for working with regular expressions to handle text patterns.
    
*   **ast**: A built-in module for parsing Python syntax.
    
*   **sqlalchemy** and **pymysql**: Used for database connectivity, though their functionality is not fully demonstrated beyond installation.
    
*   **likesucksbutthisdoesnt (ls)**: A custom library used for exporting and opening the cleaned DataFrame.
    

### Initial Data Cleaning

*   **Column Standardization**: The notebook starts by standardizing column names by converting them to title case to ensure consistency.
    
*   **Case Normalization**: It normalizes the text data in the One-Line column to title case.
    
*   **Duplicate Removal**: The script focuses on removing duplicate entries. It first removes duplicates based on the combination of Movies, Year, and Rating columns. A subsequent, more aggressive step removes additional duplicates by keeping only the first entry for each unique movie title.
    

### Handling Missing and Inconsistent Data

*   **Year Column**: The Year column contains inconsistent formats like (2021– ) and -2021. The notebook handles this by:
    
    *   Creating a New column to extract four-digit years using a regular expression.
        
    *   Defining a custom function clean\_year to parse release year ranges and split them into separate start and end year columns.
        
*   **Rating Column**: Missing rating values (NaN) are filled with the mean rating of the entire dataset. All rating values are then rounded to one decimal place for a cleaner, more consistent format.
    
*   **Runtime Column**: Missing Runtime values are imputed with the mean runtime, grouped by the type of content (e.g., Movie, Series). This approach is more accurate than using the overall average. The notebook also cleans the runtime values to ensure they are stored as a single integer representing minutes, removing any text or decimals.
    

### Data Transformation and Classification

*   **Content Type Classification**: A new Type column is created to classify each entry. The script initially checks the Stars column for the word **"director"** to classify an entry as a **'Movie'**. If this keyword is not found, the entry is classified as a **'Series'**. The classification is further refined by checking the Genre column for keywords like 'short', 'animation', 'documentary', and 'tv-show' to assign more specific types like **'Short-movie'**, **'Animation'**, or **'Documentary'**.
