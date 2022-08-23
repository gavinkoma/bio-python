
import sys, os
import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import pingouin as pg

#this will set our working directory to be able to find the necessary documents
currentpath = os.getcwd()
newpath = os.chdir('/Users/gavinkoma/Documents/bio-python/final')
currentpath2 = os.getcwd()


class sciStats():
    # Class that does statistical analyses on a given file.

    # Initialize with filename:
    def __init__(self,inputFile='All_Data_meanofallstrides.csv'):
        self.inputFile = inputFile


    # Load and parse the data set:
    def read_parse_export_data(self):
        #okay so first lets start by loading the excel sheet into our workspace
        df = pd.read_csv(self.inputFile)
        #print(df)
        #print(type(df))
        grouped_obj = df.sort_values(['Timepoint_Name','Rat'])
        grouped_obj = grouped_obj.iloc[:,1:]
        #print(grouped_obj)

        noweek_1 = grouped_obj[grouped_obj['Timepoint_Name'] == 'week-1'].index
        grouped_obj.drop(noweek_1,inplace=True)
        #print(grouped_obj)

        noweek1 = grouped_obj[grouped_obj['Timepoint_Name'] == 'week1'].index
        grouped_obj.drop(noweek1,inplace=True)
        #print(grouped_obj)

        grouped=grouped_obj

        noweek2 = grouped[grouped['Timepoint_Name'] == 'week2'].index
        grouped.drop(noweek2,inplace = True)
        #print(grouped)

        noweek4 = grouped[grouped['Timepoint_Name'] == 'week4'].index
        grouped.drop(noweek4,inplace=True)

        # note you could also do with and statements:
        #df[df[Timepoint_Name]=='week6' & df[TimePointaame]=='week7' & ...]

        #print(grouped)
        #pd.set_option("display.max_rows",None,"display.max_columns",None)
        #print(grouped)
        #okay so now i have a dataframe that is thank god just week6-8
        #i hate how long it took me to figure out how to do that
        #actually im going to write this to a new csv file and call it again
        #so that way i can double check that i have the right data
        grouped.to_csv('week678.csv')
        self.df=df
        self.grouped=grouped


    def doWeek678(self):
        #replace all empty values with nans to do statistical analysis later
        #okay so now i need to figure out what we want to analyze
        #i have it grouped and weeks i dont need replaced
        gdf=self.grouped
        gdf.replace('',np.nan,inplace=True)

        #print(df)

        #okay so we need to choose the columns that were going to perform
        #statistical analysis on ummm
        #
        #actually we need to sort the speeds as well
        #so were going to use speed 24 because that is the closest to their natural stride

        nospeed16 = gdf[gdf['Speed_Group'] == 'speed16'].index
        gdf.drop(nospeed16,inplace = True)

        nospeed20 = gdf[gdf['Speed_Group'] == 'speed20'].index
        gdf.drop(nospeed20,inplace = True)

        nospeed28 = gdf[gdf['Speed_Group'] == 'speed28'].index
        gdf.drop(nospeed28,inplace = True)

        nospeed32 = gdf[gdf['Speed_Group'] == 'speed32'].index
        gdf.drop(nospeed32,inplace = True)

        updatedspeed = gdf
        #print(df)

        updatedspeed.to_csv('week678.csv')
        self.updatedspeed = updatedspeed


    def selectasis(self):
        # okay so chatted with spence to discuss what columns I should be analyzing here
        # and he decided to do asis height to start for week 6-8
        # we can also do ankle angle
        # other options are step duration, step height, and step length
        # if we choose to do step duration, recall that thats how long in time
        # of the a step
        # if we choose to do step length, know that it is very highly controlled
        # by whatever speed the rat is walking at
        updatedspeed=self.updatedspeed
        rat = updatedspeed["Rat"]
        timepoint = updatedspeed["Timepoint_Name"]
        speedgroup = updatedspeed["Speed_Group"]
        exptype = updatedspeed["exptype"]
        meanasis = updatedspeed["Mean_Asis_Height"]
        #print(type(rat))

        data = pd.DataFrame({'rat':rat,'timepoint':timepoint,'speeds':speedgroup,'exptype':exptype,'asis':meanasis})
        asisdata = pd.DataFrame(data)
        #print(asisdata)

        #asisdata = asisdata.groupby("exptype")
        #print(asisdata)

        asisdata = asisdata.sort_values(['exptype'])
        #print(asisdata)
        #asisdata = pd.DataFrame(['rat',rat],['timepoints',timepoint],['speed',speedgroup],['exp type',exptype],['asis data',meanasis])

        #okay so right now the asis data is sorted by cno and dreadds
        #and we need to split this into two data frames one being cno and one being dreadds
        #and then sort it again based on the time point

        cnoasis = asisdata.iloc[:18,:]
        dreaddasis = asisdata.iloc[19:,:]
        #print(cnoasis)
        #print(dreaddasis)

        #okay so now we have two separate dataframes that are cno and dreadds
        #but now i need to determine how to run the statistical anova
        #i can do cno anova for itself and i can probably do a dreadd anova for itself as well
        #but can i also do an anova for inbetween the groups? do i want to compare the cno
        #and dreadds per week?

        #cnoasis.head()
        #okay so here is a seaborn plot that shows cno vs dread improvement
        #based on week number and whether it was cno vs dreadds

        sns.set()
        anovaplot = sns.pointplot(data = data,x = 'timepoint', y = 'asis', hue = 'exptype', dodge = True, markers = ['o','s'], capsize = .1, errwidth=1, palette='colorblind')
        plt.savefig('anovafig.pdf')
        plt.show()

        #print(sns)

        #okay if i dont make block = False then the code pauses at the graph and
        #will not continue no matter what
        plt.show(block = False)

        #okay so this part below shows the mean and standard deviation
        #for each of the groups and the time points; this is what we will use to plot
        #our ANOVA soon

        df = data.groupby(['timepoint', 'exptype'])['asis'].agg(['mean', 'std']).round(2)
        print(df)



        #note to self: okay chat with dr. hey tomorrow please in regards to whether
        #or not i can use this module to compute the ANOVA; technically there were no limits
        #to what we could import but genuinely curious if this is okay or if he
        #would rather me hard-code the ANOVA

        oneway = pg.anova(data = data[data["exptype"]=="dreadds"], dv = 'asis',between = 'timepoint')
        onewaycno = pg.anova(data = data[data["exptype"]=="cno"], dv = 'asis',between = 'timepoint')
        print(oneway)
        print(onewaycno)

        aov = pg.mixed_anova(dv='asis',within='timepoint',between='exptype',subject='rat',data=data)
        #aov = pg.mixed_anova(dv='asis',within='timepoint',subject='rat',data=data)
        pg.set_default_options()
        print(aov)

        #so the cno was less significant than the dreadds
        #so for the dreadds animals this means that the withdrawal cno has no effect on asis height
        #and this is a bummer because we might have expected our dreadds acitvation to cause
        #a big improvement on asis height (no effect sad face)
        #however, our control animals where there are no dreadds, it is reassuring
        #that there was no change with the cno. which means the cno (our activation drug)
        #is not causing any changes
        #
        #so our activator is safe and we can see if there are other variables that responded in the future


        #but we dont actually know for sure if this 100% significant and such we
        #need to perform post-hoc tests on the interaction which you see below.

        posthocs = pg.pairwise_ttests(dv='asis',within='timepoint',between='exptype',subject = 'rat',data = data)
        pg.print_table(posthocs)


        #maybe just do the one way anova from dreadds and ignore the cno

    def ankleanglettests(self):
        #okay so now i need to call data again for the t-tests
        #but to do that i need to remove the extra groups and run
        #the test will be performed on week 6 because that is when the rat is immediately

        ttestdata=self.updatedspeed


        noweek7 = ttestdata[ttestdata['Timepoint_Name'] == 'week7'].index
        ttestdata.drop(noweek7,inplace=True)

        noweek8 = ttestdata[ttestdata['Timepoint_Name'] == 'week8'].index
        ttestdata.drop(noweek8,inplace=True)

        #nospeed = ttestdata[ttestdata['Speed_Group'] == 'speed24'].index
        #ttestdata.drop(nospeed,inplace=True)


        pd.set_option("display.max_rows", None, "display.max_columns", None)
        #print(ttestdata)

        rattest = ttestdata["Rat"]
        timepointtest = ttestdata["Timepoint_Name"]
        speedgrouptest = ttestdata["Speed_Group"]
        exptypetest = ttestdata["exptype"]
        ankledata = ttestdata["Max_Ankle_Height"]
        #print(type(rat))
        asisdata = pd.DataFrame({'exptype':exptypetest,'ankledata':ankledata})
        asis_data = pd.DataFrame(asisdata)
        print(asis_data)

        #okay we need to subset the data into two subset series of
        #pandas objects; for our purposes we will split them into cno and dreadds

        cno = asis_data.query('exptype == "cno"')['ankledata']
        #print(cno)

        dreadds = asis_data.query('exptype == "dreadds"')['ankledata']
        #print(dreadds)

        asis_data.groupby('exptype').describe()

        res = pg.ttest(cno,dreadds,correction = False)
        display(res)

        plt.figure()
        ttestplot = sns.boxplot(x='exptype',y='ankledata',data = asis_data)
        plt.savefig('ttestplot.pdf')
        plt.show(block = False)


        #so ankle angle is done
        #lets also look at step duration
        #step duration is how long in time the full motion of a step was


    def stepdurationttests(self):
        #Step_Duration
        #maybe in future look to remove the cno outlier
        durationdata=self.updatedspeed

        noweek7 = durationdata[durationdata['Timepoint_Name'] == 'week7'].index
        durationdata.drop(noweek7,inplace=True)
        noweek8 = durationdata[durationdata['Timepoint_Name'] == 'week8'].index
        durationdata.drop(noweek8,inplace=True)


        exptypetest = durationdata["exptype"]
        stepdurationdata = durationdata["Step_Duration"]

        #print(type(rat))
        stepduration = pd.DataFrame({'exptype':exptypetest,'stepduration':stepdurationdata})

        cnoduration = stepduration.query('exptype == "cno"')['stepduration']
        dreaddsduration = stepduration.query('exptype == "dreadds"')['stepduration']

        stepduration.groupby('exptype').describe()

        durationres = pg.ttest(cnoduration,dreaddsduration,correction = False)
        display(durationres)

        plt.figure()
        ttestplot = sns.boxplot(x='exptype',y='stepduration',data = stepduration)
        plt.savefig('durationttestplot.pdf')
        plt.show(block = False)


print("Running code using simple functions and global variables.")
print("Running code using the sciStats data class")
# make a new sciStats object iwth default file name:
mySciStatsObject=sciStats()
# load and parse the data, creating internal vairables:
mySciStatsObject.read_parse_export_data()
# run first anslysis
mySciStatsObject.doWeek678()
mySciStatsObject.selectasis()
mySciStatsObject.ankleanglettests()
mySciStatsObject.stepdurationttests()



#okay so i think this is actually done because it now has four parts saved
#to the class? we have two plot functions and we have two statistical test parameters
#saved? The ANOVA and the T-Test so i think i actually finished which is super nice
#so now i just need to make a presentations regarding the data


#dr. hey said that it will be about half regarding the data and another half regarding
#the research and maybe i can briefly discuss the libraries i imported to perform my
#tests? idk how im going to do the presentation yet but its supposed to be about 12 min

#but i did say plural ttests so maybe actually what im going to do is one more
#stride parameter for the study? spence said that step length could be interesting
#but it is highly dependent on gait speed
