# -*- coding: utf-8 -*-
"""spellchecker_rule_based_02.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1-J6dmvzpdV_f4XN3BCkJuEzheBo8Rbs7
"""

import re

# Verb correction dictionary
correct_verbs = {
    "මම": {
        "future": {
            "යාවි": "යන්නෙමි",
            "කාවි": "කන්නෙමි",
            "බෝවි": "බොන්නෙමි",
            "නාවි": "නාන්නෙමි",
            "නගීවි": "නගින්නෙමි",
            "බහීවි": "බසින්නෙමි",
            "අදීවි": "අදින්නෙමි",
            "කරාවි": "කරන්නෙමි",
            "ඒවි": "එන්නෙමි",
            "සෝදාවි": "සෝදන්නෙමි",
            "පිසීවි": "පිසින්නෙමි",
            "කරාවී": "කරන්නෙමි",
            "ගාවි": "ගන්නෙමි",
            "හිතාවී": "හිතන්නෙමි",
            "වේවි": "වෙන්නෙමි"
        },
        "present": {
            "යනවා": "යමි",
            "කනවා": "කමි",
            "බොනවා": "බොමි",
            "නානවා": "නාමි",
            "නගිනවා": "නගිමි",
            "බහිනවා": "බහිමි",
            "අදිනවා": "අදිමි",
            "කරනවා": "කරමි",
            "එනවා": "එමි",
            "සෝදනවා": "සෝදමි",
            "පිසිනවා": "පිසිමි",
            "ගියා": "යමි",
            "ගන්නවා": "ගමි",
            "හිතනවා": "හිතමි",
            "වෙනවා": "වෙමි"
        },
        "past": {
            "යන්නේය": "ගියෙමි",
            "කෑවේය": "කෑවෙමි",
            "බීවේය": "බීවෙමි",
            "නෑවේය": "නෑවෙමි",
            "නැග්ගේය": "නැග්ගෙමි",
            "බැස්සේය": "බැස්සෙමි",
            "ඇන්දේය": "ඇන්දෙමි",
            "කරේය": "කලෙමි",
            "එන්නේය": "ආවෙමි",
            "සේදුවේය": "සේදුවෙමි",
            "පිස්සේය": "පිස්සෙමි",
            "කලේය": "කලෙමි",
            "ගන්නේය": "ගත්තෙමි",
            "හිතන්නේය": "හිතුවෙමි",
            "වුනා": "වුනෙමි"
        }
    },
    "අපි": {
        "future": {
            "යාවි": "යන්නෙමු",
            "කාවි": "කන්නෙමු",
            "බෝවි": "බොන්නෙමු",
            "නාවි": "නාන්නෙමු",
            "නගීවි": "නගින්නෙමු",
            "බහීවි": "බසින්නෙමු",
            "අදීවි": "අදින්නෙමු",
            "කරාවි": "කරන්නෙමු",
            "ඒවි": "එන්නෙමු",
            "සෝදාවි": "සෝදන්නෙමු",
            "පිසීවි": "පිසින්නෙමු",
            "කරාවී": "කරන්නෙමු",
            "ගාවි": "ගන්නෙමු",
            "හිතාවී": "හිතන්නෙමු",
            "වේවි": "වෙන්නෙමු"

        },
        "present": {
            "යනවා": "යමු",
            "කනවා": "කමු",
            "බොනවා": "බොමු",
            "නානවා": "නාමු",
            "නගිනවා": "නගිමු",
            "බහිනවා": "බහිමු",
            "අදිනවා": "අදිමු",
            "කරනවා": "කරමු",
            "එනවා": "එමු",
            "සෝදනවා": "සෝදමු",
            "පිසිනවා": "පිසිමු",
            "කරනවා": "කරමු",
            "වුනා": "වුනෙමු",
            "ගන්නවා": "ගමු",
            "හිතනවා": "හිතමු",
             "වෙනවා":"වෙමු"
        },
        "past": {
            "යන්නේය": "ගියෙමු",
            "කෑවේය": "කෑවෙමු",
            "බීවේය": "බීවෙමු",
            "නෑවේය": "නෑවෙමු",
            "නැග්ගේය": "නැග්ගෙමු",
            "බැස්සේය": "බැස්සෙමු",
            "ඇන්දේය": "ඇන්දෙමු",
            "කරේය": "කලෙමු",
            "එන්නේය": "ආවෙමු",
            "සේදුවේය": "සේදුවෙමු",
            "පිස්සේය": "පිස්සෙමු",
            "කලේය": "කලෙමු",
            "ගන්නේය": "ගත්තෙමු",
            "හිතන්නේය": "හිතුවෙමු",
            "වුනා": "වුනෙමු"
        }
    }
}

# Letter validation rules
def validate_letters(text):
    """Validate letters according to rules for 'ෂ' and 'ශ'."""
    invalid_occurrences = []
    invalid_occurrences.extend(re.findall(r'ෂන', text))  # 'ෂ' followed by 'න'
    invalid_occurrences.extend(re.findall(r'ශණ', text))  # 'ශ' followed by 'ණ'
    return invalid_occurrences

