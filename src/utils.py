from easytextgen import EasyPrompt
from translate import Translator

trans_to_id = Translator(to_lang="id")
trans_to_en = Translator(to_lang="en")
prompt = EasyPrompt.from_file("assets/paraphrase-v1.yml")


def paraphrase_english(english_text: str) -> str:
    return prompt.get_output(english_text).output_text.strip()


def paraphrase_indonesian(indonesian_text: str) -> str:
    eng_text = trans_to_en.translate(indonesian_text)
    eng_paraphrased = paraphrase_english(eng_text)
    return trans_to_id.translate(eng_paraphrased)