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
    'resume': 'RESUME',
    'restart': 'RESTART',
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

# Mobile Controls section
SHOOT_BTN_LOC = (By.ID, 'shoot-btn')
ULT_BTN_LOC = (By.ID, 'ult-btn')
TRAP_BTN_LOC = (By.ID, 'trap-btn')
UP_ARROW_BTN_LOC = (By.ID, 'up-arrow-btn')
DOWN_ARROW_BTN_LOC = (By.ID, 'down-arrow-btn')
LEFT_ARROW_BTN_LOC = (By.ID, 'left-arrow-btn')
RIGHT_ARROW_BTN_LOC = (By.ID, 'right-arrow-btn')

# Game HUD section
SETTINGS_HUD_BTN_LOC = (By.ID, 'settings-btn')
PAUSE_MENU_DIV_LOC = (By.ID, 'pause-menu')
HEARTS_CONTAINER_LOC = (By.CLASS_NAME, 'hearts-container')
HEARTS_LOC = (By.TAG_NAME, 'img')
HP_INDICATOR_LOC = (By.ID, 'hp-indicator')
STATS_CONTAINER_LOC = (By.CLASS_NAME, 'stats')
LVL_STATS_LOC = (By.XPATH, "//p[contains(text(), 'LVL')]")
ATK_STATS_LOC = (By.XPATH, "//p[contains(text(), 'ATK')]")
DEF_STATS_LOC = (By.XPATH, "//p[contains(text(), 'DEF')]")
SPEED_STATS_LOC = (By.XPATH, "//p[contains(text(), 'SPEED')]")
EQUIPMENT_CONTAINER_LOC = (By.CLASS_NAME, 'equipment-container')
GOLD_INDICATOR_LOC = (By.ID, 'gold-indicator')
ULT_LABEL_LOC = (By.XPATH, "//p[contains(text(), 'ULT')]")
ULT_IMAGE_LOC = (By.ID, 'ultImage')
ULT_CHARGE_INDICATOR_LOC = (By.ID, 'ult-charge')
TRAPS_LABEL_LOC = (By.XPATH, "//p[contains(text(), 'Traps')]")
TRAPS_INDICATOR_LOC = (By.ID, 'traps-indicator')
KEYS_LABEL_LOC = (By.XPATH, "//p[contains(text(), 'Keys')]")
KEYS_INDICATOR_LOC = (By.ID, 'keys-indicator')
ENEMIES_LABEL_LOC = (By.XPATH, "//p[contains(text(), 'Enemies')]")
ENEMIES_INDICATOR_LOC = (By.ID, 'enemies-left')

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