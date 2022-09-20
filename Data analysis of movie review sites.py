#!/usr/bin/env python
# coding: utf-8

# ___
# 
# <a href='http://www.pieriandata.com'><img src='../Pierian_Data_Logo.png'/></a>
# ___
# <center><em>Copyright by Pierian Data Inc.</em></center>
# <center><em>For more information, visit us at <a href='http://www.pieriandata.com'>www.pieriandata.com</a></em></center>

# # Capstone Project
# ## Overview
# 
# If you are planning on going out to see a movie, how well can you trust online reviews and ratings? *Especially* if the same company showing the rating *also* makes money by selling movie tickets. Do they have a bias towards rating movies higher than they should be rated?
# 
# ### Goal:
# 
# **Your goal is to complete the tasks below based off the 538 article and see if you reach a similar conclusion. You will need to use your pandas and visualization skills to determine if Fandango's ratings in 2015 had a bias towards rating movies better to sell more tickets.**
# 
# ---
# ---
# 
# **Complete the tasks written in bold.**
# 
# ---
# ----
# 
# ## Part One: Understanding the Background and Data
# 
# 
# **TASK: Read this article: [Be Suspicious Of Online Movie Ratings, Especially Fandango’s](http://fivethirtyeight.com/features/fandango-movies-ratings/)**

# ----
# 
# **TASK: After reading the article, read these two tables giving an overview of the two .csv files we will be working with:**
# 
# ### The Data
# 
# This is the data behind the story [Be Suspicious Of Online Movie Ratings, Especially Fandango’s](http://fivethirtyeight.com/features/fandango-movies-ratings/) openly available on 538's github: https://github.com/fivethirtyeight/data. There are two csv files, one with Fandango Stars and Displayed Ratings, and the other with aggregate data for movie ratings from other sites, like Metacritic,IMDB, and Rotten Tomatoes.
# 
# #### all_sites_scores.csv

# -----
# 
# `all_sites_scores.csv` contains every film that has a Rotten Tomatoes rating, a RT User rating, a Metacritic score, a Metacritic User score, and IMDb score, and at least 30 fan reviews on Fandango. The data from Fandango was pulled on Aug. 24, 2015.

# Column | Definition
# --- | -----------
# FILM | The film in question
# RottenTomatoes | The Rotten Tomatoes Tomatometer score  for the film
# RottenTomatoes_User | The Rotten Tomatoes user score for the film
# Metacritic | The Metacritic critic score for the film
# Metacritic_User | The Metacritic user score for the film
# IMDB | The IMDb user score for the film
# Metacritic_user_vote_count | The number of user votes the film had on Metacritic
# IMDB_user_vote_count | The number of user votes the film had on IMDb

# ----
# ----
# 
# #### fandango_scape.csv

# `fandango_scrape.csv` contains every film 538 pulled from Fandango.
# 
# Column | Definiton
# --- | ---------
# FILM | The movie
# STARS | Number of stars presented on Fandango.com
# RATING |  The Fandango ratingValue for the film, as pulled from the HTML of each page. This is the actual average score the movie obtained.
# VOTES | number of people who had reviewed the film at the time we pulled it.

# ----
# 
# **TASK: Import any libraries you think you will use:**

# In[1]:


import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


# In[174]:





# ## Part Two: Exploring Fandango Displayed Scores versus True User Ratings
# 
# Let's first explore the Fandango ratings to see if our analysis agrees with the article's conclusion.
# 
# **TASK: Run the cell below to read in the fandango_scrape.csv file**

# In[2]:


fandango = pd.read_csv("fandango_scrape.csv")


# **TASK: Explore the DataFrame Properties and Head.**

# In[4]:


fandango.head()


# In[5]:


fandango.info()


# In[6]:


fandango.describe()


# **TASK: Let's explore the relationship between popularity of a film and its rating. Create a scatterplot showing the relationship between rating and votes. Feel free to edit visual styling to your preference.**

# In[179]:


# CODE HERE


# In[10]:


plt.figure(figsize=(10,4),dpi=200)
sns.scatterplot(data = fandango, x = 'RATING', y = 'VOTES')


# **TASK: Calculate the correlation between the columns:**

# In[11]:


fandango.corr()


# In[182]:





# **TASK: Assuming that every row in the FILM title column has the same format:**
# 
#     Film Title Name (Year)
#     
# **Create a new column that is able to strip the year from the title strings and set this new column as YEAR**

# In[183]:


# CODE HERE
fandango['YEAR'] = fandango['FILM'].apply(lambda title: title.split('(')[-1])


# In[13]:


fandango


# **TASK: How many movies are in the Fandango DataFrame per year?**

# In[15]:


#CODE HERE
fandango['YEAR'].value_counts()


