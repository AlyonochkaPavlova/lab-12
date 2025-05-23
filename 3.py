dictionary = {}
with open('en-ru.txt', 'r', encoding='utf-8') as f_in:
    for line in f_in:
        if not line.strip():
            continue
        line = line.replace('–', '-').replace('—', '-')  # замена разных видов тире на обычный дефис
        parts = line.strip().split('-')
        if len(parts) != 2:
            print(f'Ошибка в строке: "{line}"')
            continue

        english_words = parts[0].strip()
        russian_translations = parts[1].strip().split(',')
        for translation in russian_translations:
            clean_translation = translation.strip()
            if clean_translation in dictionary:
                dictionary[clean_translation].append(english_words)
            else:
                dictionary[clean_translation] = [english_words]

with open('ru-en.txt', 'w', encoding='utf-8') as f_out:
    sorted_keys = sorted(dictionary.keys())

    for key in sorted_keys:
        translations = ', '.join(sorted(set(dictionary[key])))
        output_line = f'{key} – {translations}\n'
        f_out.write(output_line)
