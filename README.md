# Sublime Text 4 Half step font size adjustment Plugin

As outlined [here](https://github.com/sublimehq/sublime_text/issues/5300), Sublime Text's `font-size` setting uses [points](https://en.wikipedia.org/wiki/Point_(typography)) instead of pixels. As a result, in many cases, especially with non-standard fonts (but this is also true for default fonts like Consolas), you might need to use decimal values like `9.5` instead of rounded point amounts.

This plugin doesn't convert points to pixels, but it allows you to adjust the font size with the default keybindings by half a point for finer real-time control over your editing environment. It replaces the default Sublime Text keyboard and mouse bindings (i.e., Ctrl + "+" and Ctrl + "-" as well as Mouse Scroll Wheel) to change the font size by 0.5 of a point instead of the default 1 point.

When you change the font size with hotkeys/mouse wheel, the status bar displays the new font size value.

## Installation

1. Clone this repository or download the ZIP file.
2. Place the extracted folder in your Sublime Text "Packages" directory. You can find the "Packages" directory by going to `Preferences > Browse Packages` within Sublime Text.

## Usage

- **Increase Font Size:** Use the shortcut `Ctrl + +` or the mouse wheel to increase the font size by half a point.
- **Decrease Font Size:** Use the shortcut `Ctrl + -` or the mouse wheel to decrease the font size by half a point.

### Keybindings and Mouse Bindings

- Control font size with your mouse wheel:
	- Scroll Up while holding Ctrl: Increase font size
	- Scroll Down while holding Ctrl: Decrease font size

- Keyboard shortcuts for adjusting font size:
	- `Ctrl + +` or `Ctrl + =`: Increase font size
	- `Ctrl + -`: Decrease font size
	- `Ctrl + 0`: Reset font size to the value specified as `default_font_size = 11.5` inside the `half_step_font_size_adjustment.py`

> Note: If you prefer not to override the default Sublime Text behavior, you can assign different keybindings of your choice.

## Features

- Adjust font size by 0.5 points.
- Replaces default Sublime Text keyboard and mouse bindings to use 0.5-point adjustment instead of 1-point.
- Real-time feedback: The status bar instantly displays the new font size after it is changed.
- Works across all views in Sublime Text.
- Easily customizable to suit your preferences.

## License

Use this as you want for any purposes (even commercial). But don't try to sell it as a standalone product. 😹

## Contact

If you have any questions, suggestions, or issues, please feel free to [create an issue](https://github.com/alexchexes/Sublime-half-step-font-size-adjustment/issues) in the repository or reach out to me at alex.chexes@gmail.com.
