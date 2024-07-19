''' My midterm translated into streamlit'''

import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

sections = ['Overview', 'Proposal', 'The Data', 'Visualizations', 'Conclusion']

# gonna try to make a sidebar that replaces my original table of contents

# opening layout. can i potentially condense this?
st.header('The Fall of the Soviet Union and its effects on American space flight')
st.markdown('![liftoff gif](https://64.media.tumblr.com/902ce0b02e2b5e8493b5ebad69b00a2c/tumblr_ng0t8eqPcY1rnq3cto1_500.gif)')
st.markdown('## Table of Contents')
st.markdown('1. [Overview](#overview)')
st.markdown('2. [Proposal](#proposal)')
st.markdown('3. [The Data](#the-data)')
st.markdown('4. [Data Cleaning](#data-cleaning)')
st.markdown('5. [Visualizations](#visualizations)')
st.markdown('6. [Conclusion](#conclusion)')

# removing all of the apostrophies is annoying
st.header('Overview') 
st.markdown('''The launch of Sputnik-1 marked the start of the Space Race between the United States and the Soviet Union.
             Throughout the years, the Soviets would dominate space, reaching new milestones left and right. The US would respond to Sputnik by racing to establish the National Aeronautics and Space Administration (NASA). Each Space Agency (NASA and the Strategic Rocket Forces of the Russian Federation - RVSN) would both compete in what is now dubbed the Space Race, 
            a product of the Cold War which pitted the two countries against each other to reach new milestones in the exploration of Space. The end goal for both countries was the Moon, which President John F. Kennedy stated that the US would send humans by 1970. This would occur in 1969, and to the American public was essentially the culmination of the space race. 
            However, the Soviets would continue to launch plenty of rockets in order to further their military and technological prowess in Space. The Soviets would suffer different setbacks geopolitically however in the late 70s and early 80s, and the Soviet Union would ultimately fall in 1991. This set back the russians heavily, with funding for Space Launches dropping and the number of launches dropping significantly. 
            It wouldnt be until the mid 2000s that Roscosmos (the russian federations launch agency) would bounce back and start launching not only their own satellites and missions again, but outsourcing their cheap SLVs (Space Launch Vehicles) to other countries, and even the United States. From 1991 to the mid 2000s, NASA had no competition and public support for sending more explorative launches up. 
            However, with the explosion of technology during this period, commercial space became much more lucrative. This opened the doors for SpaceX and ULA to find cost effective measures to reach space efficiently, and would soon essentially replace NASA entirely, with the US government awarding the
             two companies contracts to send different payloads into orbit as well ''')

st.markdown('## Proposal')
st.markdown('The fall of the Soviet Union played a key role in allowing companies such as SpaceX and ULA to become major players in the commercial Space Launch industry. ')

st.header('The Data')
st.markdown('The dataset titled All Space Missions from 1957 (found [here](https://www.kaggle.com/datasets/agirlcoding/all-space-missions-from-1957?resource=download)) The data can be found in one CSV file, and has a shape of 4,324 rows and 9 columns. Those columns were... ')
st.markdown('- Two unnamed columns counting each row')
st.markdown('- Company Name denoting which particular company / organization launched each SLV')
st.markdown('- Location showing which launch site was used')
st.markdown('- Datum which had a string valued and a detailed down to the minute day and time of launch')
st.markdown('- Detail explaining what rocket was used / its payload')
st.markdown('- Status Rocket having two string values inside, the two being StatusActive or StatusRetired')
st.markdown('- Rocket which didnt provide much explanation for, just had numeric float values')
st.markdown('- Status Mission which like the Status Rocket column, had two values string. Success or Failure')

st.header('Visualizations')

# using the 'images' folder didn't work with streamlit it seems, but I went directly to my midterm repository and copied the image address, shown below
st.markdown('### NASA vs USSR comparison')
st.markdown('![NASA USSR comparison](https://github.com/ghodgin/space-launch/blob/main/images/nasa-ussr-comparison.png?raw=true)')

st.markdown('### US based companies comparison')
st.markdown('![NASA USSR comparison](https://github.com/ghodgin/space-launch/blob/main/images/nasa-spacex-ula-2000-and-onward.png?raw=true)')
st.markdown('### Adding Russia to the mix')
st.markdown('![NASA USSR comparison](https://github.com/ghodgin/space-launch/blob/main/images/russia-comparison.png?raw=true)')

st.header('Conclusion')
st.markdown('The Fall of the Soviet Union drastically effected the amount of launches that the United States was doing. In the early 2000s, NASA would pivot to a different focus, from exploration to research and development. This, paired with the rising commercial value of space allowed for companies like SpaceX and ULA to find cost effective ways to send payloads into space, and ultimately led to those companies and others to take the reigns in regards to the space launch industry. According to the data, NASA has completely stopped sending their own rockets and payloads into space. It is almost ironic that after the fall of the Soviet Union, capitalism prevailed and now civilian companies are outpacing every other nation on the planet, and doing it in a very cost effective measure. This provides us with a brief glimpse at a possible future of Space Flight and exploration, where the motives to send things up have shifted from more of a political and militaristic reason, to more of a profit oriented reason. ')

# found out st.header exists
# gonna try to animate the graphs lol

def launch_graphs():
    launch_df = pd.read_csv("data/Space_Corrected.csv")

    ## Clean the launch data and change the date column to datetime format
    cleaned_launch_df = launch_df.drop(['Unnamed: 0.1', 'Unnamed: 0'], axis=1)
    cleaned_launch_df['Date'] = cleaned_launch_df['Datum'].str[:16]
    cleaned_launch_df.drop(columns=['Datum'], inplace=True)
    cleaned_launch_df['Date'] = pd.to_datetime(cleaned_launch_df['Date'], format='%a %b %d, %Y')

    ## Set cutoff date for analysis
    cutoff_date = pd.to_datetime('2000-01-01')

    ## Filter data for US organizations
    combined_names = ['SpaceX', 'NASA', 'ULA']
    combined_nasa_spacex_ula = cleaned_launch_df[cleaned_launch_df['Company Name'].str.contains('|'.join(combined_names))]
    america_rahh_df = combined_nasa_spacex_ula[combined_nasa_spacex_ula['Date'] > cutoff_date]
    launch_counts = america_rahh_df.groupby(['Date', 'Company Name']).size().reset_index(name='Launch Count')
    grouped_counts = launch_counts.groupby(['Company Name', launch_counts['Date'].dt.year])['Launch Count'].sum().reset_index()

    ## Create the US organizations launch graph
    fig, ax = plt.subplots(figsize=(12, 6))
    sns.barplot(x='Date', y='Launch Count', hue='Company Name', data=grouped_counts, palette='Paired', ax=ax)
    ax.set_title('Number of Launches over time by US organizations / companies')
    ax.set_xlabel('Date')
    ax.set_ylabel('Number of launches')
    ax.set_xticklabels(ax.get_xticklabels(), rotation=45, size=9)
    plt.tight_layout()

    return fig

# Main Streamlit code to display the animated graph
if __name__ == '__main__':
    st.title('Space Launch Analysis')

    # Generate the initial plot
    fig = launch_graphs()

    # Display the initial plot using st.pyplot()
    st.pyplot(fig)

    # Animation loop
    for year in range(2000, 2024):
        # Update plot data based on the selected year
        # Note: This is a simplified example assuming the data doesn't change with each year
        fig = launch_graphs()

        # Display the updated plot using st.pyplot()
        st.pyplot(fig)