def correct_word(word):
    """Correct specific letter sequences."""
    word = re.sub(r'ෂන', 'ෂණ', word)  # Replace 'ෂන' with 'ෂණ'
    word = re.sub(r'ශණ', 'ශන', word)  # Replace 'ශණ' with 'ශන'
    return word

def identify_tense(verb, subject):
    """Identify the tense of the verb."""
    if subject in correct_verbs:
        for tense in ["future", "present", "past"]:
            if verb in correct_verbs[subject][tense]:
                return tense
    return None

def correct_verb(subject, tense, verb):
    """Correct the verb based on subject and tense."""
    return correct_verbs.get(subject, {}).get(tense, {}).get(verb, verb)

def correct_sentence(sentence):
    """Corrects the sentence by applying letter rules and verb corrections."""
    corrected_words = []
    suggestions = []

    words = sentence.split()
    subject = "මම" if "මම" in words else "අපි" if "අපි" in words else None

    for word in words:
        original_word = word

        # Correct letter sequences
        corrected_word = correct_word(word)
        if corrected_word != original_word:
            suggestions.append(f"Corrected '{original_word}' to '{corrected_word}'")
        word = corrected_word

        # Correct verbs
        if subject:
            tense = identify_tense(word, subject)
            if tense:
                corrected_word = correct_verb(subject, tense, word)
                if corrected_word != word:
                    suggestions.append(f"Corrected verb: '{word}' to '{corrected_word}'")
                word = corrected_word

        corrected_words.append(word)

    corrected_sentence = " ".join(corrected_words)
    return corrected_sentence, suggestions

# Main program loop
while True:
    user_input = input("\nEnter a sentence to validate and correct (type 'exit' to quit): ")
    if user_input.lower() == "exit":
        break

    # Validate letters
    invalid_sequences = validate_letters(user_input)
    if invalid_sequences:
        print("\nInvalid letter sequences found:")
        for sequence in invalid_sequences:
            print(f"Invalid sequence: {sequence}")

    # Correct sentence
    corrected_sentence, suggestions = correct_sentence(user_input)
    print("\nCorrected Sentence:")
    print(corrected_sentence)

    if suggestions:
        print("\nSuggestions:")
        for suggestion in suggestions:
            print(suggestion)

import re

# Verb correction dictionary
correct_verbs = {
    "මම": {
        "future": {
            "යාවි": "යන්නෙමි",
            "කාවි": "කන්නෙමි",
            "බෝවි": "බොන්නෙමි",
            "නාවි": "නාන්නෙමි",
            "නගීවි": "නගින්නෙමි",
            "බහීවි": "බසින්නෙමි",
            "අදීවි": "අදින්නෙමි",
            "කරාවි": "කරන්නෙමි",
            "ඒවි": "එන්නෙමි",
            "සෝදාවි": "සෝදන්නෙමි",
            "පිසීවි": "පිසින්නෙමි",
            "කරාවී": "කරන්නෙමි",
            "ගාවි": "ගන්නෙමි",
            "හිතාවී": "හිතන්නෙමි",
            "වේවි": "වෙන්නෙමි"
        },
        "present": {
            "යනවා": "යමි",
            "කනවා": "කමි",
            "බොනවා": "බොමි",
            "නානවා": "නාමි",
            "නගිනවා": "නගිමි",
            "බහිනවා": "බහිමි",
            "අදිනවා": "අදිමි",
            "කරනවා": "කරමි",
            "එනවා": "එමි",
            "සෝදනවා": "සෝදමි",
            "පිසිනවා": "පිසිමි",
            "ගියා": "යමි",
            "ගන්නවා": "ගමි",
            "හිතනවා": "හිතමි",
            "වෙනවා": "වෙමි"
        },
        "past": {
            "යන්නේය": "ගියෙමි",
            "කෑවේය": "කෑවෙමි",
            "බීවේය": "බීවෙමි",
            "නෑවේය": "නෑවෙමි",
            "නැග්ගේය": "නැග්ගෙමි",
            "බැස්සේය": "බැස්සෙමි",
            "ඇන්දේය": "ඇන්දෙමි",
            "කරේය": "කලෙමි",
            "එන්නේය": "ආවෙමි",
            "සේදුවේය": "සේදුවෙමි",
            "පිස්සේය": "පිස්සෙමි",
            "කලේය": "කලෙමි",
            "ගන්නේය": "ගත්තෙමි",
            "හිතන්නේය": "හිතුවෙමි",
            "වුනා": "වුනෙමි"
        }
    },
    "අපි": {
        "future": {
            "යාවි": "යන්නෙමු",
            "කාවි": "කන්නෙමු",
            "බෝවි": "බොන්නෙමු",
            "නාවි": "නාන්නෙමු",
            "නගීවි": "නගින්නෙමු",
            "බහීවි": "බසින්නෙමු",
            "අදීවි": "අදින්නෙමු",
            "කරාවි": "කරන්නෙමු",
            "ඒවි": "එන්නෙමු",
            "සෝදාවි": "සෝදන්නෙමු",
            "පිසීවි": "පිසින්නෙමු",
            "කරාවී": "කරන්නෙමු",
            "ගාවි": "ගන්නෙමු",
            "හිතාවී": "හිතන්නෙමු",
            "වේවි": "වෙන්නෙමු"

        },
        "present": {
            "යනවා": "යමු",
            "කනවා": "කමු",
            "බොනවා": "බොමු",
            "නානවා": "නාමු",
            "නගිනවා": "නගිමු",
            "බහිනවා": "බහිමු",
            "අදිනවා": "අදිමු",
            "කරනවා": "කරමු",
            "එනවා": "එමු",
            "සෝදනවා": "සෝදමු",
            "පිසිනවා": "පිසිමු",
            "කරනවා": "කරමු",
            "වුනා": "වුනෙමු",
            "ගන්නවා": "ගමු",
            "හිතනවා": "හිතමු",
             "වෙනවා":"වෙමු"
        },
        "past": {
            "යන්නේය": "ගියෙමු",
            "කෑවේය": "කෑවෙමු",
            "බීවේය": "බීවෙමු",
            "නෑවේය": "නෑවෙමු",
            "නැග්ගේය": "නැග්ගෙමු",
            "බැස්සේය": "බැස්සෙමු",
            "ඇන්දේය": "ඇන්දෙමු",
            "කරේය": "කලෙමු",
            "එන්නේය": "ආවෙමු",
            "සේදුවේය": "සේදුවෙමු",
            "පිස්සේය": "පිස්සෙමු",
            "කලේය": "කලෙමු",
            "ගන්නේය": "ගත්තෙමු",
            "හිතන්නේය": "හිතුවෙමු",
            "වුනා": "වුනෙමු"
        }
    }
}

