import json
import streamlit as st
from st_helper import *
from io import StringIO
from collections import Counter

st.set_page_config(page_icon='assets/pageicon.png',page_title='Frequency Analyser')

def base_visual_details():
    # Removes the debuging menu as well as footer
    st.markdown('<style>#MainMenu {Visibility:hidden;}footer {Visibility:hidden;} </style>', unsafe_allow_html=True)

    st.markdown(max_width(2500),unsafe_allow_html=True)

    st.markdown(remove_table_index(), unsafe_allow_html=True) # Hides the index of tables

    
    st.sidebar.markdown(credits(),unsafe_allow_html=True)

base_visual_details()

st.title('Frequency Analyser')


encoded_text=st.text_area('Enter text:').lower()

def pad(size):
	padding='st.write("")'
	return eval(padding)


def write_color_text(color,size,text):
	st.markdown(f'<{size}><span style="+color:{color}">{text}</span></{size}>',unsafe_allow_html=True)


def write_color_char(color,size='h3',char='',text='',object=''):
	return(f'<{size}><span style="color:{color}">{char}</span>{text}</{size}>')


pad(2)

#Global Variables

columns=['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
mutable_enc_text_display=st.empty()
st.session_state['encoded_text']=encoded_text
display_color='DarkCyan'

#Global Variables


with mutable_enc_text_display:
	write_color_text(display_color,'h7',encoded_text)


def char_replacer(to_replace,to_replace_with):

	global mutable_enc_text

	text=st.session_state['encoded_text']
	mapping_table=text.maketrans(to_replace,to_replace_with)

	display=text.translate(mapping_table)

	if display:
		with mutable_enc_text_display:
			write_color_text(display_color,'h7',display)

def single_char(text):
	return ' '.join([char for char in text.split() if len(char)==1])

def make_cells():

	to_replace_with_chars=''
	to_replace_chars=''

	write_color_text('MediumSeaGreen','h6','Enter characters to replace:')

	A,B,C,D,E,F,G,H,I,J,K,L,M,N,O,P,Q,R,S,T,U,V,W,X,Y,Z=st.columns([1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,])

	for col in columns:
		st.session_state[col]=eval(col).text_input(col,max_chars=1)

	for chars in columns:
		if st.session_state[chars]:
			to_replace_with_chars+=st.session_state[chars].upper()

			to_replace_chars+=chars.lower()

			char_replacer(to_replace_chars,to_replace_with_chars)



def get_common_cipher_letters(text):

    c={chars:round((text.count(chars)/len(text))*100,3) for chars in text}

    c=Counter(c)

    try:
    	c.pop('\n')
    except:
        # write_color_text('green','h2','Enter text to decode')
	    pass

    return (''.join(list(map(lambda x:x[0],c.most_common())))).lower()


def get_ngraphs(text,size):
	graph=text.split()
	table=[]

	for word in graph:
		if len(word)==size:
			table.append(word)
		else:
			for char in range(len(word)):
				p=word[char:char+size]

				if p.isalpha() and len(p)==size:
					table.append(p)

	return Counter(table).most_common(10)


def get_ngraphs_standalone(text,size):
	graph=text.split()
	table=[]

	for words in graph:
		if len(words)==size:
			table.append(words)
	return Counter(table).most_common(10)


def get_doubles(text):
	graph=text.split()
	table=[]

	for doubles in graph:
		for p in range(len(doubles)):
			if doubles[p-1]==doubles[p]:
				table.append(doubles[p]*2)


	return list(Counter(table).most_common(10))


pad(2)

common_cipher_letters=get_common_cipher_letters(encoded_text).replace(' ','')
common_lexicon_letters='etaoinshrdlcumwfgypbvkjxqz'
common_lexicon_digraphs='TH,HE,IN,ER,AN,RE,ES,ON,ST,NT,EN,AT,AI,AU,EA,EW,EY,OY,IE,OI'.split(',')[0:10]
common_lexicon_trigraphs='THE,AND,ING,ENT,ION,HER,FOR,THA,NTH,INT,ERE,TIO,SCH,TCH,EAU,IOU,EOU,SPL,SPR,SQU,THR'.split(',')[0:10]
common_lexicon_doubles='SS,EE,TT,FF,LL,MM,OO'.split(',')

common=st.columns([1,7])

with common[0]:
	write_color_text('green','h6','Common lexicon letters')
	write_color_text('green','h6','Common Cipher Letters')

with common[1]:
	st.markdown(horizontal_table(common_lexicon_letters,100),unsafe_allow_html=True)
	st.markdown(horizontal_table(common_cipher_letters,100),unsafe_allow_html=True)


# st.info(write_color_text('green','h4',single_char(encoded_text)))
st.info(f'Singular characters: {single_char(encoded_text)}')

make_cells()

#Table
digraphs_common,digraphs,trigraphs_common,trigraphs,doubles_common,doubles=st.columns([.4,.3,.4,.3,.4,.3])

digraphs.write('Digraphs')
digraphs.table(get_ngraphs_standalone(encoded_text,2))
digraphs_common.table({'Lexicon Digraphs':common_lexicon_digraphs})


trigraphs.write('Trigraphs')
trigraphs.table(get_ngraphs_standalone(encoded_text,3))
trigraphs_common.table({'Lexicon Trigraphs':common_lexicon_trigraphs})


doubles.write('Doubles')
doubles.table(get_doubles(encoded_text))
doubles_common.table({'Lexicon Doubles':common_lexicon_doubles})
#Table


#Import/Export Data
def load_config():

    st.sidebar.markdown('---')
	
    st.sidebar.download_button('Export Data',str(st.session_state))
    file=st.sidebar.file_uploader('Import Data','txt',)

    if file is not None:
        content=StringIO(file.getvalue().decode("utf-8")).read()
        st.session_state=json.loads(content.replace("'",'"'))

        

load_config()

with st.sidebar.expander('See Data',):
	st.write(st.session_state)
#Import/Export Data



# test={' ': 18.266, 'S': 10.173, 'O': 9.827, 'G': 7.746, 'F': 5.896, 'D': 4.855, 'L': 4.509, 'M': 4.046, 'K': 4.046, 'I': 3.815, 'P': 3.468, 'N': 3.353, 'C': 3.006, 'E': 2.659, 'U': 1.965, 'R': 1.965, 'W': 1.85, 'Q': 1.618, "'": 1.387, 'Y': 1.156, ',': 1.156, 'H': 0.925, 'X': 0.694, 'A': 0.578, 'V': 0.347, '.': 0.347, 'B': 0.231, 'J': 0.116}
# data=pd.DataFrame(index=test.keys(),data=test.values(),columns=['data'])

# st.bar_chart(data)

# st.bar_chart(data)
