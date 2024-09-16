from dotenv import load_dotenv
import os
import sys

import deepl

from french_citations import citations as french_citations

load_dotenv()

trad = os.getenv('TRAD')
translator = deepl.Translator(trad)

def translate_fr_to_en(fr_str):
    return translator.translate_text(fr_str, source_lang="FR", target_lang="EN-US")

def translate_fr_to_sp(fr_str):
    return translator.translate_text(fr_str, source_lang="FR", target_lang="ES")

def translate_french_citations_to_en():
    with open("english_citations.py", "w", encoding="utf-8") as file:
        file.write("citations = [\n")

        for cit in french_citations:
            file.write(f'\t{{"citation": "{translate_fr_to_en(cit["citation"])}", "autor": "{cit["autor"]}"}},\n')

        file.write("]")

def translate_french_citations_to_sp():
    with open("spanish_citations.py", "w", encoding="utf-8") as file:
        file.write("citations = [\n")

        for cit in french_citations:
            file.write(f'\t{{"citation": "{translate_fr_to_sp(cit["citation"])}", "autor": "{cit["autor"]}"}},\n')

        file.write("]")
    

if __name__ == "__main__":
    if len(sys.argv) > 1:
        if sys.argv[1] == "translate_french_citations_to_en":
            translate_french_citations_to_en()
        elif sys.argv[1] == "translate_french_citations_to_sp":
            translate_french_citations_to_sp()
        else:
            print("unknow command")
    else:
        print("you should indicate a command")