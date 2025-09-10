# Chinese Flashcards App

An interactive desktop flashcard application for learning Chinese vocabulary with pinyin

## Features

- Auto-flip Cards: Cards automatically flip after 2.5 seconds to show translations
- Pinyin Display: Shows correct pronunciation for each Chinese character
- Progress Tracking: Save words you're struggling with
- Clipboard Integration: Automatically copies Chinese characters to your clipboard
- Export Feature: Save your study list to CSV for external review

### Prerequisites
- Python 3.7 or higher
- pip (Python package installer)

### Setup
1. **Clone the repository**
```bash
  git clone https://github.com/selvingarcia/ChineseFlashCards.git
  cd ChineseFlashCards
```

2. **Install required packages**
```bash
pip install pandas pillow pyperclip
```
2. **Run the application**
```bash
python main.py
```

## How to use 
- Green Button (Right): Click when you know the word → moves to next card
- Red Button (Wrong): Click when you forgot the word → saves for review and moves to next
- Save Button (Diskette): Export your forgotten words to study_words.csv

## License

[MIT](https://choosealicense.com/licenses/mit/)
