from selenium.webdriver.common.by import By

# buttons
BTN_TEXT_LOCATORS = {
    'play': 'PLAY',
    'cherem_pedia': 'CHEREM-PEDIA',
    'settings': 'SETTINGS',
    'credits': 'CREDITS',
    'exit': 'EXIT',
    'back': 'BACK',
    'apply': 'APPLY',
    'controls': 'CONTROLS',
    'bestiary': 'BESTIARY',
    'items': 'ITEMS',
    'main_game': 'MAIN GAME',
    'survival': 'SURVIVAL',
    'ng+': 'NG+',
    'yes': 'YES',
    'no': 'NO',
    'high_scores': 'HIGH SCORES',
    'continue': 'CONTINUE',
    'submit_high_score': 'SUBMIT HIGH SCORE',
    'continue_no_submit': 'CONTINUE WITHOUT SUBMITTING',
}

# Title Screen
PRESS_ENTER_BTN_LOC = (By.ID, 'title-start-btn')

# Main Menu
VERSION_INDICATOR_LOC = (By.CLASS_NAME, 'version')

# Patch Notes section
PATCH_NOTES_DIV_LOC = (By.CLASS_NAME, 'patchnotes')
PATCH_NOTES_HEADER_LOC = (By.ID, 'patchnotes-header')
PATCH_NOTES_TEXT_LOC = (By.ID, 'patchnotes-text')
PATCH_NOTES_VERSIONS_LOC = (By.CLASS_NAME, 'patchnotes-versions')
PATCH_NOTES_VERSIONS_INDICATORS_LOC = (By.TAG_NAME, 'li')

# Credits section
CREDITS_DIV_LOC = (By.CLASS_NAME, 'credits')
CREDITS_PARAGRAPHS_LOC = (By.TAG_NAME, 'p')

# Settings section
SETTINGS_DIV_LOC = (By.CLASS_NAME, 'settings')
SETTINGS_FIELDS_GENERIC_LOC = (By.XPATH, ".//input[@type='checkbox']")

# Play section
NAVIGATION_WRAPPER_LOC = (By.CLASS_NAME, 'navigation-wrapper')

# Game section
GAME_CANVAS_LOC = (By.XPATH, "//canvas[contains(@style, 'image-rendering: pixelated;')]")

# Bestiary + Items pedia section
RECORDS_CARD_LOC = (By.CLASS_NAME, 'records-card')
RECORDS_IMAGES_GENERIC_LOC = (By.TAG_NAME, 'img')
PEDIA_CARD_LOC = (By.CLASS_NAME, 'pedia-card')
PEDIA_RECORD_NAME_DIV_LOC = (By.CLASS_NAME, 'pedia-record-name')
PEDIA_RECORD_NAME_TEXT_LOC = (By.TAG_NAME, 'p')
PEDIA_STAT_LOC = (By.CLASS_NAME, 'pedia-stat')
NG_BUTTON_TOGGLED_LOC = (By.CLASS_NAME, 'ng-toggled')

# Intro section
INTRO_DIV_LOC = (By.CLASS_NAME, 'intro')

# High Scores section
LOADING_LOC = (By.ID, 'loading')
NO_CONNECTION_P_LOC = (By.ID, 'no-connection')
NO_HIGHSCORES_P_LOC = (By.ID, 'no-highscores-yet')
HIGHSCORES_TABLE = (By.CLASS_NAME, 'highscores-table')
HIGHSCORES_TABLE_HEADERS_LOC = (By.TAG_NAME, 'th')
HIGHSCORES_TABLE_DATA_LOC = (By.TAG_NAME, 'td')

# End Game screen section
END_GAME_STATS_DIV_LOC = (By.CLASS_NAME, 'game-finish-stats')
END_GAME_STATS_LOC = (By.TAG_NAME, 'p')

# High Score submit form
NAME_INPUT_LOC = (By.ID, 'name-input')
NAME_WARNING_LOC = (By.ID, 'profanity-error')
SUBMISSION_RESULT_MSG_LOC = (By.ID, 'form-submit-result')