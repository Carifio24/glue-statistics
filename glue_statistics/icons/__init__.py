from os.path import abspath, dirname, join

def icon_path(filename):
    return abspath(join(dirname(__file__), filename))

REFRESH_LOGO = icon_path('glue_refresh.png')
NOTATION_LOGO = icon_path('glue_scientific_notation.png')
EXPORT_LOGO = icon_path('glue_export.png')
CALCULATE_LOGO = icon_path('glue_calculate.png')
SORT_LOGO = icon_path('glue_sort.png')
SETTINGS_LOGO = icon_path('glue_settings.png')
INSTRUCTIONS_LOGO = icon_path('glue_instructions.png')

HOME_LOGO = icon_path('glue_home.png')
SAVE_LOGO = icon_path('glue_filesave.png')
EXPAND_LOGO = icon_path('glue_expand.png')
COLLAPSE_LOGO = icon_path('glue_collapse.png')
CUSTOM_COLUMN_LOGO = icon_path('glue_addcolumn.png')