# In[186]:





# **TASK: Visualize the count of movies per year with a plot:**

# In[17]:


#CODE HERE
sns.countplot(data =fandango,x = 'YEAR')


# In[188]:





# **TASK: What are the 10 movies with the highest number of votes?**

# In[189]:


#CODE HERE


# In[19]:


fandango.nlargest(10,'VOTES')


# **TASK: How many movies have zero votes?**

# In[20]:


#CODE HERE
no_votes = fandango['VOTES'] == 0
no_votes


# In[23]:


no_votes.sum()


# **TASK: Create DataFrame of only reviewed films by removing any films that have zero votes.**

# In[193]:


#CODE HERE


# In[28]:


fans_reviewed = fandango[fandango['VOTES']>0]
fans_reviewed


# ----
# 
# **As noted in the article, due to HTML and star rating displays, the true user rating may be slightly different than the rating shown to a user. Let's visualize this difference in distributions.**
# 
# **TASK: Create a KDE plot (or multiple kdeplots) that displays the distribution of ratings that are displayed (STARS) versus what the true rating was from votes (RATING). Clip the KDEs to 0-5.**

# In[195]:


#CODE HERE


# In[31]:


plt.figure(figsize = (10,4),dpi=200)
sns.kdeplot(data = fans_reviewed,x='RATING',clip=[0,5],fill=True,label='True Rating')
sns.kdeplot(data = fans_reviewed,x = 'STARS',clip=[0,5],fill = True,label = 'Stars Displayed')

plt.legend(loc = (1.05,0.5))


# **TASK: Let's now actually quantify this discrepancy. Create a new column of the different between STARS displayed versus true RATING. Calculate this difference with STARS-RATING and round these differences to the nearest decimal point.**

# In[32]:


#CODE HERE


# In[34]:


fans_reviewed['DIFF'] = fans_reviewed['STARS'] - fans_reviewed['RATING']
fans_reviewed ['DIFF']= fans_reviewed['DIFF'].round(2)


# In[199]:





# **TASK: Create a count plot to display the number of times a certain difference occurs:**

# In[200]:


#CODE HERE


# In[38]:


plt.figure(figsize=(12,4))
sns.countplot(data = fans_reviewed,x = 'DIFF')


# **TASK: We can see from the plot that one movie was displaying over a 1 star difference than its true rating! What movie had this close to 1 star differential?**

# In[41]:


#CODE HERE
fans_reviewed[fans_reviewed['DIFF'] == 1]


# In[203]:





# ## Part Three: Comparison of Fandango Ratings to Other Sites
# 
# Let's now compare the scores from Fandango to other movies sites and see how they compare.
# 
# **TASK: Read in the "all_sites_scores.csv" file by running the cell below**

# In[43]:


all_sites = pd.read_csv("all_sites_scores.csv")


# **TASK: Explore the DataFrame columns, info, description.**

# In[44]:


all_sites.head()


# In[205]:





# In[45]:


all_sites.info()


# In[46]:


all_sites.describe()


# ### Rotten Tomatoes
# 
# Let's first take a look at Rotten Tomatoes. RT has two sets of reviews, their critics reviews (ratings published by official critics) and user reviews. 
# 
# **TASK: Create a scatterplot exploring the relationship between RT Critic reviews and RT User reviews.**

# In[208]:


# CODE HERE


# In[47]:


plt.figure(figsize=(12,4),dpi=200)
sns.scatterplot(data = all_sites,x='RottenTomatoes',y ='RottenTomatoes_User' )
plt.xlim(0,100)
plt.ylim(0,100)


# Let's quantify this difference by comparing the critics ratings and the RT User ratings. We will calculate this with RottenTomatoes-RottenTomatoes_User. Note: Rotten_Diff here is Critics - User Score. So values closer to 0 means aggrement between Critics and Users. Larger positive values means critics rated much higher than users. Larger negative values means users rated much higher than critics.
# 
# **TASK: Create a new column based off the difference between critics ratings and users ratings for Rotten Tomatoes. Calculate this with RottenTomatoes-RottenTomatoes_User**

# In[210]:


#CODE HERE


# In[49]:


all_sites['DIFF'] = all_sites['RottenTomatoes'] - all_sites['RottenTomatoes_User']


# Let's now compare the overall mean difference. Since we're dealing with differences that could be negative or positive, first take the absolute value of all the differences, then take the mean. This would report back on average to absolute difference between the critics rating versus the user rating.

# **TASK: Calculate the Mean Absolute Difference between RT scores and RT User scores as described above.**

# In[50]:


# CODE HERE
all_sites['DIFF'].apply(abs).mean()


# In[213]:





