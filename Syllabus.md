# Overview

This year we are 'flipping' the classroom. That means that we expect you to come to 'lecture' (***except*** in Week 1!) having already watched the assigned videos and completed the assigned readings. This means that there is a mix of 'asynchronous' (work that you do in your own time) and 'synchronous' (work that we do during scheduled hours) interaction. For those unable to attend a 'synchronous' activity because of Time Zone issues we *intend* to make a recording available afterwards, but we expect that a 2-hour recording of a group discussion and live coding session will be rather less educational and informative than actually *being there* so recordings should not be used as a substitute for attendance.

### Preparation

The nature and amount of preparation will vary from week to week, but may include:

- Readings from both academic and non-academic sources.
- Recorded lectures from CASA staff.
- Recorded videos from non-CASA staff.
- short Moodle quizzes to test your completion of readings and videos.
- Contributions to a weekly '[Padlet](https://en-gb.padlet.com/)' that will be used to guide the 'synchronous' sessions.

### 'Lecture'

The 'lecture' in your timetable will be used for a mix of discussion and 'live coding' (eeek!) using the following framework:

- We will review questions and issues arising from the previous week's practical session.
- We will use ***your*** contributions to the week's Padlet to prioritise discussion around concepts and readings with which students are struggling or wish to engage further.
- We will have a 'live coding' session following an 'I do/We do' format: we will employ concepts covered in the week's preparation activities, as well as approaches that will be explored further in the practical, to look a real-world data set *together* using code.

So we're going to call these **workshops** instead! These will take place on Zoom and can be accessed using the 'activity' specified on the [Lectures and Workshop Material](https://moodle.ucl.ac.uk/course/view.php?id=11291&section=2) page.

### Practical

