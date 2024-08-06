from jiwer.process import process_characters, process_words
from jiwer.transformations import cer_default, wer_default
from normalize import Normalize


def clean(inp: str) -> str:
    """Convertes all the multi-shitespace characters to single whitespace
    """
    # Reduce double newlines to single newlines
    while '\n\n' in inp:
        inp = inp.replace('\n\n', '\n')
    # Convert window style return to unix style return
    while '\r\n' in inp:
        inp = inp.replace('\r\n', '\n')
    # as a backup, window style return (\r) should not be present in the text
    while '\r' in inp:
        inp = inp.replace('\r', '')
    # reduce newlines to whitespaces
    while '\n' in inp:
        inp = inp.replace('\n', ' ')
    # reduce double whitespaces to single whitespace
    while '  ' in inp:
        inp = inp.replace('  ', ' ')
    # return after removing trailing whitespaces
    return inp.strip()


def evaluate(ref_text: str, pred_text: str, language: str) -> tuple[float, float]:
    """Takes the 2 strings to be compared and the language as input and outputs
    a tuple containing CRR and WRR of the pred_text in comparison to ref_text.
    language is a string which takes one of these values:
    ('assamese', 'bengali', 'english', 'gujarati', kannada',
    'kashmiri', 'konkani', 'maithili', 'malayalam', 'manipuri',
    'marathi', 'nepali', 'oriya', 'punjabi', 'sanskrit', 'santali',
    'sindhi', 'tamil', 'telugu', 'urdu')

    *Usage*
    [IN]  >> evaluate("hello world", "Hell world", 'english')
    [OUT] >> (82.0, 50.0)
    """
    cleaned_ref = clean(ref_text)
    cleaned_pred = clean(pred_text)
    normalized_ref = Normalize(language).run(cleaned_ref)
    normalized_pred = Normalize(language).run(cleaned_pred)

    crr, wrr = 0.0, 0.0
    try:
        a = process_words(
            normalized_ref,
            normalized_pred,
            wer_default,
            wer_default,
        )
        wrr = round(100.0 * a.hits / len(normalized_ref.split(' ')), 2)
        if wrr < 0: wrr = 0.0

        b = process_characters(
            normalized_ref,
            normalized_pred,
            cer_default,
            cer_default,
        )
        crr = round(100.0 * b.hits / len(normalized_ref))
        if crr < 0: crr = 0.0
    except ZeroDivisionError:
        print('Zero Division error encounter: Please check ref_text')
    except Exception as e:
        print('Unknown Error Encountered: {}'.format(e))
    return (crr, wrr)


if __name__ == '__main__':
    pass