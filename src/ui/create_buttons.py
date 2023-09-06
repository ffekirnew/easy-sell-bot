import telebot


def create_buttons(
    elements: list[str], width: int
) -> telebot.types.ReplyKeyboardMarkup:
    """
    Creates buttons with the given elements in the list with the given width
    and returns a markup.
    """
    markup = telebot.types.ReplyKeyboardMarkup(row_width=width)

    if 1 < width <= 3 < len(elements):
        while len(elements) % 3 != 0:
            elements.append("")

        if width == 2:
            for element in range(0, len(elements), 2):
                btn1 = telebot.types.KeyboardButton(elements[element])
                btn2 = telebot.types.KeyboardButton(elements[element + 1])
                markup.add(btn1, btn2)

        if width == 3:
            for element in range(0, len(elements), 3):
                btn1 = telebot.types.KeyboardButton(elements[element])
                btn2 = telebot.types.KeyboardButton(elements[element + 1])
                btn3 = telebot.types.KeyboardButton(elements[element + 2])
                markup.add(btn1, btn2, btn3)

    else:
        for element in elements:
            btn = telebot.types.KeyboardButton(element)
            markup.add(btn)

    return markup