There are two timetabled practical sessions; we will inform you of your assigned session. These will also take place on Zoom and can *also* be accessed using the 'activity' specified on the [Lectures and Workshop Material](https://moodle.ucl.ac.uk/course/view.php?id=11291&section=2) page of Moodle.

# Week 1: Setting Up

This week is focussed on getting you set up for the rest of the course in terms of having the requisite software installed and accounts configured so that you can keep track of your work, write code, and track changes.

### Preparation

Although none of these activities are *compulsory* in advance of the first session, getting your computer set up to code *does* take time and most of these preparatory activites are fairly straightforward... with a few exceptions noted below. If you are able to get these tools installed in advance then you can focus on the taught content in the first two practicals rather than also wrestling with an installation. This will also give us more time to help you if you discover that you're one of the unlucky people for whom installation is a lot more work!

#### Computer Health Check-up

Please ensure that your computer is fully up-to-date with Operating System and application updates. Also, please make a note of the following three things:

- What Operating System and Version is your _main_ computer running? [Help for Windows](https://support.microsoft.com/en-gb/help/13443/windows-which-version-am-i-running). [Help for Mac](https://support.apple.com/en-gb/HT201260).
- How much RAM does your _main_ computer have? [Help for Windows](https://www.howtogeek.com/435644/how-to-see-how-much-ram-is-in-your-pc-and-its-speed/). [Help for Mac](https://www.macworld.co.uk/how-to/mac/much-ram-need-more-3793418/).
- How much free disk space does your _main_ computer have? [Help for Windows](https://www.lifewire.com/how-to-check-free-hard-drive-space-in-windows-2619187). [Help for Mac](https://www.macworld.com/article/2972775/how-to-check-a-mac-free-hard-drive-space.html).

This information will be very useful during the first few weeks when you are most likely to encounter problems with the programming environment. *Generally* speaking, the things to watch out for are:

1. Your operating system is Windows 10 Home, or something older than Windows 10 (*e.g.* Windows 8 or ealier), or MacOS older than 10.13 (High Sierra).
2. Your computer has less than 8GB of RAM.
3. Your computer has less than 15GB of free disk space remaining.

#### Installing Command Line Tools 

If you want to get a *little* bit ahead of things, then you should try to install one of:

- **Mac:** the Xcode Command Line Tools, which can be done [directly from the Terminal](https://osxdaily.com/2014/02/12/install-command-line-tools-mac-os-x/).
- **Windows:** Git Bash, for which you can follow [these instructions](https://www.stanleyulili.com/git/how-to-install-git-bash-on-windows/).

#### Installing the Programming Environment

If you want to get even *more* ahead of things, then the single most important thing you can do is to install the programming environment. This is the stage where you're most likely to encounter problems that will need our assistance, so knowing that you need our help here means that you ask for it much sooner!

So we have created **installation videos** with transcripts for [Macs](https://web.microsoftstream.com/video/d94bc09d-02c9-45cf-83ed-3badeab3568b) as well as [Windows](https://web.microsoftstream.com/video/ca31d99c-1c98-4a84-abb8-e40bfd307dd6). There are also written instructions that you can follow for [installing Vagrant](https://github.com/jreades/sds_env/tree/master/vagrant), if you prefer. 

##### Windows Issues

If you are on a Windows machine and receive this error:

> *VBoxManage.exe: error: Not in a hypervisor partition (HVP=0) (VERR_NEM_NOT_AVAILABLE).*
> *VBoxManage.exe: error: VT-x is disabled in the BIOS for all CPU modes (VERR_VMX_MSR_ALL_VMX_DISABLED)*
> *VBoxManage.exe: error: Details: code E_FAIL (0x80004005), component ConsoleWrap, interface IConsole*

Then you have two options:

1. Talk to use about how to enable Hypervisor in the BIOS for computer.
2. Switch to installing [Anaconda Python directly](https://github.com/jreades/sds_env/tree/master/conda).

We'd recommend \#1 first as it will be useful to have 'virtualisation' enabled on your computer anyway, but we have \#2 has a backup if that's just not possible for some reason!

### Workshop


- Poll Time! The password for all Padlets can be found on Moodle.
  - **Poll**: [Where in the world are you?](https://padlet.com/jreades1/o5xckdew9o6f5jay)
  - **Poll**: [Hopes, fears, and expectations of this module?](https://padlet.com/jreades1/ve3t55wfw4rul8by) ([Recording](https://web.microsoftstream.com/video/979f3dfb-57b1-40ad-9c08-3e21c29e2d2f))

- 1.1: [Getting Oriented & Getting Help](https://github.com/jreades/i2p/blob/master/lectures/1.1-Getting_Oriented.md) ([Recording](https://web.microsoftstream.com/video/553fcc7c-f361-45a8-bb20-69055d345a01))
- 1.2: [Tools of the Trade](https://github.com/jreades/i2p/blob/master/lectures/1.2-Tools_of_the_Trade.md) ([Recording](https://web.microsoftstream.com/video/86991aba-0305-4cb5-bbb9-f89a5fbebe46))
- 1.3: [Writing Code](https://github.com/jreades/i2p/blob/master/lectures/1.3-Writing_Code.md) ([Recording](https://web.microsoftstream.com/video/2713168e-47cf-4df6-8cf2-2e9059cc698a))

### Practical

If you have already installed the programming environment then the practical can be downloaded from [GitHub](https://github.com/jreades/i2p/blob/master/practicals/Practical-01-Getting_Started.ipynb) (Click on `Raw` and then `Save File As...`) and viewed by saving it to your `Documents/CASA/...` folder, or you can just [view it online](https://github.com/jreades/i2p/blob/master/practicals/Practical-01-Getting_Started.ipynb) in your web browser.

# Week 2: Foundations (Part 1)

### Preparation

#### Installing Command Line Tools 

If you didn't get to this during the practical then *please* do it before we get to Week 2's practical! You need to install one of:

- **Mac:** the Xcode Command Line Tools, which can be done [directly from the Terminal](https://osxdaily.com/2014/02/12/install-command-line-tools-mac-os-x/).
- **Windows:** Git Bash, for which you can follow [these instructions](https://www.stanleyulili.com/git/how-to-install-git-bash-on-windows/).

#### Installing the Programming Environment

See the [previous week's instructions](#installing-the-programming-environment). It is *vital* that you try to get this installed **before this week's practical**. If you encounter difficulties we will need time to help you, so the sooner you know that you need help, the faster we can help you.

#### Code Camp

If you have ***not* completed [Code Camp](https://kingsgeocomputation.org/teaching/code-camp/code-camp-python/)**, then we would strongly recommend that you tackle *Notebooks 3–5* as preparation for the week's class.

#### Optional: Git & GitHub

If you would like to have more time to focus on coding, please try to get your local computer and GitHub synchronising your *Introduction to Programming* (suggested name: `i2p`) project. Click on the still below to access the video on Streams.

[![Screen Grab from Git and GitHub](https://raw.githubusercontent.com/jreades/i2p/master/practicals/img/Git_GitHub.png)](https://web.microsoftstream.com/video/29a31977-ff9e-4b53-92d3-ee3bb2a769f6)

There are written instructions in the Week's practical.

#### Lectures

As we're working in a 'flipped' environment, you should watch these videos *before* class so that the 'live' (a.k.a. 'synchronous') session can focus on demonstration, discussion, and clarification. This week is very busy because we need to cover off the basics for those of you who were unable to engage with [Code Camp](https://kingsgeocomputation.org/teaching/code-camp/code-camp-python/), while recapping only the crucial bits for those of you who *were* able to do so: 

- Watch: [Python: the Basics](https://web.microsoftstream.com/video/dc5951ed-33fb-43a7-8e30-19ec2b41cb1f) ([Notes](https://github.com/jreades/i2p/blob/master/lectures/2.3-Python_the_Basics.md))
- Watch: [Lists](https://web.microsoftstream.com/video/21ef45cf-c432-4882-be54-e9bdbdaf7a3b) ([Notes](https://github.com/jreades/i2p/blob/master/lectures/2.4-Lists.md))
- Watch: [Iteration](https://web.microsoftstream.com/video/ecbf2b2b-6d11-4df0-a28b-caed2badbea1) ([Notes](https://github.com/jreades/i2p/blob/master/lectures/2.5-Iteration.md))
- Watch: [The Command Line](https://web.microsoftstream.com/video/5cd2a59c-ab53-4e75-a607-dd5de5e61681) ([Notes](https://github.com/jreades/i2p/blob/master/lectures/2.6-The_Command_Line.md))
- Watch: [Getting Stuck Into Git](https://web.microsoftstream.com/video/aa0f7893-4fb5-4af1-ad44-af8e352f4d52) ([Notes](https://github.com/jreades/i2p/blob/master/lectures/2.7-Git.md))

#### Readings

- [@Burton:1963] [DOI](https://doi.org/10.1111/j.1541-0064.1963.tb00796.x)
- [@ArribasBel:2018] [DOI](https://doi.org/10.1111/gec3.12403)

#### Contribution

- Padlet: [Collaborative Agenda](https://padlet.com/jreades1/7l6grf09kujmjrus)

#### Quiz!

- Complete the [short Moodle quiz](https://moodle.ucl.ac.uk/mod/quiz/view.php?id=2388403) associated with this week's activities.

### Workshop

- Review of **Collaborative Agenda** ([Recording](https://web.microsoftstream.com/video/a850dc75-cb3b-431c-a870-d9b4a4b7af29))
- Discussion of **Readings** ([Recording](https://web.microsoftstream.com/video/fdc94583-2409-4bfe-9a30-eda34bc28398))

- Geography and Computers ([Notes](https://github.com/jreades/i2p/blob/master/lectures/2.1-Computers_in_Planning_and_Geography.md))
- Principles of Programming ([Notes](https://github.com/jreades/i2p/blob/master/lectures/2.2-Principles_of_Programming.md))
- **Live Coding** ([Recording](https://web.microsoftstream.com/video/374b3c32-56db-42f4-8fc2-c1833a976dce))

### Practical

This week's practical requires you to have **completed installation of the programming environment**. The practical can be downloaded from [GitHub](https://github.com/jreades/i2p/raw/master/practicals/Practical-02-Foundations_1.ipynb).

# Week 3: Foundations (Part 2)

### Preparation

#### Code Camp

*All* students should complete/revisit [Code Camp](https://mybinder.org/v2/gh/kingsgeocomp/code-camp-env/notebook-v1.0?urlpath=git-pull%3Frepo%3Dhttps%253A%252F%252Fgithub.com%252Fkingsgeocomp%252Fcode-camp%26urlpath%3Dtree%252Fcode-camp%252F%26branch%3Dmaster) Notebooks 8–11.

**Note:** there is an issue with the GeoJSON tasks in Notebooks 8 and 9. We can discuss in the Workshop.

#### Lectures

This week we start to move beyond [Code Camp](https://kingsgeocomputation.org/teaching/code-camp/code-camp-python/). So although you should recognise many of the _parts_ that we discuss,  you'll see that we start to put them together in a new way:

- Watch: [Dictionaries](https://web.microsoftstream.com/video/041f9734-9368-429c-8f91-2208f9c2ba07) ([Notes](https://github.com/jreades/i2p/blob/master/lectures/3.1-Dictionaries.md))
- Watch: [LOLs](https://web.microsoftstream.com/video/129b862b-cb1b-41ab-a6ad-d526eff3fd20) ([Notes](https://github.com/jreades/i2p/blob/master/lectures/3.2-LOLs.md))
- Watch: [DOLs to Data](https://web.microsoftstream.com/video/28266460-26b2-4455-ab42-1456f483a412) ([Notes](https://github.com/jreades/i2p/blob/master/lectures/3.3-DOLs_to_Data.md))
- Watch: [Functions](https://web.microsoftstream.com/video/3bd3fe3a-5dea-4ac8-a3e2-49ab50b862aa) ([Notes](https://github.com/jreades/i2p/blob/master/lectures/3.4-Functions.md))
- Watch: [Packages](https://web.microsoftstream.com/video/0ef82489-8c35-4532-a459-596d8e8f9633) ([Notes](https://github.com/jreades/i2p/blob/master/lectures/3.5-Packages.md))

#### Readings

- [@Etherington:2016] [DOI](https://doi.org/10.1080/03098265.2015.1086981)
- [@Donoho:2017] [DOI](https://doi.org/10.1080/10618600.2017.1384734)
- [@Unwin:1980] [DOI](https://doi.org/10.1080/03098268008708772)

#### Contribution

- Padlet: [Collaborative Agenda](https://padlet.com/jreades1/qsbkobbnbpo057yz)

#### Quiz!

- Complete the [short Moodle quiz](https://moodle.ucl.ac.uk/mod/quiz/view.php?id=24300940) associated with this week's activities.

### Workshop

- Reviewing the **Collaborative Agenda** ([Recording Part 1](https://web.microsoftstream.com/video/024260b1-8c2d-4ffe-abc2-a9fe62630afd) and [Recording Part 2](https://web.microsoftstream.com/video/dd67f97f-4470-43be-b2a2-6b862ee80fc3))
- Discussion of **Readings** ([Recording](https://web.microsoftstream.com/video/6220ab79-4a31-447a-9916-6cb7e3917453))
- **Live Coding** ([Recording](https://web.microsoftstream.com/video/b5df930f-82ba-40a1-9d61-26174b58d2b3))

### Practical

The practical can then be downloaded from [GitHub](https://github.com/jreades/i2p/raw/master/practicals/Practical-03-Foundations_2.ipynb).

# Week 4: Object-Oriented Programming

### Preparation

#### Lectures

- Watch: [Methods](https://web.microsoftstream.com/video/d953bec3-667d-4330-88ca-07deb9c68c9a) ([Notes](https://github.com/jreades/i2p/blob/master/lectures/4.1-Methods.md))
- Watch: [Classes](https://web.microsoftstream.com/video/8727d485-199e-4f49-ab87-0848366a55ea) ([Notes](https://github.com/jreades/i2p/blob/master/lectures/4.2-Classes.md))
- Watch: [Design](https://web.microsoftstream.com/video/caade180-3e55-463c-a5b9-4572dd2cd2f3) ([Notes](https://github.com/jreades/i2p/blob/master/lectures/4.3-Design.md))
- Watch: [Exceptions](https://web.microsoftstream.com/video/ab802229-9eb2-46c3-8fa6-a6dec56a6828) ([Notes](https://github.com/jreades/i2p/blob/master/lectures/4.4-Errors.md))

#### Readings

- [@Cox:2016] [PDF](http://insideairbnb.com/reports/how-airbnbs-data-hid-the-facts-in-new-york-city.pdf)
- [@dignazio:2020, chap. 5] **Unicorns, Janitors, Ninjas, Wizards, and Rock Stars** [Pre-review Chapter URL](https://bookbook.pubpub.org/pub/fcshwhq6)

#### Contribution

- Padlet: [Collaborative Agenda](https://padlet.com/jreades1/hmrlizd62gfilfz7)

#### Quiz!

- Complete the [early feedback questionnaire](https://moodle.ucl.ac.uk/mod/questionnaire/view.php?id=2429914) please!

### Workshop

- Reviewing the **Collaborative Agenda** ([Recording](https://web.microsoftstream.com/video/927265a6-a3c4-4855-b96e-834b3fd90a07))
- Discussion of **Readings** (see Above)
- **Live Coding** ([Part 2](https://web.microsoftstream.com/video/97baab26-6aad-43f5-a9f8-afb633b59d58); [Part 3](https://web.microsoftstream.com/video/2c593785-436d-4490-b591-b12379440ea5))

### Practical

The practical can be [downloaded from GitHub](https://github.com/jreades/i2p/blob/master/practicals/Practical-04-Objects.ipynb).

# Week 5: Numeric Data

### Preparation

#### Lectures

- Watch: [Logic](https://web.microsoftstream.com/video/b9684684-5210-4917-8066-c7c247872051) ([Notes](https://github.com/jreades/i2p/blob/master/lectures/5.1-Logic.md))
- Watch: [Randomness](https://web.microsoftstream.com/video/18ee48e3-81d9-42d2-9e24-d434a9aa06ce) ([Notes](https://github.com/jreades/i2p/blob/master/lectures/5.2-Randomness.md))
- Watch: [Data Files](https://web.microsoftstream.com/video/465db9d5-fc82-42f7-ada4-089a01de1d7b) ([Notes](https://github.com/jreades/i2p/blob/master/lectures/5.3-Files.md))
- Watch: [Pandas](https://web.microsoftstream.com/video/ce84fd59-b44f-40cb-804b-593613053e24) ([Notes](https://github.com/jreades/i2p/blob/master/lectures/5.4-Pandas.md))

#### Readings

- [@dignazio:2020, chap. 4] **What Gets Counted Counts** in *Data Feminism*; [Pre-review URL](https://bookbook.pubpub.org/pub/rykaknh1)
- [@Wachsmuth:2018] [DOI](https://doi.org/10.1177%2F0308518X18778038)
- [@Harris:2018] [URL](https://www.theguardian.com/commentisfree/2018/feb/12/profiteers-killing-airbnb-erode-communities)

#### Contribution

- Padlet: [Collaborative Agenda](https://padlet.com/jreades1/pg23spvbkfytbcnu)

### Workshop

- Brief Discussion of **Assessments* ([Recording](https://web.microsoftstream.com/video/b2ccf725-3328-4acc-9f13-fe84f0fa8f4d))
- Reviewing the **Collaborative Agenda** ([Recording](https://web.microsoftstream.com/video/3b0ebe4e-3407-4a41-a76b-6102fc89147b))
- Discussion of **Readings** ([Recording](https://web.microsoftstream.com/video/3b0ebe4e-3407-4a41-a76b-6102fc89147b?st=822))
- **Live Coding** ([Recording](https://web.microsoftstream.com/video/05870663-8cf2-464e-9932-e6e550077d0f))

### Practical

The practical can be [downloaded from GitHub](https://github.com/jreades/i2p/blob/master/practicals/Practical-05-Numeric_Data.ipynb).

# Reading Week

You should be doing the readings that will support your answers to Assessment #2. And, looking ahead to the Final Assessment and where you might find ideas or literature to support your thinking, I'd suggest having a browse of the [Full Bibliography](https://github.com/jreades/i2p/blob/master/bib/Bibliography.md). This is a working document and I will add more items as and when I come across them or new works are published!

### Readings

In addition to looking for relevant content in [@dignazio:2020] ([URL](https://bookbook.pubpub.org/data-feminism)), you will also want to check consider:

- [@Elwood:2017] [DOI](https://doi.org/10.1080/13658816.2017.1334892)
- [@Elwood:2018] [DOI](https://doi.org/10.1080/0966369X.2018.1465396)
- [@Bemt:2018] [DOI](https://doi.org/10.1080/03098265.2018.1436534)
- [@Amoore:2019] [DOI](https://doi.org/10.1177%2F0263276419851846)
- [@Crawford:2015] [DOI](https://doi.org/10.1007/s10708-014-9597-z)

# Week 6: Spatial Data

### Preparation

#### Lectures

- Watch: [Mapping](https://web.microsoftstream.com/video/74559a29-4214-4f79-8d41-06293ba1bade) ([Notes](https://github.com/jreades/i2p/blob/master/lectures/6.1-Mapping.md))
- Watch: [GeoPandas](https://web.microsoftstream.com/video/b79dab45-1390-40e9-b97b-ffd3c63e55d6) ([Notes](https://github.com/jreades/i2p/blob/master/lectures/6.2-Geopandas.md))
- Watch: [EDA](https://web.microsoftstream.com/video/bf4b47c4-2bbc-4989-a11c-cc3be529cef1) ([Notes](https://github.com/jreades/i2p/blob/master/lectures/6.3-EDA.md))
- Watch: [ESDA](https://web.microsoftstream.com/video/5c0a28b2-eb42-4ace-baed-a0fa9131aa4a) ([Notes](https://github.com/jreades/i2p/blob/master/lectures/6.4-ESDA.md))

#### Readings

- [@dignazio:2020, chap. 6] **The Numbers Don't Speak for Themselves** in *Data Feminism*; [Pre-review URL](https://bookbook.pubpub.org/pub/6ui5n4vo)
- [@Elwood:2017] [DOI](https://doi.org/10.1080/13658816.2017.1334892) 

#### Contribution

- Padlet: [Collaborative Agenda](https://padlet.com/jreades1/48f8jhrni5cplyo2)

#### Quiz!

- Complete the [short Moodle quiz](https://moodle.ucl.ac.uk/mod/quiz/view.php?id=2532856) associated with this week's activities.

### Workshop

- Reviewing the **Collaborative Agenda** ([Recording](https://web.microsoftstream.com/video/74a13a37-c319-4747-a695-2540b1d83d07))
- Discussion of **Readings** (see [Collaborative Agenda](https://web.microsoftstream.com/video/74a13a37-c319-4747-a695-2540b1d83d07))
- **Live Coding** ([Recording](https://web.microsoftstream.com/video/292b318e-223d-48dd-9e2e-efe33c1acb3d))

### Practical

The practical can be [downloaded from GitHub](https://github.com/jreades/i2p/blob/master/practicals/Practical-06-Spatial_Data.ipynb).

# Week 7: Textual Data 

### Preparation

#### Lectures

- Watch: [Notebooks as Documents](https://web.microsoftstream.com/video/fa80e0b3-a14a-44dd-b9b5-1774dde219ba) ([Notes](https://github.com/jreades/i2p/blob/master/lectures/7.1-Notebooks_as_Documents.md))
- Watch: [Patterns in Text](https://web.microsoftstream.com/video/9e419529-f1d7-40a9-94e3-3adf8c4608f6) ([Notes](https://github.com/jreades/i2p/blob/master/lectures/7.2-Patterns_in_Text.md))
- Watch: [Cleaning Text](https://web.microsoftstream.com/video/3a7ad210-31fb-4d15-8e33-3bea705042e2) ([Notes](https://github.com/jreades/i2p/blob/master/lectures/7.3-Cleaning_Text.md))
- Watch: [Analysing Text](https://web.microsoftstream.com/video/edcbccdd-15b9-49da-b84a-691b5cc41b88) ([Notes](https://github.com/jreades/i2p/blob/master/lectures/7.4-Analysing_Text.md))


#### Readings

- [@Ladd:2020] [Web Page](https://programminghistorian.org/en/lessons/common-similarity-measures)
- [@Lavin:2019] [Web Page](https://programminghistorian.org/en/lessons/analyzing-documents-with-tfidf)

#### Contribution

- Padlet: [Collaborative Agenda](https://padlet.com/jreades1/15mbt34zr6v8e861)

#### Quiz!

- Complete the [short Moodle quiz](https://moodle.ucl.ac.uk/mod/quiz/view.php?id=2555003) associated with this week's activities.

### Workshop

- Reviewing the **Collaborative Agenda** ([Recording](https://web.microsoftstream.com/video/bc6c55dd-a34d-41bb-919b-a7f781570777))
- Discussion of **Readings** (see above)
- **Live Coding** ([Recording](https://web.microsoftstream.com/video/0bc57b29-6840-45e6-8cda-e7ec88acef5e))

### Practical

The practical can then be [downloaded from GitHub](https://github.com/jreades/i2p/blob/master/practicals/Practical-07-Textual_Data.ipynb).

# Week 8: Visualising Data

### Preparation

#### Lectures

- Watch: [Linking Data](https://web.microsoftstream.com/video/05759776-10b9-4476-9949-c7c0fbeef298) ([Notes](https://github.com/jreades/i2p/blob/master/lectures/8.1-Linking_Data.md))
- Watch: [Linking Spatial Data](https://web.microsoftstream.com/video/4bf27eaa-90d8-4628-81ba-e673816e691f) ([Notes](https://github.com/jreades/i2p/blob/master/lectures/8.2-Linking_Spatial_Data.md))
- Watch: [Grouping Data](https://web.microsoftstream.com/video/7f8df345-7339-466c-be60-a65be1ad6b57) ([Notes](https://github.com/jreades/i2p/blob/master/lectures/8.3-Grouping_Data.md))
- On Telling Stories with Data

#### Readings

- [@dignazio:2020, chap. 3] On Rational, Scientific, Objective Viewpoints from Mythical, Imaginary, Impossible Standpoints in Data Feminism; [Pre-review URL](https://bookbook.pubpub.org/pub/8tjbs2x5)
- Badger, E. and Bui, Q. and Gebeloff, R. (2019) Neighborhood Is Mostly Black. The Home Buyers Are Mostly White. New York Times [URL](https://www.nytimes.com/interactive/2019/04/27/upshot/diversity-housing-maps-raleigh-gentrification.html)

#### Contribution

- Padlet: [Collaborative Agenda](https://padlet.com/jreades1/iwn12kf61hfyhbx5)

#### Quiz!

- Complete the short Moodle quiz associated with this week's activities.

### Workshop

- Reviewing the **Collaborative Agenda**
- Discussion of **Readings**
- **Live Coding**

### Practical

The practical can then be downloaded from GitHub.

# Week 9: Classifying Data 

### Preparation

#### Lectures

- Normalisation & Standardisation
- Transformations 
- PySAL
- Aggregation & Joins

#### Readings

- Bunday, B.D. (????) A Final Tale or You Can Prove Anything with Figures [URL](https://www.ucl.ac.uk/~ucahhwi/AFinalTale.pdf)
- Harris, R. (2019), The Certain Uncertainty of University Rankings [URL](https://rpubs.com/profrichharris/uni-rankings)
- Cima, R. (2014) The Most and Least Diverse Cities in America, Priceonomics [URL](https://priceonomics.com/the-most-and-least-diverse-cities-in-america/) [But need to provide PDF as figures now missing]

#### Contribution

- Padlet: [Collaborative Agenda](https://padlet.com/jreades1/7w9x315mt1vjaadm)

#### Quiz!

- Complete the short Moodle quiz associated with this week's activities.

### Workshop

- Reviewing the **Collaborative Agenda**
- Discussion of **Readings**
- **Live Coding**

### Practical

The practical can then be downloaded from GitHub.

# Week 10: Grouping Data 

### Preparation

#### Lectures

- Dimensionality Reduction
- Clustering 

#### Readings

- Shapiro, W. and Yavuz, M. (2017) Rethinking 'distance' in New York City Medium [URL](https://medium.com/topos-ai/rethinking-distance-in-new-york-city-d17212d24919)


#### Contribution

- Padlet: [Collaborative Agenda](https://padlet.com/jreades1/r5xk6texlxwgga3u)

#### Quiz!

- Complete the short Moodle quiz associated with this week's activities.

### Workshop

- Reviewing the **Collaborative Agenda**
- Discussion of **Readings**
- **Live Coding**

### Practical

The practical can then be downloaded from GitHub.

Bibliography
============

::: {#refs}
:::
