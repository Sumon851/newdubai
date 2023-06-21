'''Fardini Khandaker
fardini@nawe.ae'''

import pandas as pd
import streamlit as st
from streamlit_extras.switch_page_button import switch_page

st.set_page_config(page_title='NAWE DUBAI INTELLIGENCE PLATFORM',initial_sidebar_state='collapsed',layout='wide')
no_sidebar_style = """
    <style>
        div[data-testid="stSidebarNav"] {display: none;}
    </style>
"""
st.markdown(no_sidebar_style, unsafe_allow_html=True)
st.header('NAWE DUBAI CONSULTANCY INTELLIGENCE PLATFORM')
st.markdown("---")
#st.subheader('please select following criteria to estimate budget
df1=pd.read_excel('budget-fk.xlsx',sheet_name='Sheet1')
df_area=pd.read_excel('budget-fk.xlsx',sheet_name='ST-1')
df_area=df_area.fillna(' ')


x=st.selectbox('How large is your project area?',options=df_area['Rate'].unique(),help='The size of the project area is an important variable by which we can get an idea of the vastness and extent of the project. Thus, to evaluate a project we need the client to define the total project area in hectare unit.')

final_df=pd.DataFrame(columns=df_area.columns)
def main_col(a):
	
		df=pd.read_excel('budget-fk.xlsx',sheet_name=a)
		df=df.fillna(' ')
		df.index=df.Rate
		df=df.drop(columns='Rate')
		constant_df=df.loc[[x]]
		return constant_df
main_service=['Stormwater','Water','Sewer'] ###main services

###list of subservice under main services
subsevrice=[['Stormwater Investigation for detailed plan area','Stormwater Investigation for building permit (bygglov)','Stormwater Investigation for existing properties','Flood Investigation (1D stormwater pipe modelling)', 'Rain bed design with calculations','Stormwater pipe network design'],['Water distribution network modelling','Water hammer analysis','Existing water distribution network investigation',],['Existing sewer network investigation(Gravity)','Existing sewer network investigation(Pressure)','Existing sewer network investigation(Gravity and pressure)','Sewer distribution network investigation','Inleak analysis according to flow measurement and rainfall data','Sewer pump analysis and calculation','Sewer pipe network design']]

selection=[]
columns=st.columns(3)
if x==' ':
	st.write(':red[Please select area first]')
else:
	for i,name in enumerate(main_service):
		with columns[i]:
			
	
			st.header(name)
			st.divider()
			a=st.multiselect('**:red[Select a service]**',options=subsevrice[i])[:]
			selection.append(a)
		
			print(selection)
	selection_flat = [item for sublist in selection for item in sublist]
	
	#print(selection_flat)
	budget=[]
	final_df=pd.DataFrame()
	
	
	for item in selection_flat:
		a=df1['Sheet'].loc[df1['Sub service']==item].values[0]
		print(a)
		constant_df=main_col(a)
		print(constant_df)
		final_df=pd.concat([final_df,constant_df],ignore_index=True)
	
	
	final_df['services']=selection_flat
	
	final_df['area']=x
	
	final_df.to_excel('new.xlsx',index=False)
	
	
	
	
	if selection_flat==[]:
		st.write(':red[Please select a service]')
	
	else:
		if st.button('NEXT :arrow_forward:'):
			switch_page('web_app_new')




