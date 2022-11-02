from enchant.checker import SpellChecker


def spell_check(report_child_page, dictionary='spell_dictionary.txt', report_spell_check='spell_check.txt'):

    d = []
    misspelled = []

    check_ru = SpellChecker('ru_RU')  # \venv\Lib\site-packages\enchant\data\mingw64\share\enchant\hunspell
    check_en = SpellChecker('en')

    with open(dictionary, 'r', encoding='utf-8') as f:
        d += f.read().splitlines()

    with open(report_child_page, 'r', encoding='utf-8') as f:
        check_ru.set_text(f.read())

        errors = [i.word for i in check_ru]
        check_en.set_text(' '.join(errors))
        errors = [i.word for i in check_en]
        for i in errors:
            if not (i in d):
                misspelled += i

    with open(report_spell_check, 'a', encoding='utf-8') as f:
        f.write(''.join(misspelled))


if __name__ == "__main__":
    spell_check(report_child_page='report.txt')
