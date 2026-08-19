from tiveltext import text, fonts, decorate, colorize, strip_ansi

def test_block():
    result = text("ABC", font="block", plain=True)
    assert "█" in result and "\n" in result

def test_unicode_styles():
    assert text("Hello", font="bold").startswith("𝐇")
    assert text("Hello", font="gothic").startswith("𝔥")

def test_registry():
    assert "block" in fonts() and "gothic" in fonts()

def test_colors():
    assert strip_ansi(colorize("hello", "cyan")) == "hello"
    assert strip_ansi(colorize("hello", "#00ffff", "#111111")) == "hello"

def test_decorations():
    result = decorate("Hi", "double")
    assert "Hi" in result and "╔" in result
