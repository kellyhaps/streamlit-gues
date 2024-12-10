import streamlit as st
import random
import json
import pandas as pd
import numpy as np
from datetime import datetime

#To do for highscore;
#Function to check if highscore
#function to get the name
#At score to list
#sort list low to high and drop number 5

#page setup
st.set_page_config(page_title="GuesGame",page_icon="🌟")

#title
st.title("Stelly Game || 2.2")
st.subheader("In how many tries can you guess the number? :sunglasses:")

#open highscore
with open ('highscore.json') as f:
	highscore_list = json.load(f)

#enter high score to list
def enter_high_score():
	#open highscore
	with open ('highscore.json') as f:
		highscore_list = json.load(f)
	#get time
	now = str(datetime.now())
	now = now[:19]
	#get name & guessen
	name_win = st.session_state.name_win
	gueses = st.session_state.gueses_win
	#create win dictonary
	win_dict={"Name":name_win,"score":gueses,"Date":now}
	highscore_list.append(win_dict)
	#save list;
	with open ('highscore.json', 'w') as f:
		json.dump(highscore_list,f)
	#set button to fals
	#st.session_state.enter_high_score = False
	del st.session_state.open_dialog

print("dialog")
#dialog box for winning state
#if "open_dialog" in st.session_state:
@st.dialog("You got a highscore!")
def win_name():
	st.session_state.name_win = st.text_input("What's your name?")
	win_btn = st.button("Enter highscore",on_click=enter_high_score)
	#st.rerun()


#check for highscore
def check_for_higscore():
	#get guesscore;
	gueses = st.session_state.gues_count
	print(f"The gueses = {gueses}")
	#check for highscore
	for x in highscore_list:
		print(f"Score is; {x["score"]}")
		if gueses < x["score"]:
			#Highscoor balloons;
			st.balloons()
			print("winning here")
			#open name box
			st.session_state.open_dialog = "Hoi"
			st.session_state.gueses_win = st.session_state.gues_count
			#	name_win = st.text_input("What's your name?")
			#@st.dialog("You got a highscore!")
			#def win_name():
			#	st.session_state.name_win = st.text_input("What's your name?")
			#	win_btn = st.button("Enter highscore",on_click=enter_high_score)
			win_name()

			
			break


#Create a random number
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
	print(st.session_state.random_number)

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
		
		#function to check for win
		check_for_higscore()
		#set gues count to 0
		random_number2()
		#rerun app.
		#st.rerun()

	#To high
	if win > 0:
		placeholder2.write(f"You guesed to high! - {st.session_state.gues_count} number is; {st.session_state.random_number}")
	#To low
	if win < 0:
		placeholder2.write(f"You guesed to low!- {st.session_state.gues_count} number is; {st.session_state.random_number}")

else:
	#create a count
	st.session_state.gues_count = 0
#button to gues the number
st.button("gues the number", on_click=gues_number)

# --- section for highscore ---------------------------------------
st.divider()

#sort the highscore;
highscore_list = sorted(highscore_list, key=lambda x: x['score'])

#At number to highscore;
highscore_list_2=[]
count = 1
for x in highscore_list:
	#x = {"Place":score}
	x["Place"] = count
	highscore_list_2.append(x)
	count+=1
	#stop for top 5;
	if count > 5:
		#save this new 5 number long list
		with open ('highscore.json', 'w') as f:
			json.dump(highscore_list_2,f)
		break



#print as a table
df = pd.DataFrame(highscore_list_2)

# Move the last column to the first position
columns = df.columns.tolist()
columns = [columns[-1]] + columns[:-1]
df = df[columns]
#Put it to the screen;
st.markdown(df.to_html(index=False), unsafe_allow_html=True)
