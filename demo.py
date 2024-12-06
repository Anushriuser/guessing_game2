import random
import streamlit as st

#navigation
st.sidebar.title("navigation")
page=st.sidebar.radio("select a page",["portfolio","guessing_game"])

if page == "portfolio":
    st.title("MY PORTFOLIO")
    st.write("welcome to my portfolio")
    sub_option = st.sidebar.selectbox("Portfolio Options", ["name", "Contact_detail","hobbies","mini_project"])
    if sub_option=='name':
        st.write('Name : Anushri Thirumavalavan')
    elif sub_option=='contact_detail':
        st.write('e-mail: anushri6688@gmail.com')
    elif sub_option=='hobbies':
        st.write('listening music')
    elif sub_option=='mini_project':
        st.write('guessing game')

elif page == "guessing_game":

    st.title("welcome to guessing game")

    EASY_LEVEL_ATTEMPTS = 15
    MEDIUM_LEVEL_ATTEMPTS = 10
    HARD_LEVEL_ATTEMPTS = 5
    
    def difficulty_level(level_choosen):
        if level_choosen == 'easy':
            return EASY_LEVEL_ATTEMPTS
        elif level_choosen == 'medium':
            return MEDIUM_LEVEL_ATTEMPTS
        else:
            return HARD_LEVEL_ATTEMPTS

    #check if the guessed number is correct
    def check_answer(guessed_number, answer, attempts):
        if guessed_number > answer:
            st.write("Too high")
            return attempts - 1
        elif guessed_number < answer:
            st.write("Too low")
            return attempts - 1
        else:
            st.success(f"You got it! The answer was {answer}")
            return attempts

    #guessing game
    def guessing_game():
        st.title("Guessing Game")
        st.write("I am thinking of a number between 1 and 100.")

        if 'answer' not in st.session_state:
            st.session_state.answer = random.randint(1, 100)

    # Choose difficulty level
        level = st.selectbox("Choose a difficulty level:", ['easy', 'medium', 'hard'])
        attempts = st.session_state.get('attempts', difficulty_level(level))

    # remaining attempts
        st.write(f"You have {attempts} attempts remaining to guess the number.")

    # Get the user guess
        guessed_number = st.number_input("Make a guess:", min_value=1, max_value=100, step=1)


        if st.button("Submit Guess"):
            attempts = check_answer(guessed_number, st.session_state.answer, attempts)
            st.session_state.attempts = attempts

            if attempts == 0:
                st.error("You've run out of guesses, you lose.")
                st.session_state.answer = random.randint(1, 100)  
            # Reset  with a new number
                st.session_state.attempts = difficulty_level(level)  
            # Reset attempts
            elif guessed_number == st.session_state.answer:
                st.balloons()
                st.session_state.answer = random.randint(1, 100)  
                st.session_state.attempts = difficulty_level(level)  
            # Reset attempts
    guessing_game()
