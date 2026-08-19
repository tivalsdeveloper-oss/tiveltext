from tiveltext import color, colorize, color_list, color_dict, gradient, rainbow, style, strip_ansi


def test_string_color_and_f_string():
    name = "Lufuno"
    value = color(f"Hello {name}", "cyan")
    assert strip_ansi(value) == "Hello Lufuno"


def test_rgb_and_hex():
    assert strip_ansi(color("RGB", fg=(1, 2, 3))) == "RGB"
    assert strip_ansi(color("HEX", fg="#0ff")) == "HEX"


def test_list_and_dictionary():
    values = color_list(["Python", "C++"], "green")
    assert [strip_ansi(v) for v in values] == ["Python", "C++"]
    data = color_dict({"name": "Lufuno"}, key_color="cyan", value_color="white")
    assert [(strip_ansi(k), strip_ansi(v)) for k, v in data.items()] == [("name", "Lufuno")]


def test_recursive_collections():
    data = {"skills": ["Python", "C++"]}
    result = colorize(data, "cyan", recursive=True)
    assert strip_ansi(result["skills"][0]) == "Python"


def test_chainable_style():
    result = style("TivelText").bold().rgb(0, 255, 255).underline()
    assert strip_ansi(str(result)) == "TivelText"


def test_rainbow_and_gradient():
    assert strip_ansi(rainbow("TIVALS")) == "TIVALS"
    assert strip_ansi(gradient("TIVALS", "#00ffff", "#ff00ff")) == "TIVALS"
