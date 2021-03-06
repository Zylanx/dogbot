# http://jesselegg.com/archives/2009/09/5/simple-word-wrap-algorithm-pythons-pil/
def draw_word_wrap(draw,
                   font,
                   text,
                   xpos=0,
                   ypos=0,
                   max_width=130,
                   fill=(0, 0, 0)):
    """
    Draws text that automatically word wraps.

    Parameters
    ----------
    draw : PIL.ImageDraw.Draw
        The `ImageDraw.Draw` instance to draw with.
    font : PIL.ImageFont
    text
        The font to draw with.
    xpos : int
        The X position to start at.
    ypos : int
        The Y position to start at.
    max_width : int
        The maximum width allotted to draw text at before wrapping.
    fill : Tuple[int, int, int]
        The fill color.
    """
    text_size_x, text_size_y = draw.textsize(text, font=font)
    remaining = max_width
    space_width, space_height = draw.textsize(' ', font=font)
    output_text = []
    for word in text.split(None):
        word_width, word_height = draw.textsize(word, font=font)
        if word_width + space_width > remaining:
            output_text.append(word)
            remaining = max_width - word_width
        else:
            if not output_text:
                output_text.append(word)
            else:
                output = output_text.pop()
                output += ' %s' % word
                output_text.append(output)
            remaining = remaining - (word_width + space_width)
    for text in output_text:
        draw.text((xpos, ypos), text, font=font, fill=fill)
        ypos += text_size_y
