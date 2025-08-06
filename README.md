# Password Generator

<p align="left">
<img src="assets/banner.jpeg" alt="Password Generator" style="border-radius: 10px;" width=80%>
</p>

A simple password generator application written in Python that supports multiple password generation strategies. Whether you need a random password with symbols and numbers, a memorable passphrase using real words, or a simple PIN code, this tool has you covered.

## 🚀 Features

- **🌐 Web Interface**: Interactive Streamlit web application with user-friendly controls
- **🎲 Random Password Generation**: Create secure passwords with customizable length and character sets
- **🧠 Memorable Password Generation**: Generate human-readable passphrases using real English words
- **🔢 PIN Code Generation**: Create numeric PIN codes of any length
- **⚙️ Flexible Configuration**: Customize all aspects of password generation through the web interface
- **🏗️ Object-Oriented Design**: Clean, extensible architecture using abstract base classes
- **📚 NLTK Integration**: Uses the Natural Language Toolkit for authentic word-based passwords
- **🎛️ Interactive Controls**: Real-time password generation with sliders, toggles, and input fields

## 🎯 Usage Options

### Option 1: Web Application (Recommended)
Launch the interactive Streamlit web interface for an easy-to-use password generation experience.

### Option 2: Command Line
Use the password generator classes directly in your Python scripts for programmatic access.

## 📁 Project Structure

```
pass_generator/
├── README.md                    # Project documentation
├── requirements.txt             # Python dependencies
├── assets/                      # Project assets
└── src/                        # Source code directory
    ├── app.py                  # Streamlit web application
    └── password_generators.py  # Core password generator classes
```

## 🛠️ Installation

### Prerequisites

- Python 3.7 or higher
- pip (Python package installer)

### Step-by-Step Installation

1. **Clone the repository** (or download the source code):
   ```bash
   git clone https://github.com/alireza-fllh/password_generator.git
   cd password_generator
   ```

2. **Install dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

3. **Run the web application**:
   ```bash
   streamlit run src/app.py
   ```

   This will start the web server and automatically open your default browser to the application.

## 🖥️ Web Application Usage

Once you launch the Streamlit app, you'll see an intuitive interface with:

### 🎛️ Generator Selection
Choose from three password generation types:
- **Random Password**: Customizable length (8-16 chars) with optional symbols and numbers
- **PIN Code**: Numeric codes with adjustable length (4-10 digits)
- **Memorable Password**: Word-based passwords with customizable separators and capitalization

### ⚙️ Configuration Options

**Random Password:**
- Length slider (8-16 characters)
- Include symbols toggle
- Include numbers toggle

**PIN Code:**
- Length slider (4-10 digits)

**Memorable Password:**
- Number of words slider (2-10 words)
- Custom separator input (default: `-`)
- Capitalization toggle

### 🔄 Real-time Generation
- Passwords are generated instantly as you adjust settings
- Click "Generate New Password" for a fresh password with the same settings

## 💻 Command Line Usage

You can also use the password generators programmatically:

```python
from src.password_generators import RandomPasswordGenerator, PinCodeGenerator, MemorablePasswordGenerator

# Generate a random password
random_gen = RandomPasswordGenerator(length=12, include_symbols=True, include_numbers=True)
password = random_gen.generate()

# Generate a PIN code
pin_gen = PinCodeGenerator(length=6)
pin = pin_gen.generate()

# Generate a memorable password
memorable_gen = MemorablePasswordGenerator(num_words=4, separator='-', is_capitalize=True)
passphrase = memorable_gen.generate()
```


## 📋 Requirements

### System Requirements

- **Operating System**: Windows, macOS, or Linux
- **Python Version**: 3.7 or higher
- **Memory**: Minimal (< 50MB)
- **Storage**: < 100MB (including NLTK word corpus)


### Installation Notes

- On first run, NLTK will automatically download the required word corpus (~10MB)
- Internet connection required for initial NLTK data download
- No additional system dependencies required

## ☑️ Testing

The password generator classes include built-in test functions. You can run them by executing:

```bash
python src/password_generators.py
```

This will run test cases for each password generator type and display sample outputs to verify functionality.

## 🛡️ Security Features

- **Cryptographically Secure**: Uses Python's `random` module with secure random number generation
- **No Data Storage**: Passwords are generated on-demand and not stored anywhere
- **Customizable Complexity**: Full control over character sets and password structure
- **Word-based Security**: Memorable passwords use real dictionary words for better memorability without sacrificing security


## 🔗 Links

- **Repository**: [https://github.com/alireza-fllh/password_generator](https://github.com/alireza-fllh/password_generator)
