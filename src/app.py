import streamlit as st
from src.password_generators import RandomPasswordGenerator, PinCodeGenerator, MemorablePasswordGenerator


st.image("./assets/banner.jpeg", use_container_width=True)
st.title(":zap: Password and PIN Code Generator")

option = st.radio(
    "Select the type of generator:",
    ("Random Password", "PIN Code", "Memorable Password")
)

if option == 'PIN Code':
    length = st.slider('Select the length of the pin code:', 4, 10, 4)
    generator = PinCodeGenerator(length=length)

elif option == 'Random Password':
    length = st.slider('Select the length of the password:', 8, 12, 16)
    include_symbols = st.toggle('Include symbols', value=True)
    include_numbers = st.toggle('Include numbers', value=True)
    generator = RandomPasswordGenerator(length=length, include_symbols=include_symbols, include_numbers=include_numbers)

else:
    num_words = st.slider('Select the number of words:', 2, 10, 4)
    separator = st.text_input('Separator:', value='-')
    is_capitalize = st.toggle('Capitalization', value=False)
    generator = MemorablePasswordGenerator(num_words=num_words, separator=separator, is_capitalize=is_capitalize)

password = generator.generate()
st.write(fr"Your password is: ``` {password} ``` ")