# **TASK: Plot the distribution of the differences between RT Critics Score and RT User Score. There should be negative values in this distribution plot. Feel free to use KDE or Histograms to display this distribution.**

# In[214]:


#CODE HERE


# In[53]:


plt.figure(figsize=(10,4),dpi = 200)
sns.histplot(data=all_sites,x='DIFF',kde=True,bins=25)
plt.title('RT Critics Score minus RT User Score')


# **TASK: Now create a distribution showing the *absolute value* difference between Critics and Users on Rotten Tomatoes.**

# In[216]:


#CODE HERE


# In[54]:


plt.figure(figsize=(10,4),dpi=200)
sns.histplot(x=all_sites['DIFF'].apply(abs),bins = 25,kde=True)
plt.title("Abs Difference between RT Critics Score and RT User Score");


# **Let's find out which movies are causing the largest differences. First, show the top 5 movies with the largest *negative* difference between Users and RT critics. Since we calculated the difference as Critics Rating - Users Rating, then large negative values imply the users rated the movie much higher on average than the critics did.**

# **TASK: What are the top 5 movies users rated higher than critics on average:**

# In[218]:


# CODE HERE


# In[57]:


all_sites.nsmallest(5,'DIFF')[['FILM','DIFF']]


# **TASK: Now show the top 5 movies critics scores higher than users on average.**

# In[220]:


# CODE HERE


# In[59]:


all_sites.nlargest(5,'DIFF')[['FILM','DIFF']]


# ## MetaCritic
# 
# Now let's take a quick look at the ratings from MetaCritic. Metacritic also shows an average user rating versus their official displayed rating.

# **TASK: Display a scatterplot of the Metacritic Rating versus the Metacritic User rating.**

# In[222]:


# CODE HERE


# In[63]:


plt.figure(figsize=(10,4),dpi=200)
sns.scatterplot(data =all_sites,x='Metacritic',y = 'Metacritic_User')
plt.xlim(0,100)
plt.ylim(0,10)


# ## IMDB
# 
# Finally let's explore IMDB. Notice that both Metacritic and IMDB report back vote counts. Let's analyze the most popular movies.
# 
# **TASK: Create a scatterplot for the relationship between vote counts on MetaCritic versus vote counts on IMDB.**

# In[224]:


#CODE HERE


# In[64]:


sns.scatterplot(data = all_sites,x='Metacritic_user_vote_count',y = 'IMDB_user_vote_count')


# **Notice there are two outliers here. The movie with the highest vote count on IMDB only has about 500 Metacritic ratings. What is this movie?**
# 
# **TASK: What movie has the highest IMDB user vote count?**

# In[226]:


#CODE HERE


# In[67]:


all_sites.nlargest(1,'IMDB_user_vote_count')


# **TASK: What movie has the highest Metacritic User Vote count?**

# In[228]:


#CODE HERE


# In[68]:


all_sites.nlargest(1,'Metacritic_user_vote_count')


# ## Fandago Scores vs. All Sites
# 
# Finally let's begin to explore whether or not Fandango artificially displays higher ratings than warranted to boost ticket sales.

# **TASK: Combine the Fandango Table with the All Sites table. Not every movie in the Fandango table is in the All Sites table, since some Fandango movies have very little or no reviews. We only want to compare movies that are in both DataFrames, so do an *inner* merge to merge together both DataFrames based on the FILM columns.**

# In[230]:


#CODE HERE


# In[69]:


df = pd.merge(fandango,all_sites,on='FILM',how = 'inner')


# In[70]:


df.info()


# In[71]:


df.head()


# ### Normalize columns to Fandango STARS and RATINGS 0-5 
# 
# Notice that RT,Metacritic, and IMDB don't use a score between 0-5 stars like Fandango does. In order to do a fair comparison, we need to *normalize* these values so they all fall between 0-5 stars and the relationship between reviews stays the same.
# 
# **TASK: Create new normalized columns for all ratings so they match up within the 0-5 star range shown on Fandango. There are many ways to do this.**
# 
# Hint link: https://stackoverflow.com/questions/26414913/normalize-columns-of-pandas-data-frame
# 
# 
# Easier Hint:
# 
# Keep in mind, a simple way to convert ratings:
# * 100/20 = 5 
# * 10/2 = 5

# In[234]:


# CODE HERE


# In[77]:


df['RT_Norm'] = np.round(df['RottenTomatoes']/20,1) 
df['RTU_Norm'] =  np.round(df['RottenTomatoes_User']/20,1)


# In[72]:


df['Meta_Norm'] =  np.round(df['Metacritic']/20,1)
df['Meta_U_Norm'] =  np.round(df['Metacritic_User']/2,1)


# In[73]:


