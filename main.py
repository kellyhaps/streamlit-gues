import streamlit as st
import random

#title
st.title("Gues the number2")
st.subheader("In how many tries can you guess the number? :sunglasses:")

def random_number2():
	st.session_state.random_number = random.randint(0,100)
	st.session_state.gues_count = 0
	#del win in session state
	if "win" in st.session_state:
		del st.session_state.win

#function to gues
def gues_number():
	st.session_state.win = int(gues)-int(st.session_state.random_number)
	#update gues
	st.session_state.gues_count += 1

#placeholder
placeholder = st.empty()

#check if number is create;
if "random_number" in st.session_state:
	placeholder.write(f"Random number picked")
	#print(st.session_state.random_number)

#button
st.button("Pick a number",on_click=random_number2, icon=":material/refresh:")
#placeholder2
placeholder2 = st.empty()
#input
gues = st.number_input("gues the number",min_value=0,max_value=100)

#check if number is guesed
if "win" in st.session_state:
	win = st.session_state.win
	#Check if you won
	if win == 0:
		placeholder2.subheader(f"You got it!! It took you; {st.session_state.gues_count}")
		st.balloons()
		#set gues count to 0
		random_number2()
		#st.session_state.gues_count = 0
		#st.session_state.win = 1
	#To high
	if win > 0:
		placeholder2.write(f"You guesed to high! - {st.session_state.gues_count}")
	#To low
	if win < 0:
		placeholder2.write(f"You guesed to low!- {st.session_state.gues_count}")

else:
	#create a count
	st.session_state.gues_count = 0
#button to gues the number
st.button("gues the number", on_click=gues_number)