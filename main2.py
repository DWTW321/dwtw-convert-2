import pint
import inquirer
from rich.console import Console
from deep_translator import GoogleTranslator

ureg = pint.UnitRegistry()
ureg.autoconvert_offset_to_baseunit = True

def convert_unit(value, from_unit, to_unit):
    return (value * ureg(from_unit)).to(to_unit)

def translate_text(text, src, dest):
    translator = GoogleTranslator(source=src, target=dest)
    return translator.translate(text)

def main():
    console = Console()
    console.print("Welcome to the unit conversion and translation program!", style="bold green")
    categories = [
        inquirer.List(
            "category",
            message="Which category would you like to choose?",
            choices=["Unit conversion", "Text translation"],
        ),
    ]
    category = inquirer.prompt(categories)["category"]
    if category == "Unit conversion":
        console = Console()
        console.print("Welcome to the unit conversion program!", style="bold green")
        categories = [
            inquirer.List(
                "category",
                message="Which category would you like to convert?",
                choices=["Length", "Weight", "Temperature"],
            ),
        ]
        category = inquirer.prompt(categories)["category"]
        if category == "Length":
            units = ["mm", "cm", "m", "km", "in", "ft", "yd", "mi"]
        elif category == "Weight":
            units = ["mg", "g", "kg", "t", "oz", "lb", "st"]
        elif category == "Temperature":
            units = ["degC", "degF", "K"]
        else:
            console.print("Invalid category!", style="bold red")
            return
        questions = [
            inquirer.Text(
                "value",
                message="Enter the value you want to convert:",
                validate=lambda _, x: x.isdigit(),
            ),
            inquirer.List(
                "from_unit",
                message="Enter the unit you want to convert from:",
                choices=units,
            ),
            inquirer.List(
                "to_unit",
                message="Enter the unit you want to convert to:",
                choices=units,
            ),
        ]
        answers = inquirer.prompt(questions)
        value = float(answers["value"])
        from_unit = answers["from_unit"]
        to_unit = answers["to_unit"]
        result = convert_unit(value, from_unit, to_unit)
        console.print(f"{value} {from_unit} is equal to [bold blue]{result.magnitude:.2f}[/bold blue] [bold red]{to_unit}[/bold red]")
    elif category == "Text translation":
        languages = ["en", "zh-CN", "ja", "fr", "de", "es", "ru", "ar", "hi"]
        questions = [
            inquirer.Text(
                "text",
                message="Enter the text you want to translate:",
            ),
            inquirer.List(
                "src",
                message="Enter the source language:",
                choices=languages,
            ),
            inquirer.List(
                "dest",
                message="Enter the destination language:",
                choices=languages,
            ),
        ]
        answers = inquirer.prompt(questions)
        text = answers["text"]
        src = answers["src"]
        dest = answers["dest"]
        result = translate_text(text, src, dest)
        console.print(f"[bold blue]{text}[/bold blue] in {src} is translated to [bold red]{result}[/bold red] in {dest}")
    else:
        console.print("Invalid category!", style="bold red")
        return

if __name__ == '__main__':
    main()
