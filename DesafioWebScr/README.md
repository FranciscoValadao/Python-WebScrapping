GOAL: WEBSCRAPPING WITH PYTHON

DESCRIPTION:

STEPS:
    1:OPEN THE LISTED URLs IN A AUTOMATED BROWSER
    2:SEARCH IN EACH PAGE SOURCE CODE IF THERES A KEYWORD FROM THE PARAMETER LIST
    3:ADD THE KEYWORDS FOUND IN A SPREADSHEET REFERENCING EACH KEYWORD TO ITS URL

REQUIREMENTS:
    SELENIUM (with chrome webdriver: save your version of the webdriver navigator in the ChromeDriver folder)
    BEAULTIFULSOUP
    PANDAS

INPUTS:
    URL LIST
    KEYWORDS

OUTPUT:
    EXCEL SPREADSHEET

EXAMPLE OF USAGE:
Any word that is listed at "Palavras_chave" column into the "parametros.xlsx" spreadsheet will be searched
in any page that is listed into the  Urls column at the same "parametros.xlsx" spreadsheet.

The result will be given in a new spreadsheet, wich will be generated instantly for every search, with the name
"DataScrOutput" and the time an date of the search. Ex.: DataScrOutput_08-02-2022_02-13.xlsx


#################################################################################################
Expected Spreadsheet Output Format:

              Keywords Found
<URL_1>       A, B, C, D
<URL_2>       C, D
<URL_3>       B, D

 Dictionary Representation:

 DATA = {<URL_1>: ['A', 'B', 'C', 'D'], <URL_2>: ['C', 'D'], <URL_3>: ['B', 'D']}
