"""
This module provides a class `EText` for rendering enhanced text with various styles and configurations.
It supports features such as bold, italic, underlined, strike-through text, custom colors, and custom sizes.
The text is rendered on a `RenderTexture` and can be displayed using a `Sprite`.

The main components of this module include:
- `EText.StyleConfig`: A class to manage the style configuration of the text, such as color, base size, letter spacing, and line spacing.
- `EText`: The main class for handling enhanced text rendering. It parses the input text, applies styles, and renders the text on a texture.
- `EText._TextFragment`: A helper class to represent a fragment of text with specific style and configuration.

The module uses the `sfSystem` and `sfGraphics` libraries from the `sf` framework to handle vector operations and graphics rendering.
"""

from typing import List
from .sfSystem import Vector2u, Vector2f
from .sfGraphics import Sprite, Color, Font, Text, RenderTexture

class EText(Sprite):
    """
    A class for rendering enhanced text with various styles and configurations.
    """

    class StyleConfig:
        """
        A class to manage the style configuration of the text.
        """

        def __init__(self, color: Color, base_size: int, letter_spacing: float, line_spacing: float):
            """
            Default constructor.

            Parameters:
            - color: The color of the text.
            - base_size: The base size of the text.
            - letter_spacing: The letter spacing of the text.
            """

            self.color = color
            self.base_size = base_size
            self.letter_spacing = letter_spacing
            self.line_spacing = line_spacing

        def copy(self):
            """
            Returns a copy of the style configuration.

            Returns:
            - A copy of the style configuration.
            """

            config = EText.StyleConfig(self.color, self.base_size, self.letter_spacing, self.line_spacing)
            return config

    def __init__(self, font: Font, text: str, size: Vector2u, style_config: StyleConfig, text_pos: int = 0):
        """
        Default constructor.

        Parameters:
        - font              The font to use for rendering the text.
        - text              The text to be rendered. It can be applied with different styles and configurations using certain formatting codes. Bold, italic, underlined and strikethrough styles are supported, just like Markdown. If you want to change the color, use \c[color_code], it will use the same name static function in sf::Graphcs::Color. If you want to change the character size, use \s[size]. For example, \c[red]\s[24]Hello World!\c[white]\s[12]
        - size              The size of the text.
        - style_config      The style configuration for the text.
        - text_pos          The position of the text in the rendered rectangle.
        """

        self._font = font
        self._text = text
        self._size = size
        self._style_config = style_config
        self._text_pos = text_pos

        self._style = Text.Style.Regular

        self._fragment: EText._TextFragment = None
        self._render_fragments: List[List[Text]] = []
        self._fragments_list: List[Text] = []

        self._canvas = RenderTexture(self._size)
        self._parse()
        super().__init__(self._canvas.get_texture())

    def get_text(self):
        """
        Returns the text of this EText object.

        Returns:
        - The text of this EText object.
        """
        return self._text

    def set_text(self, text: str):
        """
        Sets the text of this EText object.

        Parameters:
        - text    The new text to be set.
        """
        self._text = text

        self._style = Text.Style.Regular

        self._fragment: EText._TextFragment = None
        self._render_fragments: List[List[Text]] = []
        self._fragments_list: List[Text] = []

        self._canvas.clear(Color.transparent())
        self._parse()

    def render(self):
        """
        Renders the text on the canvas.
        """

        for texts in self._render_fragments:
            for text in texts:
                self._canvas.draw(text)
        self._canvas.display()

    def render_one(self):
        """
        Renders one fragment of the text on the canvas.
        """

        if len(self._fragments_list) != 0:
            self._canvas.draw(self._fragments_list[0])
            self._fragments_list.pop(0)
            self._canvas.display()

    @staticmethod
    def from_str(text: str, font: Font, size: Vector2u, style_config: StyleConfig, text_pos: int = 0):
        """
        Creates an EText object from a string.

        Parameters:
        - text    The text to be rendered.
        - font    The font to use for rendering the text.
        - size    The size of the text.
        - style_config    The style configuration for the text.
        """

        text_obj = EText(font, text, size, style_config, text_pos)
        text_obj.render()
        return text_obj


    def _get_line_spacing(self, text: str, size = None):
        """
        Returns the line spacing for the given text.

        Parameters:
        - text    The text to calculate the line spacing for.
        - size    The size of the text. If not provided, the base size of the style configuration is used.
        """

        if len(text) == 0:
            return 0
        if self._style & Text.Style.Bold:
            bold = True
        else:
            bold = False

        if size is None:
            size = self._style_config.base_size
        bounds = self._font.get_glyph(ord(text), size, bold).bounds
        base = size + bounds.position.y + bounds.size.y
        linespace = base * self._style_config.line_spacing
        return linespace

    def _get_advance(self, text: str, size = None):
        """
        Returns the advance for the given text.

        Parameters:
        - text    The text to calculate the advance for.
        - size    The size of the text. If not provided, the base size of the style configuration is used.
        """

        if len(text) == 0:
            return 0
        if self._style & Text.Style.Bold:
            bold = True
        else:
            bold = False

        if size is None:
            size = self._style_config.base_size
        advance = self._font.get_glyph(ord(text), size, bold).advance * self._style_config.letter_spacing
        return advance

    def _parse(self):
        """
        Parses the input text and applies styles to the text fragments.
        """

        self._canvas.clear(Color.transparent())
        self._fragment = EText._TextFragment(self._font, '')
        self._fragment.apply_style_config(self._style_config)
        self._render_fragments.clear()
        self._render_fragments.append([])

        def end_phase():
            self._commit_fragment(self._fragment)
            self._fragment = EText._TextFragment(self._font, '')
            self._fragment.apply_style_config(self._style_config)
            self._fragment.apply_style(self._style)

        def between_bracket(i):
            j = 1
            found = False
            while i + j + 2 < len(self._text):
                part = self._text[i + j + 2]
                if part == ']':
                    found = True
                    break
                if part == '[':
                    break
                j += 1
            return (found, self._text[i + 3:i + j + 2], j)

        i = 0
        pos = 0
        while i < len(self._text):
            c = self._text[i]
            if c == '\n':
                end_phase()
                i += 1
                self._render_fragments.append([])
                pos = 0
                continue

            if c == '*' and len(self._text) > i + 1 and self._text[i + 1] == '*' and (i == 0 or (i > 0 and self._text[i - 1] != '\\')):
                if self._style & Text.Style.Bold:
                    self._style = self._style & (~Text.Style.Bold)
                    self._fragment.apply_style(self._style)
                else:
                    self._style = self._style | Text.Style.Bold
                    self._fragment.apply_style(self._style)
                i += 2
                continue

            if c == '*' and i > 0 and self._text[i - 1] != '\\':
                if self._style & Text.Style.Italic:
                    self._style = self._style & (~Text.Style.Italic)
                    self._fragment.apply_style(self._style)
                else:
                    self._style = self._style | Text.Style.Italic
                    self._fragment.apply_style(self._style)
                i += 1
                continue

            if c == '_' and len(self._text) > i + 1 and self._text[i + 1] == '_' and (i == 0 or i > 0 and self._text[i - 1]!= '\\'):
                if self._style & Text.Style.Underlined:
                    self._style = self._style & (~Text.Style.Underlined)
                    self._fragment.apply_style(self._style)
                else:
                    self._style = self._style | Text.Style.Underlined
                    self._fragment.apply_style(self._style)
                i += 2
                continue

            if c == '_' and i > 0 and self._text[i - 1]!= '\\':
                if self._style & Text.Style.StrikeThrough:
                    self._style = self._style & (~Text.Style.StrikeThrough)
                    self._fragment.apply_style(self._style)
                else:
                    self._style = self._style | Text.Style.StrikeThrough
                    self._fragment.apply_style(self._style)
                i += 1
                continue

            if c == '\\':
                if i + 2 < len(self._text) and self._text[i + 1] == 'c' and self._text[i + 2] == '[':
                    (found, color, j) = between_bracket(i)
                    if found:
                        self._style_config.color = eval(f"Color.{color}()")
                        self._fragment.apply_style_config(self._style_config)
                        i = i + j + 3
                        continue

                if i + 2 < len(self._text) and self._text[i + 1] == 's' and self._text[i + 2] == '[':
                    (found, size, j) = between_bracket(i)
                    if found:
                        self._style_config.base_size = int(size)
                        self._fragment.apply_style_config(self._style_config)
                        i = i + j + 3
                        continue

            advance = self._get_advance(c)
            if pos + advance >= self._size.x:
                self._render_fragments.append([])
                self._fragment.apply_text(c)
                end_phase()
                i += 1
                pos = 0
                continue
            pos += advance
            i += 1
            self._fragment.apply_text(c)
            end_phase()

        self._set_letter_position()

    class _TextFragment:
        """
        A helper class to represent a fragment of text with specific style and configuration.
        """

        def __init__(self, font: Font, text: str):
            """
            Default constructor.

            Parameters:
            - font    The font to use for rendering the text.
            - text    The text to be rendered.
            """

            self._text: Text = Text(font, text)
            self._style_config: EText.StyleConfig = None

        def apply_text(self, text: str):
            """
            Appends the given text to the existing text.

            Parameters:
            - text    The text to be appended.
            """

            self._text.set_string(text)

        def apply_style_config(self, style_config: 'EText.StyleConfig'):
            """
            Applies the given style configuration to the text.

            Parameters:
            - style_config    The style configuration to be applied.
            """

            self._style_config = style_config
            self._text.set_character_size(self._style_config.base_size)
            self._text.set_line_spacing(self._style_config.line_spacing)
            self._text.set_fill_color(self._style_config.color)

        def apply_style(self, style: Text.Style):
            """
            Applies the given style to the text.

            Parameters:
            - style    The style to be applied.
            """

            self._text.set_style(style)

        def get_bounds(self):
            """
            Returns the global bounds of the text.

            Returns:
            - The global bounds of the text.
            """

            return self._text.get_global_bounds()

        def get_text(self):
            """
            Returns the text object.

            Returns:
            - The text object.
            """

            return self._text

    def _commit_fragment(self, fragment: _TextFragment):
        """
        Commits the given text fragment to the rendering process.

        Parameters:
        - fragment    The text fragment to be committed.
        """

        text = fragment.get_text()
        if text.get_string().strip() == '':
            return
        self._render_fragments[-1].append(text)
        self._fragments_list.append(text)

    def _set_letter_position(self):
        """
        Sets the position of each letter in the text.
        """

        position = Vector2f(0, 0)
        for texts in self._render_fragments:
            max_h = 0
            line_width = 0
            for text in texts:
                h = self._get_line_spacing(text.get_string(), text.get_character_size())
                max_h = max(max_h, h)
                width = self._get_advance(text.get_string(), text.get_character_size())
                line_width += width
            for text in texts:
                text.set_position(position)
                x_offset = 0
                if self._text_pos == 1:
                    x_offset = (self._size.x - line_width) / 2
                elif self._text_pos == 2:
                    x_offset = self._size.x - line_width
                text.move(Vector2f(x_offset, 0))
                position.x += self._get_advance(text.get_string(), text.get_character_size())
            position = Vector2f(0, position.y + max_h)
