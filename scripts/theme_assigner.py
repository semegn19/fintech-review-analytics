def assign_theme(text, theme_dict):

    text = str(text).lower()

    for theme, keywords in theme_dict.items():

        for kw in keywords:

            if kw in text:
                return theme

    return 'Other'