df['IMDB_Norm'] = np.round(df['IMDB']/2,1)


# In[78]:


df.head()


# **TASK: Now create a norm_scores DataFrame that only contains the normalizes ratings. Include both STARS and RATING from the original Fandango table.**

# In[239]:


#CODE HERE


# In[79]:


norm_scores = df[['STARS','RATING','RT_Norm','RTU_Norm','Meta_Norm','Meta_U_Norm','IMDB_Norm']]


# In[81]:


norm_scores.head()


# ### Comparing Distribution of Scores Across Sites
# 
# 
# Now the moment of truth! Does Fandango display abnormally high ratings? We already know it pushs displayed RATING higher than STARS, but are the ratings themselves higher than average?
# 
# 
# **TASK: Create a plot comparing the distributions of normalized ratings across all sites. There are many ways to do this, but explore the Seaborn KDEplot docs for some simple ways to quickly show this. Don't worry if your plot format does not look exactly the same as ours, as long as the differences in distribution are clear.**
# 
# Quick Note if you have issues moving the legend for a seaborn kdeplot: https://github.com/mwaskom/seaborn/issues/2280

# In[84]:


#CODE HERE
def move_legend(ax, new_loc, **kws):
    old_legend = ax.legend_
    handles = old_legend.legendHandles
    labels = [t.get_text() for t in old_legend.get_texts()]
    title = old_legend.get_title().get_text()
    ax.legend(handles, labels, loc=new_loc, title=title, **kws)


# In[85]:


fig, ax = plt.subplots(figsize=(15,6),dpi=150)
sns.kdeplot(data=norm_scores,clip=[0,5],shade=True,palette='Set1',ax=ax)

move_legend(ax, "upper left")


# In[244]:





# **Clearly Fandango has an uneven distribution. We can also see that RT critics have the most uniform distribution. Let's directly compare these two.** 
# 
# **TASK: Create a KDE plot that compare the distribution of RT critic ratings against the STARS displayed by Fandango.**

# In[ ]:


#CODE HERE


# In[167]:


fig,ax = plt.subplots(figsize=(!5,6),dpi =150)
sns.kdeplot(data = norm_scores[['RT_Norm','STARS']],clip=[0,5],shade = True,palette='Set1',ax=ax)


# **OPTIONAL TASK: Create a histplot comparing all normalized scores.**

# In[ ]:


#CODE HERE


# In[86]:


sns.histplot(data=norm_scores)


# 
# ### How are the worst movies rated across all platforms?
# 
# **TASK: Create a clustermap visualization of all normalized scores. Note the differences in ratings, highly rated movies should be clustered together versus poorly rated movies. Note: This clustermap does not need to have the FILM titles as the index, feel free to drop it for the clustermap.**

# In[ ]:


# CODE HERE


# In[87]:


sns.clustermap(norm_scores,cmap='magma',col_cluster=False)


# **TASK: Clearly Fandango is rating movies much higher than other sites, especially considering that it is then displaying a rounded up version of the rating. Let's examine the top 10 worst movies. Based off the Rotten Tomatoes Critic Ratings, what are the top 10 lowest rated movies? What are the normalized scores across all platforms for these movies? You may need to add the FILM column back in to your DataFrame of normalized scores to see the results.**

# In[245]:


# CODE HERE


# In[88]:


norm_films = df[['STARS','RATING','RT_Norm','RTU_Norm','Meta_Norm','Meta_U_Norm','IMDB_Norm','FILM']]


# In[89]:


norm_films.nsmallest(10,'RT_Norm')


# **FINAL TASK: Visualize the distribution of ratings across all sites for the top 10 worst movies.**

# In[ ]:


# CODE HERE


# In[94]:


print('\n\n')
plt.figure(figsize=(15,6),dpi=150)
worst_films = norm_films.nsmallest(10,'RT_Norm').drop('FILM',axis=1)
sns.kdeplot(data=worst_films,clip=[0,5],shade=True,palette='Set1')
plt.title("Ratings for RT Critic's 10 Worst Reviewed Films");


# ---
# ----
# 
# <img src="https://upload.wikimedia.org/wikipedia/en/6/6f/Taken_3_poster.jpg">
# 
# **Final thoughts: Wow! Fandango is showing around 3-4 star ratings for films that are clearly bad! Notice the biggest offender, [Taken 3!](https://www.youtube.com/watch?v=tJrfImRCHJ0). Fandango is displaying 4.5 stars on their site for a film with an [average rating of 1.86](https://en.wikipedia.org/wiki/Taken_3#Critical_response) across the other platforms!**

# In[95]:


norm_films.iloc[25]


# In[254]:


0.4+2.3+1.3+2.3+3


# In[255]:


9.3/5


# ----