# Letter validation rules
def validate_letters(text):
    """Validate letters according to rules for 'ෂ' and 'ශ'."""
    invalid_occurrences = []
    invalid_occurrences.extend(re.findall(r'ෂන', text))  # 'ෂ' followed by 'න'
    invalid_occurrences.extend(re.findall(r'ශණ', text))  # 'ශ' followed by 'ණ'
    return invalid_occurrences

def correct_word(word):
    """Correct specific letter sequences."""
    word = re.sub(r'ෂන', 'ෂණ', word)  # Replace 'ෂන' with 'ෂණ'
    word = re.sub(r'ශණ', 'ශන', word)  # Replace 'ශණ' with 'ශන'
    return word

def identify_tense(verb, subject):
    """Identify the tense of the verb."""
    if subject in correct_verbs:
        for tense in ["future", "present", "past"]:
            if verb in correct_verbs[subject][tense]:
                return tense
    return None

def correct_verb(subject, tense, verb):
    """Correct the verb based on subject and tense."""
    return correct_verbs.get(subject, {}).get(tense, {}).get(verb, verb)

def correct_sentence(sentence):
    """Corrects the sentence by applying letter rules and verb corrections."""
    corrected_words = []
    suggestions = []

    words = sentence.split()
    subject = "මම" if "මම" in words else "අපි" if "අපි" in words else None

    for word in words:
        original_word = word

        # Correct letter sequences
        corrected_word = correct_word(word)
        if corrected_word != original_word:
            suggestions.append(f"Corrected '{original_word}' to '{corrected_word}'")
        word = corrected_word

        # Correct verbs
        if subject:
            tense = identify_tense(word, subject)
            if tense:
                corrected_word = correct_verb(subject, tense, word)
                if corrected_word != word:
                    suggestions.append(f"Corrected verb: '{word}' to '{corrected_word}'")
                word = corrected_word

        corrected_words.append(word)

    corrected_sentence = " ".join(corrected_words)
    return corrected_sentence, suggestions

def calculate_accuracy(corrected, true):
    """Calculate the accuracy of the corrected paragraph compared to the true paragraph."""
    corrected_words = corrected.split()
    true_words = true.split()

    total_words = len(true_words)
    matching_words = sum(1 for c, t in zip(corrected_words, true_words) if c == t)

    return (matching_words / total_words) * 100 if total_words > 0 else 0

# Main program loop
while True:
    user_input = input("\nEnter a sentence to validate and correct (type 'exit' to quit): ")
    if user_input.lower() == "exit":
        break

    true_paragraph = input("\nEnter the true paragraph: ")

    # Validate letters
    invalid_sequences = validate_letters(user_input)
    if invalid_sequences:
        print("\nInvalid letter sequences found:")
        for sequence in invalid_sequences:
            print(f"Invalid sequence: {sequence}")

    # Correct sentence
    corrected_sentence, suggestions = correct_sentence(user_input)
    print("Corrected Sentence:")
    print(corrected_sentence)

    if suggestions:
        print("Suggestions:")
        for suggestion in suggestions:
            print(suggestion)

    # Calculate accuracy
    accuracy = calculate_accuracy(corrected_sentence, true_paragraph)
    print(f"Accuracy compared to the true paragraph: {accuracy:.2f}%")